from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 
from datetime import date
import time


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
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('2022')
        time.sleep(3)
    # ---------------------------------------------  Select Final Day  -----------------------------------------------------

        data_atual = date.today()
        time.sleep(0.5)
        data_em_texto = '{}{}{}'. format(data_atual.day, data_atual.month,data_atual.year)

        self.nav.find_element(By.ID, 'form:dataFinalInputDate').click()

        if 10 > data_atual.day:
            data_em_texto = '0{}'. format(data_atual.day)
            self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys(data_em_texto)
        else:
            data_em_texto ='{}'.format(data_atual.day)
            self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys(data_em_texto)

        time.sleep(1)
        if 10 > data_atual.month:
            data_em_texto = '0{}{}'. format(data_atual.month,data_atual.year)
            self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys(data_em_texto)
        else:
            data_em_texto ='{}{}'.format(data_atual.month,data_atual.year)
            self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys(data_em_texto)
        
        
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
            time.sleep(2)
            select_pisos = self.nav.find_element_by_id('form:piso') 
            drop = Select(select_pisos) 
            drop.select_by_visible_text(piso)
            time.sleep(2)
            self.nav.find_element(By.CLASS_NAME, 'btn').click()
            time.sleep(2)
            pag = self.nav.find_element_by_id('content').text
            time.sleep(2)
            if 'Nenhum registro encontrado.' in pag:
                print('Não existe arquivo para download')
            else:
                self.nav.find_element_by_xpath('//*[@id="form:botoes4"]/span[1]/span/input').click()
            time.sleep(2)
        self.nav.quit()

    def rodar_bot_2021(self):
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
            # -----------------------------------------------------------------------------------------------------------------------

            # ---------------------------------------------  Select UF    ----------------------------------------------------------- 
        self.nav.find_element(By.ID, 'form:uf').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:uf').send_keys('RJ')
        time.sleep(1)
        self.nav.find_element(By.ID, 'form:uf').send_keys(Keys.ENTER)
        time.sleep(1)
    # -----------------------------------------------------------------------------------------------------------------------
    
    # ---------------------------------------------  Select Mun   ----------------------------------------------------------- 
        self.nav.find_element(By.ID, 'form:municipio').click()
        time.sleep(1)
        self.nav.find_element(By.ID, 'form:municipio').send_keys('P')
        time.sleep(1)
        self.nav.find_element(By.ID, 'form:municipio').send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:municipio').send_keys(Keys.ENTER)
        time.sleep(0.5)
    # -----------------------------------------------------------------------------------------------------------------------

    # ---------------------------------------------  Select data  ----------------------------------------------------------- 
    # ---------------------------------------------  Select Inicial Day  ----------------------------------------------------

        self.nav.find_element(By.ID, 'form:dataInicialInputDate').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('01')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('01')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('2021')
        time.sleep(1)
    # ---------------------------------------------  Select Final Day  -----------------------------------------------------

        self.nav.find_element(By.ID, 'form:dataFinalInputDate').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('31')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('12')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('2021')
        time.sleep(1)
    # -----------------------------------------------------------------------------------------------------------------------


    # ---------------------------------------------  Select Tipo Gestão  ----------------------------------------------------

        self.nav.find_element(By.ID, 'form:canal').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:canal').send_keys('M')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:canal').send_keys(Keys.ENTER)
            # -----------------------------------------------------------------------------------------------------------------------

            # ---------------------------------------------  Select Pisos Fin  ------------------------------------------------------

        list_pisos_financeiros =['APOIO FINANCEIRO AO BL PSB', 'APOIO FINANCEIRO BLMAC',
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
            time.sleep(0.5)
            self.nav.find_element(By.CLASS_NAME, 'btn').click()
            time.sleep(0.5)
            pag = self.nav.find_element(By.ID, 'content').text
            time.sleep(0.5)
            if 'Nenhum registro encontrado.' in pag:
                print('Não existe arquivo para download')
            else:
                self.nav.find_element(By.XPATH, '//*[@id="form:botoes4"]/span[1]/span/input').click()
        self.nav.quit()

    def rodar_bot_2020(self):
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
            # -----------------------------------------------------------------------------------------------------------------------

            # ---------------------------------------------  Select UF    ----------------------------------------------------------- 
        self.nav.find_element(By.ID, 'form:uf').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:uf').send_keys('RJ')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:uf').send_keys(Keys.ENTER)
        time.sleep(0.5)
    # -----------------------------------------------------------------------------------------------------------------------
    
    # ---------------------------------------------  Select Mun   ----------------------------------------------------------- 
        self.nav.find_element(By.ID, 'form:municipio').click()
        time.sleep(1)
        self.nav.find_element(By.ID, 'form:municipio').send_keys('P')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:municipio').send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:municipio').send_keys(Keys.ENTER)
        time.sleep(0.5)
    # -----------------------------------------------------------------------------------------------------------------------

    # ---------------------------------------------  Select data  ----------------------------------------------------------- 
    # ---------------------------------------------  Select Inicial Day  ----------------------------------------------------

        self.nav.find_element(By.ID, 'form:dataInicialInputDate').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('01')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('01')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('2020')
        time.sleep(1)
    # ---------------------------------------------  Select Final Day  -----------------------------------------------------

        self.nav.find_element(By.ID, 'form:dataFinalInputDate').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('31')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('12')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('2020')
        time.sleep(1)
    # -----------------------------------------------------------------------------------------------------------------------


    # ---------------------------------------------  Select Tipo Gestão  ----------------------------------------------------

        self.nav.find_element(By.ID, 'form:canal').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:canal').send_keys('M')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:canal').send_keys(Keys.ENTER)
            # -----------------------------------------------------------------------------------------------------------------------

            # ---------------------------------------------  Select Pisos Fin  ------------------------------------------------------

        list_pisos_financeiros =['APOIO FINANCEIRO AO BL PSB', 'APOIO FINANCEIRO BLMAC',
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
            time.sleep(0.5)
            self.nav.find_element(By.CLASS_NAME, 'btn').click()
            time.sleep(0.5)
            pag = self.nav.find_element(By.ID, 'content').text
            time.sleep(0.5)
            if 'Nenhum registro encontrado.' in pag:
                print('Não existe arquivo para download')
            else:
                self.nav.find_element(By.XPATH, '//*[@id="form:botoes4"]/span[1]/span/input').click()
        self.nav.quit()

    def rodar_bot_2019(self):
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
            # -----------------------------------------------------------------------------------------------------------------------

            # ---------------------------------------------  Select UF    ----------------------------------------------------------- 
        self.nav.find_element(By.ID, 'form:uf').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:uf').send_keys('RJ')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:uf').send_keys(Keys.ENTER)
        time.sleep(0.5)
    # -----------------------------------------------------------------------------------------------------------------------
    
    # ---------------------------------------------  Select Mun   ----------------------------------------------------------- 
        self.nav.find_element(By.ID, 'form:municipio').click()
        time.sleep(1)
        self.nav.find_element(By.ID, 'form:municipio').send_keys('P')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:municipio').send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:municipio').send_keys(Keys.ENTER)
        time.sleep(0.5)
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
        time.sleep(1)
    # ---------------------------------------------  Select Final Day  -----------------------------------------------------

        self.nav.find_element(By.ID, 'form:dataFinalInputDate').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('31')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('12')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('2019')
        time.sleep(1)
    # -----------------------------------------------------------------------------------------------------------------------


    # ---------------------------------------------  Select Tipo Gestão  ----------------------------------------------------

        self.nav.find_element(By.ID, 'form:canal').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:canal').send_keys('M')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:canal').send_keys(Keys.ENTER)
            # -----------------------------------------------------------------------------------------------------------------------

            # ---------------------------------------------  Select Pisos Fin  ------------------------------------------------------

        list_pisos_financeiros =['APOIO FINANCEIRO AO BL PSB', 'APOIO FINANCEIRO BLMAC',
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
            time.sleep(0.5)
            self.nav.find_element(By.CLASS_NAME, 'btn').click()
            time.sleep(0.5)
            pag = self.nav.find_element(By.ID, 'content').text
            time.sleep(0.5)
            if 'Nenhum registro encontrado.' in pag:
                print('Não existe arquivo para download')
            else:
                self.nav.find_element(By.XPATH, '//*[@id="form:botoes4"]/span[1]/span/input').click()
        self.nav.quit()
    
    def rodar_bot_2018(self):
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
            # -----------------------------------------------------------------------------------------------------------------------

            # ---------------------------------------------  Select UF    ----------------------------------------------------------- 
        self.nav.find_element(By.ID, 'form:uf').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:uf').send_keys('RJ')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:uf').send_keys(Keys.ENTER)
        time.sleep(0.5)
    # -----------------------------------------------------------------------------------------------------------------------
    
    # ---------------------------------------------  Select Mun   ----------------------------------------------------------- 
        self.nav.find_element(By.ID, 'form:municipio').click()
        time.sleep(1)
        self.nav.find_element(By.ID, 'form:municipio').send_keys('P')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:municipio').send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:municipio').send_keys(Keys.ENTER)
        time.sleep(0.5)
    # -----------------------------------------------------------------------------------------------------------------------

    # ---------------------------------------------  Select data  ----------------------------------------------------------- 
    # ---------------------------------------------  Select Inicial Day  ----------------------------------------------------

        self.nav.find_element(By.ID, 'form:dataInicialInputDate').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('01')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('01')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('2018')
        time.sleep(1)
    # ---------------------------------------------  Select Final Day  -----------------------------------------------------

        self.nav.find_element(By.ID, 'form:dataFinalInputDate').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('31')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('12')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('2018')
        time.sleep(1)
    # -----------------------------------------------------------------------------------------------------------------------


    # ---------------------------------------------  Select Tipo Gestão  ----------------------------------------------------

        self.nav.find_element(By.ID, 'form:canal').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:canal').send_keys('M')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:canal').send_keys(Keys.ENTER)
            # -----------------------------------------------------------------------------------------------------------------------

            # ---------------------------------------------  Select Pisos Fin  ------------------------------------------------------

        list_pisos_financeiros =['APOIO FINANCEIRO AO BL PSB', 'APOIO FINANCEIRO BLMAC',
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
            time.sleep(0.5)
            self.nav.find_element(By.CLASS_NAME, 'btn').click()
            time.sleep(0.5)
            pag = self.nav.find_element(By.ID, 'content').text
            time.sleep(0.5)
            if 'Nenhum registro encontrado.' in pag:
                print('Não existe arquivo para download')
            else:
                self.nav.find_element(By.XPATH, '//*[@id="form:botoes4"]/span[1]/span/input').click()
        self.nav.quit()
    
    def rodar_bot_2017(self):
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
            # -----------------------------------------------------------------------------------------------------------------------

            # ---------------------------------------------  Select UF    ----------------------------------------------------------- 
        self.nav.find_element(By.ID, 'form:uf').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:uf').send_keys('RJ')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:uf').send_keys(Keys.ENTER)
        time.sleep(0.5)
    # -----------------------------------------------------------------------------------------------------------------------
    
    # ---------------------------------------------  Select Mun   ----------------------------------------------------------- 
        self.nav.find_element(By.ID, 'form:municipio').click()
        time.sleep(1)
        self.nav.find_element(By.ID, 'form:municipio').send_keys('P')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:municipio').send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:municipio').send_keys(Keys.ENTER)
        time.sleep(0.5)
    # -----------------------------------------------------------------------------------------------------------------------

    # ---------------------------------------------  Select data  ----------------------------------------------------------- 
    # ---------------------------------------------  Select Inicial Day  ----------------------------------------------------

        self.nav.find_element(By.ID, 'form:dataInicialInputDate').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('01')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('01')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('2017')
        time.sleep(1)
    # ---------------------------------------------  Select Final Day  -----------------------------------------------------

        self.nav.find_element(By.ID, 'form:dataFinalInputDate').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('31')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('12')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('2017')
        time.sleep(1)
    # -----------------------------------------------------------------------------------------------------------------------


    # ---------------------------------------------  Select Tipo Gestão  ----------------------------------------------------

        self.nav.find_element(By.ID, 'form:canal').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:canal').send_keys('M')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:canal').send_keys(Keys.ENTER)
            # -----------------------------------------------------------------------------------------------------------------------

            # ---------------------------------------------  Select Pisos Fin  ------------------------------------------------------

        list_pisos_financeiros =['APOIO FINANCEIRO AO BL PSB', 'APOIO FINANCEIRO BLMAC',
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
            time.sleep(0.5)
            self.nav.find_element(By.CLASS_NAME, 'btn').click()
            time.sleep(0.5)
            pag = self.nav.find_element(By.ID, 'content').text
            time.sleep(0.5)
            if 'Nenhum registro encontrado.' in pag:
                print('Não existe arquivo para download')
            else:
                self.nav.find_element(By.XPATH, '//*[@id="form:botoes4"]/span[1]/span/input').click()
        self.nav.quit()

    def rodar_bot_2016(self):
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
            # -----------------------------------------------------------------------------------------------------------------------

            # ---------------------------------------------  Select UF    ----------------------------------------------------------- 
        self.nav.find_element(By.ID, 'form:uf').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:uf').send_keys('RJ')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:uf').send_keys(Keys.ENTER)
        time.sleep(0.5)
    # -----------------------------------------------------------------------------------------------------------------------
    
    # ---------------------------------------------  Select Mun   ----------------------------------------------------------- 
        self.nav.find_element(By.ID, 'form:municipio').click()
        time.sleep(1)
        self.nav.find_element(By.ID, 'form:municipio').send_keys('P')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:municipio').send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:municipio').send_keys(Keys.ENTER)
        time.sleep(0.5)
    # -----------------------------------------------------------------------------------------------------------------------

    # ---------------------------------------------  Select data  ----------------------------------------------------------- 
    # ---------------------------------------------  Select Inicial Day  ----------------------------------------------------

        self.nav.find_element(By.ID, 'form:dataInicialInputDate').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('01')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('01')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('2016')
        time.sleep(1)
    # ---------------------------------------------  Select Final Day  -----------------------------------------------------

        self.nav.find_element(By.ID, 'form:dataFinalInputDate').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('31')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('12')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('2016')
        time.sleep(1)
    # -----------------------------------------------------------------------------------------------------------------------


    # ---------------------------------------------  Select Tipo Gestão  ----------------------------------------------------

        self.nav.find_element(By.ID, 'form:canal').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:canal').send_keys('M')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:canal').send_keys(Keys.ENTER)
            # -----------------------------------------------------------------------------------------------------------------------

            # ---------------------------------------------  Select Pisos Fin  ------------------------------------------------------

        list_pisos_financeiros =['APOIO FINANCEIRO AO BL PSB', 'APOIO FINANCEIRO BLMAC',
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
            time.sleep(0.5)
            self.nav.find_element(By.CLASS_NAME, 'btn').click()
            time.sleep(0.5)
            pag = self.nav.find_element(By.ID, 'content').text
            time.sleep(0.5)
            if 'Nenhum registro encontrado.' in pag:
                print('Não existe arquivo para download')
            else:
                self.nav.find_element(By.XPATH, '//*[@id="form:botoes4"]/span[1]/span/input').click()
        self.nav.quit()
    
    def rodar_bot_2015(self):
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
            # -----------------------------------------------------------------------------------------------------------------------

            # ---------------------------------------------  Select UF    ----------------------------------------------------------- 
        self.nav.find_element(By.ID, 'form:uf').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:uf').send_keys('RJ')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:uf').send_keys(Keys.ENTER)
        time.sleep(0.5)
    # -----------------------------------------------------------------------------------------------------------------------
    
    # ---------------------------------------------  Select Mun   ----------------------------------------------------------- 
        self.nav.find_element(By.ID, 'form:municipio').click()
        time.sleep(1)
        self.nav.find_element(By.ID, 'form:municipio').send_keys('P')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:municipio').send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:municipio').send_keys(Keys.ENTER)
        time.sleep(0.5)
    # -----------------------------------------------------------------------------------------------------------------------

    # ---------------------------------------------  Select data  ----------------------------------------------------------- 
    # ---------------------------------------------  Select Inicial Day  ----------------------------------------------------

        self.nav.find_element(By.ID, 'form:dataInicialInputDate').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('01')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('01')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('2015')
        time.sleep(1)
    # ---------------------------------------------  Select Final Day  -----------------------------------------------------

        self.nav.find_element(By.ID, 'form:dataFinalInputDate').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('31')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('12')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('2015')
        time.sleep(1)
    # -----------------------------------------------------------------------------------------------------------------------


    # ---------------------------------------------  Select Tipo Gestão  ----------------------------------------------------

        self.nav.find_element(By.ID, 'form:canal').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:canal').send_keys('M')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:canal').send_keys(Keys.ENTER)
            # -----------------------------------------------------------------------------------------------------------------------

            # ---------------------------------------------  Select Pisos Fin  ------------------------------------------------------

        list_pisos_financeiros =['APOIO FINANCEIRO AO BL PSB', 'APOIO FINANCEIRO BLMAC',
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
            time.sleep(0.5)
            self.nav.find_element(By.CLASS_NAME, 'btn').click()
            time.sleep(0.5)
            pag = self.nav.find_element(By.ID, 'content').text
            time.sleep(0.5)
            if 'Nenhum registro encontrado.' in pag:
                print('Não existe arquivo para download')
            else:
                self.nav.find_element(By.XPATH, '//*[@id="form:botoes4"]/span[1]/span/input').click()
        self.nav.quit()
    
    def rodar_bot_2014(self):
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
            # -----------------------------------------------------------------------------------------------------------------------

            # ---------------------------------------------  Select UF    ----------------------------------------------------------- 
        self.nav.find_element(By.ID, 'form:uf').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:uf').send_keys('RJ')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:uf').send_keys(Keys.ENTER)
        time.sleep(0.5)
    # -----------------------------------------------------------------------------------------------------------------------
    
    # ---------------------------------------------  Select Mun   ----------------------------------------------------------- 
        self.nav.find_element(By.ID, 'form:municipio').click()
        time.sleep(1)
        self.nav.find_element(By.ID, 'form:municipio').send_keys('P')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:municipio').send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:municipio').send_keys(Keys.ENTER)
        time.sleep(0.5)
    # -----------------------------------------------------------------------------------------------------------------------

    # ---------------------------------------------  Select data  ----------------------------------------------------------- 
    # ---------------------------------------------  Select Inicial Day  ----------------------------------------------------

        self.nav.find_element(By.ID, 'form:dataInicialInputDate').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('01')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('01')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('2014')
        time.sleep(1)
    # ---------------------------------------------  Select Final Day  -----------------------------------------------------

        self.nav.find_element(By.ID, 'form:dataFinalInputDate').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('31')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('12')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('2014')
        time.sleep(1)
    # -----------------------------------------------------------------------------------------------------------------------


    # ---------------------------------------------  Select Tipo Gestão  ----------------------------------------------------

        self.nav.find_element(By.ID, 'form:canal').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:canal').send_keys('M')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:canal').send_keys(Keys.ENTER)
            # -----------------------------------------------------------------------------------------------------------------------

            # ---------------------------------------------  Select Pisos Fin  ------------------------------------------------------

        list_pisos_financeiros =['APOIO FINANCEIRO AO BL PSB', 'APOIO FINANCEIRO BLMAC',
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
            time.sleep(0.5)
            self.nav.find_element(By.CLASS_NAME, 'btn').click()
            time.sleep(0.5)
            pag = self.nav.find_element(By.ID, 'content').text
            time.sleep(0.5)
            if 'Nenhum registro encontrado.' in pag:
                print('Não existe arquivo para download')
            else:
                self.nav.find_element(By.XPATH, '//*[@id="form:botoes4"]/span[1]/span/input').click()
        self.nav.quit()
    
    def rodar_bot_2013(self):
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
            # -----------------------------------------------------------------------------------------------------------------------

            # ---------------------------------------------  Select UF    ----------------------------------------------------------- 
        self.nav.find_element(By.ID, 'form:uf').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:uf').send_keys('RJ')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:uf').send_keys(Keys.ENTER)
        time.sleep(0.5)
    # -----------------------------------------------------------------------------------------------------------------------
    
    # ---------------------------------------------  Select Mun   ----------------------------------------------------------- 
        self.nav.find_element(By.ID, 'form:municipio').click()
        time.sleep(1)
        self.nav.find_element(By.ID, 'form:municipio').send_keys('P')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:municipio').send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:municipio').send_keys(Keys.ENTER)
        time.sleep(0.5)
    # -----------------------------------------------------------------------------------------------------------------------

    # ---------------------------------------------  Select data  ----------------------------------------------------------- 
    # ---------------------------------------------  Select Inicial Day  ----------------------------------------------------

        self.nav.find_element(By.ID, 'form:dataInicialInputDate').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('01')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('01')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataInicialInputDate').send_keys('2013')
        time.sleep(1)
    # ---------------------------------------------  Select Final Day  -----------------------------------------------------

        self.nav.find_element(By.ID, 'form:dataFinalInputDate').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('31')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('12')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:dataFinalInputDate').send_keys('2013')
        time.sleep(1)
    # -----------------------------------------------------------------------------------------------------------------------


    # ---------------------------------------------  Select Tipo Gestão  ----------------------------------------------------

        self.nav.find_element(By.ID, 'form:canal').click()
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:canal').send_keys('M')
        time.sleep(0.5)
        self.nav.find_element(By.ID, 'form:canal').send_keys(Keys.ENTER)
            # -----------------------------------------------------------------------------------------------------------------------

            # ---------------------------------------------  Select Pisos Fin  ------------------------------------------------------

        list_pisos_financeiros =['APOIO FINANCEIRO AO BL PSB', 'APOIO FINANCEIRO BLMAC',
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
            time.sleep(0.5)
            self.nav.find_element(By.CLASS_NAME, 'btn').click()
            time.sleep(0.5)
            pag = self.nav.find_element(By.ID, 'content').text
            time.sleep(0.5)
            if 'Nenhum registro encontrado.' in pag:
                print('Não existe arquivo para download')
            else:
                self.nav.find_element(By.XPATH, '//*[@id="form:botoes4"]/span[1]/span/input').click()
        self.nav.quit()

bot = Bot()
bot.rodar_bot()