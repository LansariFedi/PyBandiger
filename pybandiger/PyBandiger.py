from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd

class PyBandiger:
    def __init__(self):
        self.le = {}
        self.ss = StandardScaler()

    def clean(self, data):
        data = data.copy()
        cat_col = data.select_dtypes(include='object').columns
        num_col = data.select_dtypes(include=['int', 'float']).columns
        for col in cat_col:
            data[col] = data[col].fillna('Missing')
        for col in num_col:
            data[col] = data[col].fillna(data[col].mean())
        return data

    def EncodeAndScale_fit(self, data):
        data = data.copy()
        cat_col = data.select_dtypes(include='object').columns
        num_col = data.select_dtypes(include=['int', 'float']).columns
        for col in cat_col:
            encoder = LabelEncoder()
            data[col] = encoder.fit_transform(data[col])
            self.le[col] = encoder
        data[num_col] = self.ss.fit_transform(data[num_col])
        return data

    def EncodeAndScale_transform(self, data):
        data = data.copy()
        cat_col = data.select_dtypes(include='object').columns
        num_col = data.select_dtypes(include=['int', 'float']).columns
        for col in cat_col:
            if col in self.le:
                data[col] = self.le[col].transform(data[col])
            else:
                raise ValueError(f"Column '{col}' was not fitted with an encoder.")
        data[num_col] = self.ss.transform(data[num_col])
        return data