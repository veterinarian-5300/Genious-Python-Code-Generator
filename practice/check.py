import csv
import pandas as pd

one=pd.read_csv("pa_dashboards.csv")

two=pd.read_csv("pa_dashboards(1).csv", squeeze=True)

pattern = '|'.join(two)

exist=one['sentences'].str.contains(pattern, na=False)

with open('new.csv', 'w') as outFile:
    for cols in exist:
        if pattern in exist:
            outFile.write(exist, "1")
