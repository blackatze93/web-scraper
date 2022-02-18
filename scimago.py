import time, os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

options = Options()
options.binary_location = "/usr/bin/brave-browser"

#options.headless = True
options.add_argument("window-size=1920,1080")
options.add_argument('user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"')

service = Service(executable_path=chromedriver)

driver = webdriver.Chrome(options = options, service = service)

url = "https://www.scimagojr.com/journalsearch.php?q="
journal = "2076-3417"
year = 2020
driver.get(url + journal)
time.sleep(1)

cookies_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]')
cookies_btn.click()

try:
    results = driver.find_element(By.CLASS_NAME, 'search_results')
    results.click()
    time.sleep(2)

    table = driver.find_element(By.TAG_NAME, 'table')
    table_rows = table.find_elements(By.TAG_NAME, 'tr')
    del table_rows[0]
    quartile = "Año no encontrado"

    for i in range(len(table_rows)):
        row = table_rows[i].find_elements(By.TAG_NAME, 'td')
        if (row[1].text == str(year)):
            quartile = row[2].text
            break
    print(quartile)

except Exception as e:
    print('Revista no encontrada')

# driver.close()
