#!/bin/bash


if [ -e /dev/ttyACM0 ]; then
  echo "detected IMU module"
  sudo chmod 666 /dev/ttyACM0
  echo "added sudo"

else
  echo "can't find imu"
fi

if [ -e ~/my_ros2_ws/src/rt_usb_9axisimu_driver ]; then
  gnome-terminal -- bash -c "ls; source ~/my_ros2_ws/install/setup.bash ; ros2 launch rt_usb_9axisimu_driver rt_usb_9axisimu_driver.launch.py; bash"
  echo "running rt_usb_9axisimu_driver"

else
  echo " can't find my_ros2_ws"
fi

sleep 3
ros2 lifecycle set rt_usb_9axisimu_driver configure
ros2 lifecycle set rt_usb_9axisimu_driver activate

RT_TOPIC_NAME=$(ros2 topic list | grep /imu)
echo ${RT_TOPIC_NAME}

