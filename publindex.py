import time, os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

options = Options()
options.binary_location = "/usr/bin/brave-browser"
options.headless = True
options.add_argument("window-size=1920,1080")
options.add_argument('user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"')

service = Service(executable_path=chromedriver)

driver = webdriver.Chrome(options = options, service = service)

url = "https://scienti.minciencias.gov.co/publindex/#/revistasPublindex/buscador"
journal = "2248-762X"
year = 2012
driver.get(url)
time.sleep(2)

plus = driver.find_element(By.XPATH, '/html/body/app-root/ng-component/div/div[3]/div/div/div/div[2]/ng-component/form/div/div[6]/button[1]')
plus.click()

search_select = driver.find_element(By.XPATH, '/html/body/app-root/ng-component/div/div[3]/div/div/div/div[2]/ng-component/form/div/div[7]/div/div[1]/p-dropdown')
search_select.click()

issn_select = driver.find_element(By.XPATH, '/html/body/app-root/ng-component/div/div[3]/div/div/div/div[2]/ng-component/form/div/div[7]/div/div[1]/p-dropdown/div/div[4]/div/ul/p-dropdownitem[2]/li')
issn_select.click()

search_box = driver.find_element(By.XPATH, '/html/body/app-root/ng-component/div/div[3]/div/div/div/div[2]/ng-component/form/div/div[7]/div/div[2]/input')
search_box.send_keys(journal)
time.sleep(1)

search_btn = driver.find_element(By.XPATH, '/html/body/app-root/ng-component/div/div[3]/div/div/div/div[2]/ng-component/form/div/div[8]/button[1]')
search_btn.click()
time.sleep(3)

try:
    details_btn = driver.find_element(By.XPATH, '/html/body/app-root/ng-component/div/div[3]/div/div/div/div[2]/ng-component/form/div/div[9]/p-table/div/div/table/tbody/tr/td[4]/button')                                                 
    details_btn.click()
    time.sleep(1)

    history_tab = driver.find_element(By.XPATH, '/html/body/app-root/ng-component/div/div[3]/div/div/div/div[2]/ng-component/div/div[2]/p-tabview/div/ul/li[2]')
    history_tab.click()

    year_box = driver.find_element(By.XPATH, '/html/body/app-root/ng-component/div/div[3]/div/div/div/div[2]/ng-component/div/div[2]/p-tabview/div/div/p-tabpanel[2]/div/p-table/div/div/table/thead/tr[2]/th[1]/input')
    year_box.send_keys(year)
    time.sleep(1)

    try:
        classification = driver.find_element(By.XPATH, '/html/body/app-root/ng-component/div/div[3]/div/div/div/div[2]/ng-component/div/div[2]/p-tabview/div/div/p-tabpanel[2]/div/p-table/div/div/table/tbody/tr[1]/td[2]')
        print(classification.text)
    except Exception as e:
        print('Año no encontrado')

except Exception as e:
    print('Revista no encontrada')

driver.close()

