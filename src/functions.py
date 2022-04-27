import numpy as np
import pandas as pd
from typing import List


def get_categoricals(df: pd.DataFrame) -> List[str]:
    """Return a list of categorical column names in a dataframe"""
    return [i for i in list(df.columns) if df[i].dtypes in ['object', 'category']]

