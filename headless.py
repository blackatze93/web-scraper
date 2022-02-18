import time
import os
from selenium.webdriver.common.keys import Keys
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import json

enlace = "https://www.dropbox.com/sh/qe9h0jdh7fgz006/AADWQ5v8_4YRIF61uAbu75oua?dl=0&lst=&preview=horarios_20211_Facultad_Artes.pdf"
chrome_options=Options()
conf_cliente = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], "download.default_directory": os.getcwd()}
chrome_options.add_experimental_option("prefs", conf_cliente)
chrome_options.headless = True
chrome_options.add_argument("window-size=1920,1080")
chrome_options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"')
navegador = webdriver.Chrome(r'./chromedriver', options=chrome_options)
navegador.get(enlace)
time.sleep(3)
item = navegador.find_element_by_class_name('viewer-container')
