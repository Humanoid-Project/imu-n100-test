# IMU N100 Test

ROS 2 Humble workspace for testing the WHEELTEC N100 IMU.

## References

[![Reference: serial-ros2](https://img.shields.io/badge/reference-serial--ros2-181717?logo=github)](https://github.com/RoverRobotics-forks/serial-ros2)
[![Reference: ros2_wheeltec_n100_imu](https://img.shields.io/badge/reference-ros2__wheeltec__n100__imu-181717?logo=github)](https://github.com/NDHANA94/ros2_wheeltec_n100_imu)

## Quick Start

```bash
cd ~/imu_ws
source /opt/ros/humble/setup.bash
colcon build
source install/setup.bash
```

```bash
# Find the IMU serial port
ls /dev/ttyUSB* /dev/ttyACM*

# Grant read/write permission
sudo chmod 666 /dev/ttyUSB0
```

```bash
# Use the detected port path instead of /dev/ttyUSB0 if needed
ros2 run wheeltec_n100_imu imu_node --ros-args -p serial_port:="/dev/ttyUSB0"
```

```bash
ros2 topic list
ros2 topic echo /imu
```
