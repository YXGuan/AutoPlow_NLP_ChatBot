#!/bin/bash

name="AutoPlow"

echo "Hi Autoplow"
sleep 1

ros2 action send_goal /wall_follow irobot_create_msgs/action/WallFollow "{follow_side: 1, max_runtime: {sec: 1, nanosec: 0}}"

# https://iroboteducation.github.io/create3_docs/api/wall-follow/