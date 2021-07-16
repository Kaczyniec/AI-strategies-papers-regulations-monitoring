#!/usr/bin/env python3
# coding: utf-8
from Api import Api
import pandas as pd
from utils import get_oecd_df
import os


OUT_DOCS_PATH = "data/oecd_html/"

if __name__ == "__main__":
    if os.path.isfile("oecd.csv"):
        df = pd.read_csv("oecd.csv", index_col=0)
    else:
        df = get_oecd_df()
        df.to_csv("oecd.csv")
    api = Api(headless=True)

    for index, row in df.iterrows():
        filename = OUT_DOCS_PATH + "/%s.html" % index
        if "pdf" in row["documentUrl"]:
            continue
        if os.path.isfile(filename):
            continue
        try:
            api.save_article(row["documentUrl"], filename)
        except:
            continue
