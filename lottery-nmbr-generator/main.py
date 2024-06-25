#!/usr/bin/env python

from collections import Counter
from itertools import chain
from os import getcwd, listdir, path
from shutil import move
from time import sleep

import chromedriver_autoinstaller
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

"""
Gera um jogo de loteria de 06 números com base no histórico de resultados da 'Mega-Sena'.

Realiza o web-scraping do arquivo de histórico de resultados da 'Mega-Sena', baixando-o para
a pasta raiz de onde está sendo executado o script;
Renomeia o arquivo resultante e o lê para um dataframe com pd.read_excel;
Transforma os resultados aglomerados em uma lista e utiliza Counter e chain para encontrar
os números mais recorrentes.

TODO:
* IMPLEMENTAR MAIS OPÇÕES DE FILTRAGEM DE PROVÁVEIS DEZENAS
* IMPLEMENTAR INTERFACE PYQT6 DE SELEÇÃO DE MÉTODO DE FILTRAGEM E DISPLAY DE RESULTADO
* IMPLEMENTAR SELEÇÃO DE QTDE. DE DEZENAS (PADRÃO 06)
"""

__author__ = "Victor Monteiro Ribeiro"
__version__ = "0.1"
__maintainer__ = "Victor Monteiro Ribeiro"
__email__ = "victormribeiro.py@gmail.com"
__status__ = "Development"

if __name__ == "__main__":
    # CONFIGURANDO DRIVER DO CHROME PARA SELENIUM
    chromedriver_autoinstaller.install()

    service = Service()
    chrome_options = Options()
    prefs = {
        "download.default_directory": getcwd(),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = WebDriverWait(driver, 20)
    driver.get("https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx")

    driver.find_element(
        by=By.XPATH,
        value="//body/form[@id='aspnetForm']/div[@id='s4-workspace']/div[@id='s4-bodyContainer']/div[@id='ContainerSite']/span[@id='DeltaPlaceHolderMain']/div[5]/div[1]/div[1]/div[1]/div[1]/div[8]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]",
    ).click()
    sleep(3)

    # RENOMEANDO ARQUIVO BAIXADO PARA O PADRÃO 'MEGASENA.XLSX'
    filepath = getcwd()
    filename = max([filepath + "\\" + f for f in listdir(filepath)], key=path.getctime)
    move(path.join(filepath, filename), "megasena.xlsx")

    # CARREGANDO PARA DATAFRAME COM PANDAS
    df = pd.read_excel("megasena.xlsx")
    df["Resultado"] = list(
        df[["Bola1", "Bola2", "Bola3", "Bola4", "Bola5", "Bola6"]].values
    )
    df = df[
        [
            "Bola1",
            "Bola2",
            "Bola3",
            "Bola4",
            "Bola5",
            "Bola6",
            "Resultado",
            "Data do Sorteio",
        ]
    ]

    # PASSANDO RESULTADOS PARA LISTA E CONTANDO AS DEZENAS MAIS RECORRENTES
    lista_resultados = df["Resultado"].to_list()
    aparicoes_numeros = Counter(chain.from_iterable(lista_resultados))
    top6 = [int(tpl[0]) for tpl in aparicoes_numeros.most_common(6)]
