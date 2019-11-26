#!/bin/bash

echo "Video and GPS startup"
printf "Participant ID: "
read answer
echo "$answer"

cd ~/Desktop/ParticipantData

# create a new directory for the participant and go to that directory
mkdir "$answer"
mkdir "$answer"/VIDEO
mkdir "$answer"/VIDEO/QUAD

# start the video recording
python ~/Desktop/DataRecordingCode/startVideo.py "$answer"/VIDEO/QUAD

# UNCOMMENT THIS WHEN YOU GET THE BU-353S4 GPS WORKING
 #mkdir "$answer"/GPS

# start the GPS logger
# python ~/Desktop/DataRecordingCode/GPSLogger.py "$answer"/GPS
