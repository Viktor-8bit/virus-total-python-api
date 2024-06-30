


import pandas as pd
import os


def excel_reader() -> list:

    urls = pd.read_excel(f"{os.getcwd()}\\urls.xlsx", sheet_name="url")

    urls_head = urls.head()

    data = []

    for url in urls_head["URLS"]:
        data.append(url)
        
    return data


