from pydub import AudioSegment
from pydub.silence import detect_nonsilent
import random
import os
import tqdm
import logging
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


def split_on_silence(
        path_audio,
        out_folder="data/data_split",
        lower_bound=6000,
        upper_bound=12000,
        rand_bound=0.9):
    logging.info(f"Reading audio from {path_audio}...")
    sound = AudioSegment.from_mp3(path_audio)

    logging.info(f"Detecting nonsilent...")
    lst_nonsilent = detect_nonsilent(
        sound, min_silence_len=500, silence_thresh=-40)

    start_time = 0
    end_time = 0
    i = 0
    check = False

    os.makedirs(out_folder, exist_ok=True)
    logging.info(f"Saving clips to {out_folder}...")
    for idx, seg in enumerate(tqdm.tqdm(lst_nonsilent)):
        end_time = seg[1]
        if check:
            start_time = seg[0]

        if end_time - start_time >= lower_bound \
                or random.uniform(0, 1) > rand_bound \
                or (idx + 1 < len(lst_nonsilent) and lst_nonsilent[idx + 1][1] - start_time > upper_bound):
            i += 1
            sound[max(0, start_time - 100):min(end_time + 100, len(sound))] \
                .export(os.path.join(out_folder, f'chunk_{i}.mp3'), format="mp3")
            check = True
        else:
            check = False


if __name__ == '__main__':
    split_on_silence("data/data_separate/output.mp3")
