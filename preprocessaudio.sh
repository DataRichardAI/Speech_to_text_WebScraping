
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
/