#!/bin/bash

name="AutoPlow"

echo "Hi Autoplow"
sleep 1

source ~/code/2023/robotics/create3_examples_ws/install/local_setup.sh

ros2 action send_goal /dock irobot_create_msgs/action/DockServo "{}"


# https://iroboteducation.github.io/create3_docs/api/docking/