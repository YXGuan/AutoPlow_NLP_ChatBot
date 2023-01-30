#!/bin/bash

name="AutoPlow"

echo "Hi Autoplow"
sleep 1

source ~/code/2023/robotics/create3_examples_ws/install/local_setup.sh

ros2 run teleop_twist_keyboard teleop_twist_keyboard

https://github.com/iRobotEducation/create3_examples/tree/galactic/create3_teleop