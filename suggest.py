import numpy as np
import pandas as pd
import json

def suggest_model(book_list_json):
    data=book_list_json['docs']
    df = pd.DataFrame(data)
    #subject가 좋아요 싫어요 -> 결과의 묶을 지표.