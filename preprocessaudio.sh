#!/bin/bash

# Take inputs from user
INP=$1
OUT=$2
N=$3

# Create output directory if it doesn't exist
if [ ! -d $OUT ]
then
    mkdir $OUT
fi


# Loop through all files in input directory
for file in $INP/*.mp3; do
    # Use ffmpeg to convert audio to WAV format with 16KHz sampling rate and mono channel
    ffmpeg -i $file -ac 1 -ar 16000 $OUT/$(basename $file .mp3).wav &
    # Limit the number of parallel processes to num_cpus
    while [ $(jobs | wc -l) -ge $N ]; do
        sleep 1
    done
done

# Wait for all background jobs to complete
wait





# Add any additional preprocessing steps here
# For example, to remove the last 10 seconds of audio from each file:
# for file in $output_dir/*.wav
# do
#     duration=$(ffprobe -i $file -show_entries format=duration -v quiet -of csv="p=0")
#     trimmed_duration=$(bc -l <<< "$duration - 10")
#     ffmpeg -i $file -ss 0 -to $trimmed_duration -c copy $file.tmp
#     mv $file.tmp $file
# done
