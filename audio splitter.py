from pydub import AudioSegment


def split_wav(input_file, output_prefix):
    try:
        # Load the .wav file
        audio = AudioSegment.from_wav(input_file)

        # Calculate the duration of each piece (in milliseconds)
        duration_ms = len(audio)
        piece_duration = duration_ms // 3

        # Split the audio into three parts
        part1 = audio[:piece_duration]
        part2 = audio[piece_duration:2*piece_duration]
        part3 = audio[2*piece_duration:]

        # Export the three parts as separate files
        part1.export(f"{output_prefix}_part1.wav", format="wav")
        part2.export(f"{output_prefix}_part2.wav", format="wav")
        part3.export(f"{output_prefix}_part3.wav", format="wav")

        print(
            f"Audio has been split into three parts: {output_prefix}_part1.wav, {output_prefix}_part2.wav, {output_prefix}_part3.wav.")

    except Exception as e:
        print(f"Error: {e}")


# Specify the input file and output prefix
# Replace with your input file path
input_file = "C:/Users/Rafia/Desktop/Thesis Files/EdAcc Corpus/edacc_v1.0/edacc_v1.0/data/EDACC-C30.wav"
# Replace with your desired output prefix
output_prefix = "C:/Users/Rafia/Downloads/EDACC-C30"

# Run the function
split_wav(input_file, output_prefix)
