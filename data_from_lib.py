from datetime import datetime
import pandas as pd
from pandas_datareader import data as pdr
import pickle
import json
import yfinance as yf
from flask import jsonify
yf.pdr_override()

import requests


url = "https://www.nl.go.kr/seoji/SearchApi.do?cert_key=	87d0f15c44993805de5164e410b1883e6842f0c00796acc5584c0ecd2315cd6b&result_style=json&page_no=1&page_size=1000"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # JSON 형태로 응답 데이터를 파싱
    # JSON 데이터를 데이터프레임으로 변환
    df = pd.DataFrame(data)
    df=df['docs']
    # 데이터프레임을 CSV 파일로 저장
    df.to_csv('user.csv', index=False)
else:
    print(f"Error: {response.status_code}")

def getLib():
    url = "https://www.nl.go.kr/seoji/SearchApi.do?cert_key=	87d0f15c44993805de5164e410b1883e6842f0c00796acc5584c0ecd2315cd6b&result_style=json&page_no=1&page_size=9"
    response = requests.get(url)

    if response.status_code == 200:
        df = response.json()  # JSON 형태로 응답 데이터를 파싱
        return(df)
    else:
        return(f"Error: {response.status_code}")
