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

if __name__ == "__main__":
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
    sleep(5)
    filepath = getcwd()
    filename = max([filepath + "\\" + f for f in listdir(filepath)], key=path.getctime)
    move(path.join(filepath, filename), "megasena.xlsx")

    df = pd.read_excel("megasena.xlsx")
    df["Resultado"] = list(
        df[["Bola1", "Bola2", "Bola3", "Bola4", "Bola5", "Bola6"]].values
    )
    df = df[["Resultado", "Data do Sorteio"]]

    print(df)
