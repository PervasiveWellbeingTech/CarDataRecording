#!/bin/bash

echo "IMU startup:"
printf "Participant ID: "
read participant
echo "$participant"

cd ~/Desktop/ParticipantData

mkdir "$participant"/IMU_Seat

# start the IMU logger
python ~/Desktop/DataRecordingCode/imu_logger_seat.py "$participant"/IMU_seat
