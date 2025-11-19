import pandas as pd
import os

def load_csv(path: str):
    """
    CSV 파일을 안전하게 불러오는 함수.

    Parameters
    ----------
    path : str
        파일 경로 (예: 'data/raw/01.bike/bike.csv')

    Returns
    -------
    pandas.DataFrame
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ 파일을 찾을 수 없습니다: {path}")
    
    df = pd.read_csv(path)
    return df


def load_all_data(folder_path: str, file_extension="csv"):
    """
    폴더 안에 있는 CSV 파일 전체를 불러오는 함수.
    
    예:
    load_all_data("data/raw/01.bike/")
    """
    dataframes = {}

    for file in os.listdir(folder_path):
        if file.endswith(file_extension):
            full_path = os.path.join(folder_path, file)
            df_name = file.replace("." + file_extension, "")
            dataframes[df_name] = pd.read_csv(full_path)

    return dataframes