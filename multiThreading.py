from concurrent.futures import ThreadPoolExecutor, wait
import requests
import pandas as pd
from tqdm import tqdm

def punctuate(text, index):
    res = requests.post('http://127.0.0.1:5000/v1/punctuation/bn', json={"rawText":text})
    if res.ok:
        output = res.json()
        with open ("data/texts_punc/"+str(index)+".txt", "w", encoding="utf8") as f:
            f.write((output["punctText"]))

def batch_punctuate(texts):
    tasks = []

    with ThreadPoolExecutor(max_workers=1) as executor:
        for i in tqdm(range(len(texts))):
            tasks.append(executor.submit(punctuate, texts[i], i))

    wait(tasks)


if __name__ == "__main__":
    df = pd.read_excel("data/bn_bd.xlsx")
    puncTexts = list()
    for i in tqdm(range(0, 2)):
        puncTexts.append(df.Text[i]+"\n")
    batch_punctuate(puncTexts)
    print("DONE")