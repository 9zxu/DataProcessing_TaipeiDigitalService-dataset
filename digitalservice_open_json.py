import pandas as pd
import json

# read json file: https://officeguide.cc/python-read-write-json-encode-decode-tutorial-examples/
with open("/Users/graceyu/Program/crawler/digitalservice_datasets.json") as f:
    dic = json.load(f)
# print(dic)
print(type(dic))
df = pd.DataFrame(dic)
print(list(df.columns))
df.to_csv("digitalservice.csv")
