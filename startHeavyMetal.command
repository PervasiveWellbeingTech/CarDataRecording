echo "Breathing Nudges"
printf "Participant ID: "
read answer
echo "$answer"

cd ~/Desktop/ParticipantData

echo "Starting Metal"

cd "$answer"
mkdir Metal

cd Metal
python ~/Desktop/DataRecordingCode/Metal.py





