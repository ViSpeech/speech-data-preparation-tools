from pydub import AudioSegment
from pydub.silence import detect_nonsilent
import random

def split_on_silence(path_audio):
    sound = AudioSegment.from_mp3(path_audio)
    lst_nonsilent = detect_nonsilent(sound, min_silence_len=500, silence_thresh=-40)
    start_time = 0
    end_time = 0
    i = 0
    check = False
    for seg in lst_nonsilent:
        end_time = seg[1]
        if check:
            start_time = seg[0]
        if end_time - start_time > 6000 or random.uniform(0, 1) > 0.95:
            i +=1
            sound[start_time:end_time].export(f'data/data_split/chunk_{i}.mp3', format="mp3")
            print('write chunk ', i)
            check = True
        else:
            check = False

if __name__ == '__main__':
    split_on_silence("data/data_separate/output.mp3")