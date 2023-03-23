import pandas as pd
import os

class Converter:

    def array_to_csv(self, dict, name):
        df = pd.DataFrame(dict)
        res = df.to_excel(f"{name}.xlsx")
        return os.path.abspath(f"{name}.xlsx")