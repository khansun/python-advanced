from concurrent.futures import ProcessPoolExecutor, wait
import codecs
import re
import os
from pydub import AudioSegment
def resample_audio(file):
    print("Start: "+file)
    newAudio = AudioSegment.from_wav(file)
    newAudio = AudioSegment.from_wav(file)
    newAudio = newAudio.set_frame_rate(22050)
    newAudio = newAudio.set_sample_width(2) 
    newAudio = newAudio.set_channels(1)
    newAudio.export(re.sub(".wav", "_res.wav", file),format='wav')
    print("End: "+file)


def batch_resample(files):
    tasks = []

    with ProcessPoolExecutor(max_workers=4) as executor:
        for file in files:
            tasks.append(executor.submit(resample_audio, "wavs/"+file))

    wait(tasks)


if __name__ == "__main__":
    filePaths = os.listdir("wavs")
    batch_resample(filePaths)
