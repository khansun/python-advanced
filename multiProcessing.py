from concurrent.futures import ProcessPoolExecutor, wait
from tqdm import tqdm
import re
import os
from pydub import AudioSegment
from timeit import timeit

def resample_audio(file):
    newAudio = AudioSegment.from_wav(file)    
    newAudio = newAudio.set_frame_rate(22050)
    newAudio = newAudio.set_sample_width(2) 
    newAudio = newAudio.set_channels(1)
    output = re.sub("wavs/", "wavs_res/", file)
    newAudio.export(output,format='wav')
    
    

def batch_resample(files):
    tasks = []
    
    with ProcessPoolExecutor(max_workers=8) as executor:
        for file in tqdm(files):
            tasks.append(executor.submit(resample_audio, "wavs/"+file))
        print("Batch Resampling Audio...")    
    
    wait(tasks)


if __name__ == "__main__":
    execution_time = timeit('import os \nbatch_resample(os.listdir("wavs"))', number=1,setup="from __main__ import batch_resample")
    print(str(len(os.listdir("wavs")))+" WAVs Resampled Successfully!")
    print('Execution Time (s): ' + str(execution_time))
