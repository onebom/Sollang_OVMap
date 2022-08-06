import pickle as pkl
import pandas as pd
import csv

object = []
with open("./dataset/val_allroom.pkl", "rb") as f:
    object = pkl.load(f)

with open(r'./dataset/val_allroom.csv', 'w') as f:
    writer = csv.writer(f)
    for line in object:
        writer.writerow(line)
