import unittest
import pandas as pd


class MyTestCase(unittest.TestCase):

    def __init__(self):
        pass

    def create_dummy_dataframe(self,
                               rows: int,
                               cols: int,
                               num_cols: int,
                               cat_cols: int,
                               dt_cols: int) -> pd.DataFrame:
        self.assertEqual(True, False)


if __name__ == '__main__':
    df = pd.util.testing.makeMixedDataFrame()
    # unittest.main()
