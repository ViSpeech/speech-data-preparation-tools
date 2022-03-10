from pydub import AudioSegment
from pydub.silence import split_on_silence
#reading from audio mp3 file
sound = AudioSegment.from_mp3("data/data_separate/output.mp3")
# spliting audio files
audio_chunks = split_on_silence(sound, min_silence_len=5000, silence_thresh=-40, keep_silence=True)
#loop is used to iterate over the output list
for i, chunk in enumerate(audio_chunks):
   output_file = "data/data_split/chunk{0}.mp3".format(i)
   print("Exporting file", output_file)
   chunk.export(output_file, format="mp3")