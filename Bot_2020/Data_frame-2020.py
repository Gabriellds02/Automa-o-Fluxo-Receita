import os
import pandas as pd
import glob
from pathlib import Path
import pathlib



class BaseDados:

    def __init__(self):
        self.principal = Path(r'I:\Meu Drive\Prestação de Contas\Prestação de Contas FMAS (Geral)\2020\Detalhamento da Receita')
        self.csv_files = glob.glob(os.path.join(self.principal, "*.csv"))
        self.caminho_backup = pathlib.Path(r'I:\Meu Drive\Prestação de Contas\Prestação de Contas FMAS (Geral)\2020\Detalhamento da Receita')

    def logica(self):
        principal_list = []
        #list_grafico1 = []
        for f in self.csv_files: 
            df = pd.read_csv(f, encoding='latin1', sep=';')
            df.columns = df.columns.str.replace(' ', '') 
            df.drop(['Total'], axis=1, inplace=True)
            df.drop(1, axis=0, inplace=True)
            df.drop(2, axis=0, inplace=True)
            for i in df:
                if "Programa/Piso" not in i:
                    df [['Valor', 'Data Pagamento']] = df[i].str.split(' /', expand=True)
                    for piso in df['Programa/Piso']:
                        pass
                        for data in df['Data Pagamento']:
                            pass
                            for valor in df['Valor']:
                                principal_list.append([piso, data, valor])
        new_df = pd.DataFrame(principal_list, columns=['Programa/Piso','Data Pagamento', 'Valor'])
        new_df['Valor'].str.replace(' ', '')
        new_df = new_df.sort_values(by=['Valor'], ascending=False)
        nome_arquivo = f'Data_Base.csv'
        local_arquivo = self.caminho_backup/nome_arquivo
        new_df.to_csv(local_arquivo, sep=';', encoding='utf-8-sig', decimal=',', index=True)
        display(new_df)
    
rodar_bot = BaseDados()
rodar_bot.logica()
    