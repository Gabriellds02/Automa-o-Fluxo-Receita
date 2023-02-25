from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 
from datetime import date
import time
import os
import shutil
import glob

# Acesso principal

class Bot:

    def __init__(self):
      
        self.nav = webdriver.Chrome(executable_path= r'./chromedriver')
      
    def rodar_bot(self):
        self.nav.get("https://aplicacoes.mds.gov.br/saa-web/login.action")
        # Dados para acesso
        login = "044.827.497-37"
        senha = "boris2023"
        # ---------------------------------------------  Acess Relatório Financeiro    --------------------------------------------
        self.nav.find_element(By.ID, 'login_user_username').send_keys(login)
        self.nav.find_element(By.ID, 'login_user_password').send_keys(senha)
        time.sleep(0.2)
        self.nav.find_element(By.ID, 'login_user_password').send_keys(Keys.ENTER)
        self.nav.find_element(By.PARTIAL_LINK_TEXT, 'SUASWEB').click()
        time.sleep(0.5)
        self.nav.find_element(By.CLASS_NAME, 'button').click()
        time.sleep(0.5)
        self.nav.find_element(By.PARTIAL_LINK_TEXT, 'Relatório').click()
        time.sleep(0.5)
        self.nav.find_element(By.PARTIAL_LINK_TEXT, 'Financeiro').click()
        time.sleep(0.5)
        self.nav.find_element(By.PARTIAL_LINK_TEXT, 'Distribuição Financeira por Piso').click()
        time.sleep(0.5)
            # ---------------------------------------------------------------------------------------------------------------

            # ---------------------------------------------  Select UF    --------------------------------------------------- 
        self.nav.find_element(By.ID, 'form:uf').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:uf').send_keys('RJ')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:uf').send_keys(Keys.ENTER)
        time.sleep(5)
    # -----------------------------------------------------------------------------------------------------------------------
    
    # ---------------------------------------------  Select Mun ------------------------------------------------------------- 
        self.nav.find_element(By.ID, 'form:municipio').click()
        time.sleep(1)
        self.nav.find_element(By.ID, 'form:municipio').send_keys('P')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:municipio').send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:municipio').send_keys(Keys.ENTER)
        time.sleep(3)
    # -----------------------------------------------------------------------------------------------------------------------

    # ---------------------------------------------  Select data  ----------------------------------------------------------- 
    # ---------------------------------------------  Select Inicial Day  ----------------------------------------------------

        self.nav.find_element(By.ID, 'form:dataInicialInputDate').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('01')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('01')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('2019')
        time.sleep(3)



       
    # ---------------------------------------------  Select Final Day  -----------------------------------------------------

        self.nav.find_element(By.ID, 'form:dataFinalInputDate').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('31')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('12')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('2019')
        time.sleep(3)
        
    # -----------------------------------------------------------------------------------------------------------------------


    # ---------------------------------------------  Select Tipo Gestão  ----------------------------------------------------

        self.nav.find_element(By.ID, 'form:canal').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:canal').send_keys('M')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:canal').send_keys(Keys.ENTER)
            # ---------------------------------------------------------------------------------------------------------------

            # ---------------------------------------------  Select Pisos Fin  ----------------------------------------------
        list_pisos_financeiros = ['APOIO FINANCEIRO AO BL PSB', 'APOIO FINANCEIRO BLMAC',
        'BPC - QUESTIONÁRIO APLICADO', 'BPC NA ESCOLA - CAPACITAÇÃO', 'BPC NA ESCOLA QUESTIONARIO APLICADO',
        'COMPONENTE - PACI CRIANÇA ADOLESCEN','COMPONENTE - PBFI', 'COMPONENTE - PTMC', 'COMPONENTE - SCFV',
        'COVID-ACOLHIMENTO', 'COVID-ALIMENTOS', 'COVID-EPI', 'IGD BOLSA FAMÍLIA', 'IGD DO SUAS',
        'IGD PROGRAMA AUXÍLIO BRASIL', 'IGD-SUAS', 'MAC-COVID-19', 'PAC-I CRIANÇA\ADOLESCE', 'PBVA-SCFV',
        'PBVII', 'PFMC - CREAS PAEFI', 'PFMC - MSE', 'PFMC-MSE', 'PISO BÁSICO FIXO', 'PISO BÁSICO TRANSIÇÃO',
        'PISO BÁSICO VARIÁVEL', 'PRIMEIRA INFANCIA NO SUAS', 'PROJOVEM', 'PSB - PORT 751-22', 'PSB Família',
        'PSB Infância', 'PSB-COVID-19', 'PSE - PORT 751-22', 'PSE AC à Pessoa com Deficiência', 'PSE MC Serv/CT',
        'PTMC', 'SIGTV ESTRUTURAÇÃO CUSTEIO', 'SIGTV ESTRUTURAÇÃO INVESTIMENTO', 'SIGTV_CUSTEIO A PARTIR 2022']


        for piso in list_pisos_financeiros:
            time.sleep(1)
            select_pisos = self.nav.find_element_by_id('form:piso') 
            drop = Select(select_pisos) 
            drop.select_by_visible_text(piso)
            time.sleep(1)
            self.nav.find_element(By.CLASS_NAME, 'btn').click()
            time.sleep(3)
            pag = self.nav.find_element_by_id('content').text
            time.sleep(1)
            if 'Nenhum registro encontrado.' in pag:
                print('Não existe arquivo para download')
            else:
                self.nav.find_element_by_xpath('//*[@id="form:botoes4"]/span[1]/span/input').click()
            time.sleep(1)
    # --------------------------------------------  Movimentando arquivos -------------------------------------------       
        origem = r'C:\Users\Escritorio\Downloads'
        files = glob.glob(os.path.join(origem, 'RelatorioDistribuicaoFinanceiraPiso*.csv'))
        dst = r'I:\Meu Drive\Prestação de Contas\Prestação de Contas FMAS (Geral)\2019\Detalhamento da Receita'
        delete = glob.glob(os.path.join(dst, 'RelatorioDistribuicaoFinanceiraPiso*.csv'))

        for file in delete:
            if os.path.isfile(file):
                os.remove(file)
                
        for file in files:
            if os.path.isfile(file):
                shutil.move(file, dst)

    # ---------------------------------------------------------------------------------------------------------------
bot = Bot()
bot.rodar_bot()