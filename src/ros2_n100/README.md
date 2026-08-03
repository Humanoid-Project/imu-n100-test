# ros2_n100

ROS2 Humble packages for the WHEELTEC N100 IMU

## Run

```bash
source /opt/ros/humble/setup.bash
colcon build
source install/setup.bash

ros2 run wheeltec_n100_imu imu_node --ros-args -p serial_port:="/dev/ttyUSB0"
```

## `/imu` Topic

Message type: `sensor_msgs/msg/Imu`

Typical topic info:

```text
Type: sensor_msgs/msg/Imu
Publisher count: 1
Subscription count: 0
```

```text
# ROS timestamp and frame name
header.stamp
header.frame_id

# 3D orientation as quaternion
orientation.x
orientation.y
orientation.z
orientation.w

# Angular velocity in rad/s
angular_velocity.x
angular_velocity.y
angular_velocity.z

# Linear acceleration in m/s^2
linear_acceleration.x
linear_acceleration.y
linear_acceleration.z

# Measurement uncertainty hints
orientation_covariance
angular_velocity_covariance
linear_acceleration_covariance
```

## Plots

[![README: imu_gravity](https://img.shields.io/badge/README-imu__gravity-1f6feb?logo=markdown&logoColor=white)](imu_test/README.md)