import pandas as pd

from constants import PHRASES_FILEPATH

def init_sentences():

    df_phrases = pd.read_csv(PHRASES_FILEPATH)

    df_phrases = df_phrases.sample(frac=1).reset_index(drop=True)

    return df_phrases['phrase_portuguese'].tolist()