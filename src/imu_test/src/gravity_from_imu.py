import math

import rclpy
from geometry_msgs.msg import Vector3Stamped
from rclpy.node import Node
from sensor_msgs.msg import Imu


def normalize_quaternion(q):
    norm = math.sqrt(sum(value * value for value in q))
    if norm < 1e-12:
        raise ValueError("IMU orientation quaternion is too small")
    return tuple(value / norm for value in q)


def quaternion_multiply(a, b):
    ax, ay, az, aw = a
    bx, by, bz, bw = b
    return (
        aw * bx + ax * bw + ay * bz - az * by,
        aw * by - ax * bz + ay * bw + az * bx,
        aw * bz + ax * by - ay * bx + az * bw,
        aw * bw - ax * bx - ay * by - az * bz,
    )


def quaternion_conjugate(q):
    x, y, z, w = q
    return (-x, -y, -z, w)


def inverse_rotate_vector(q, vector):
    q = normalize_quaternion(q)
    vector_quat = (vector[0], vector[1], vector[2], 0.0)
    rotated = quaternion_multiply(
        quaternion_multiply(quaternion_conjugate(q), vector_quat),
        q,
    )
    return rotated[:3]


class GravityFromImu(Node):
    def __init__(self):
        super().__init__("gravity_from_imu")

        self.declare_parameter("imu_topic", "/imu")
        self.declare_parameter("gravity_topic", "/projected_gravity")
        self.declare_parameter("log_every_n", 20)

        self.imu_topic = self.get_parameter("imu_topic").value
        self.gravity_topic = self.get_parameter("gravity_topic").value
        self.log_every_n = self.get_parameter("log_every_n").value
        self.message_count = 0

        self.publisher = self.create_publisher(Vector3Stamped, self.gravity_topic, 10)
        self.subscription = self.create_subscription(
            Imu,
            self.imu_topic,
            self.imu_callback,
            10,
        )

        self.get_logger().info(
            f"Subscribing to {self.imu_topic}, publishing {self.gravity_topic}"
        )

    def imu_callback(self, msg):
        quaternion = (
            msg.orientation.x,
            msg.orientation.y,
            msg.orientation.z,
            msg.orientation.w,
        )

        try:
            gravity = inverse_rotate_vector(quaternion, (0.0, 0.0, -1.0))
        except ValueError as error:
            self.get_logger().warn(str(error))
            return

        output = Vector3Stamped()
        output.header = msg.header
        if not output.header.frame_id:
            output.header.frame_id = "imu"
        output.vector.x = gravity[0]
        output.vector.y = gravity[1]
        output.vector.z = gravity[2]

        self.publisher.publish(output)
        self.message_count += 1

        if self.log_every_n > 0 and self.message_count % self.log_every_n == 0:
            self.get_logger().info(
                "projected_gravity "
                f"x={gravity[0]: .4f}, y={gravity[1]: .4f}, z={gravity[2]: .4f}"
            )


def main(args=None):
    rclpy.init(args=args)
    node = GravityFromImu()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
