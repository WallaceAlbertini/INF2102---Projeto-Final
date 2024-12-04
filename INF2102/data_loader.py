import pandas as pd
from random import randint

class DataLoader():
   
    def __init__(self) -> None:
        self.df_out = pd.DataFrame(columns=['Categoria', 'Quote'])
        pass

    def load_excel(self,file_name,list_of_sheets,first_row=4):
        for sheet_name in list_of_sheets:
            xlsx = pd.ExcelFile(file_name)
            #load dataset as pd dataframe
            df = pd.read_excel(xlsx, sheet_name=sheet_name)
            df = df.iloc[first_row-2:].reset_index(drop=True)
            for i, row in df.iterrows():
                quote = row['Quotes']
                # Seleciona as colunas da quarta até a décima usando iloc
                categorias_nao_nan = row.iloc[4:11]  # Pega as colunas do intervalo
                categorias_nao_nan = categorias_nao_nan[categorias_nao_nan.notna()]  # Filtra as não NaN
                categorias_nao_nan = categorias_nao_nan.index.tolist()  # Converte os índices em uma lista
                if len(categorias_nao_nan) == 1:
                    tamanho = len(categorias_nao_nan)
                    self.df_out = pd.concat([self.df_out, pd.DataFrame([{'Categoria': categorias_nao_nan[randint(0, tamanho-1)], 'Quote': quote}])], ignore_index=True)
        return self.df_out
    
    def get_y_true(self):
        return self.df_out['Categoria']
    
    def get_df(self):
        return self.df_out