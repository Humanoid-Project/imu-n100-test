from glob import glob

from setuptools import setup

package_name = "imu_gravity"

setup(
    name=package_name,
    version="0.0.1",
    package_dir={"": "src"},
    py_modules=["gravity_from_imu"],
    data_files=[
        ("share/ament_index/resource_index/packages", [f"resource/{package_name}"]),
        (f"share/{package_name}", ["package.xml"]),
        (f"share/{package_name}/launch", glob("launch/*.launch.py")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="polygon",
    maintainer_email="polygon@example.com",
    description="Projected gravity test node for IMU data.",
    license="MIT",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "gravity_from_imu = gravity_from_imu:main",
        ],
    },
)
