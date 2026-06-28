from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    serial_port = LaunchConfiguration("serial_port")

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "serial_port",
                default_value="/dev/ttyUSB0",
                description="Serial port path for the N100 IMU.",
            ),
            Node(
                package="wheeltec_n100_imu",
                executable="imu_node",
                name="imu_node",
                output="screen",
                parameters=[
                    {
                        "serial_port": serial_port,
                    }
                ],
            ),
            Node(
                package="imu_gravity",
                executable="gravity_from_imu",
                name="gravity_from_imu",
                output="screen",
            ),
            Node(
                package="rqt_plot",
                executable="rqt_plot",
                name="projected_gravity_plot",
                output="screen",
                arguments=[
                    "/projected_gravity/vector/x",
                    "/projected_gravity/vector/y",
                    "/projected_gravity/vector/z",
                ],
            ),
        ]
    )
