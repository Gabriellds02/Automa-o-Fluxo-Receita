
import os
import shutil
import glob


origem = r'C:\Users\Escritorio\Downloads'
files = glob.glob(os.path.join(origem, 'RelatorioDistribuicaoFinanceiraPiso*.csv'))
dst = r'I:\Meu Drive\Prestação de Contas\Prestação de Contas FMAS (Geral)\2022\Detalhamento da Receita'
delete = glob.glob(os.path.join(dst, 'RelatorioDistribuicaoFinanceiraPiso*.csv'))


for file in delete:
    if os.path.isfile(file):
        os.remove(file)
        
for file in files:
    if os.path.isfile(file):
        shutil.move(file, dst)
