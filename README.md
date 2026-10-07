# IMU N100 Test

Workspace for testing the WHEELTEC N100 IMU

| | Path |
| --- | --- |
| ROS2 SDK | [![src/ros2_n100](https://img.shields.io/badge/src-ros2__n100-1f6feb?logo=github&logoColor=white)](src/ros2_n100/) |
| Cpp SDK | [![src/cpp_n100](https://img.shields.io/badge/src-cpp__n100-1f6feb?logo=github&logoColor=white)](src/cpp_n100/) |

## Quick Start

### Cpp_N100
[![README: cpp_n100](https://img.shields.io/badge/README-cpp__n100-1f6feb?logo=markdown&logoColor=white)](src/cpp_n100/README.md)

```bash
git clone https://github.com/Humanoid-Project/imu-n100-test.git IMU_N100_Test
cd IMU_N100_Test/src/cpp_n100
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j
```

```bash
# Find the IMU serial port
ls /dev/ttyUSB* /dev/ttyACM*

# Grant read/write permission
sudo chmod 666 /dev/ttyUSB0
```

```bash
# Sensor state and link statistics
./build/read_imu /dev/ttyUSB0 921600

# Mount rotation as roll pitch yaw in degrees
./build/read_imu /dev/ttyUSB0 921600 180 0 0

# 50 Hz control loop
./build/rl_observation /dev/ttyUSB0 921600 50
```

### ROS2_Humble_N100
[![README: ros2_n100](https://img.shields.io/badge/README-ros2__n100-1f6feb?logo=markdown&logoColor=white)](src/ros2_n100/README.md)

```bash
git clone https://github.com/Humanoid-Project/imu-n100-test.git IMU_N100_Test
cd IMU_N100_Test
git clone https://github.com/RoverRobotics-forks/serial-ros2.git src/ros2_n100/serial-ros2
git clone https://github.com/NDHANA94/ros2_wheeltec_n100_imu.git src/ros2_n100/ros2_wheeltec_n100_imu
git -C src/ros2_n100/ros2_wheeltec_n100_imu apply ../patches/wheeltec_n100_imu_geometry_msgs.patch
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
# Use the detected port path instead of /dev/ttyUSB0
ros2 run wheeltec_n100_imu imu_node --ros-args -p serial_port:="/dev/ttyUSB0"
```

</br>

## `/imu` Topic
[![README: ros2_n100](https://img.shields.io/badge/README-ros2__n100-1f6feb?logo=markdown&logoColor=white)](src/ros2_n100/README.md)

## Topic Plot
[![README: imu_gravity](https://img.shields.io/badge/README-imu__gravity-1f6feb?logo=markdown&logoColor=white)](src/ros2_n100/imu_test/README.md)

</br>

## References
[![Reference: serial-ros2](https://img.shields.io/badge/reference-serial--ros2-181717?logo=github)](https://github.com/RoverRobotics-forks/serial-ros2)
[![Reference: ros2_wheeltec_n100_imu](https://img.shields.io/badge/reference-ros2__wheeltec__n100__imu-181717?logo=github)](https://github.com/NDHANA94/ros2_wheeltec_n100_imu)

</br>

## License

Licensed under the [Apache License 2.0](LICENSE). Copyright 2026 RoboNex. Third-party ROS 2 packages are cloned, not included; see [NOTICE](NOTICE).
