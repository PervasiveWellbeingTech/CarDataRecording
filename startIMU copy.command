#!/bin/bash

echo "IMU startup:"

echo "$participant"

cd ~/Desktop/ParticipantData

mkdir IMU

# start the IMU logger
python ~/Desktop/DataRecordingCode/imu_logger.py IMU 12
