import pandas as pd

def clean_comments(raw_comments):
    df = pd.DataFrame(raw_comments)
    df.dropna(subset=['text'], inplace=True)
    df['publishedAt'] = pd.to_datetime(df['publishedAt'])
    return df