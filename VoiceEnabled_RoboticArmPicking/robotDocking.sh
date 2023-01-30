#!/bin/bash

name="AutoPlow"

echo "Hi Autoplow"
sleep 1



ros2 action send_goal /undock irobot_create_msgs/action/Undock "{}"


# https://iroboteducation.github.io/create3_docs/api/docking/