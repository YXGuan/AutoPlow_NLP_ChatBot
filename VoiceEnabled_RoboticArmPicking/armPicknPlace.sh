#!/bin/bash

# Note: it would be just easier to sleep for a certain seconds
# Note: but it would be more robust to use WAIT to kill only when a subprocess is finished procesing
# Long term concern: all file directories are hard-coded, would not work on a different system!
# ROS2 MoveIt is still missing a lot of features
name="AutoPlow"

echo "Hi Autoplow"
sleep 1

# with $! you get the PID of the last command launched in the background. 
PID=$!
echo "PID"
echo $PID

source /home/yuxiang/interbotix_ws/devel/setup.bash
roslaunch interbotix_xsarm_control xsarm_control.launch robot_model:=px100 &
PID1=$!

# get the PID of roslaunch
echo "PID1"
echo $PID1

echo "starts 5 seconds sleep"
sleep 5 
python3 /home/yuxiang/interbotix_ws/src/interbotix_ros_manipulators/interbotix_ros_xsarms/examples/python_demos/arm_python_api_Test1.py &

PID2=$!
echo "PID2"
echo $PID2


echo "waiting for PID2 to finish"

# https://stackoverflow.com/questions/356100/how-to-wait-in-bash-for-several-subprocesses-to-finish-and-return-exit-code-0?page=1&tab=scoredesc#tab-top
wait $PID2

echo "killing the program (PID1) in 3 seconds"
sleep 3
# kill ROSlaunch at the end. Same as control-C
kill $PID1

# Notes:
# Command to perform a recursive chmod to make all .sh files within a directory executable?
# find /directory/of/interest/ -type f -iname "*.sh" -exec chmod +x {} \;
# ps -p [PID]