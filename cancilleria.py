import time, os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

chromedriver = "./chromedriver_102"
os.environ["webdriver.chrome.driver"] = chromedriver

options = Options()
options.binary_location = "/usr/bin/brave-browser"

options.headless = True
options.add_argument("window-size=1920,1080")
# options.add_argument('--headless')
# options.add_argument('user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"')

service = Service(executable_path=chromedriver)

driver = webdriver.Chrome(options=options, service=service)

url = "https://tramitesmre.cancilleria.gov.co/tramites/enlinea/agendamiento.xhtml"
driver.get(url)
time.sleep(1)

solicitar_btn = driver.find_element(By.XPATH, '/html/body/div[4]/form/div[2]/div/button[1]')
solicitar_btn.click()
time.sleep(1)

# OFICINA CALLE 100
select_oficina = Select(
    driver.find_element(By.XPATH, '/html/body/div[4]/form/div[1]/div/div/table/tbody/tr/td[1]/div/div[2]/select'))
select_oficina.select_by_value('26')
time.sleep(1)

select_tramite = Select(
    driver.find_element(By.XPATH, '/html/body/div[4]/form/div[1]/div/div/table/tbody/tr/td[2]/div/div[2]/select'))
select_tramite.select_by_value('5')
time.sleep(1)

select_servicio = Select(
    driver.find_element(By.XPATH, '/html/body/div[4]/form/div[1]/div/div/table/tbody/tr/td[3]/div/div[2]/select'))
select_servicio.select_by_value('SOLICITAR')
time.sleep(1)

error_msg = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div/ul/li/span')
print("OFICINA CALLE 100: " + error_msg.text)
time.sleep(1)

# OFICINA CALLE 53
select_oficina = Select(
    driver.find_element(By.XPATH, '/html/body/div[4]/form/div[1]/div/div/table/tbody/tr/td[1]/div/div[2]/select'))
select_oficina.select_by_value('27')
time.sleep(1)

select_tramite = Select(
    driver.find_element(By.XPATH, '/html/body/div[4]/form/div[1]/div/div/table/tbody/tr/td[2]/div/div[2]/select'))
select_tramite.select_by_value('5')
time.sleep(1)

select_servicio = Select(
    driver.find_element(By.XPATH, '/html/body/div[4]/form/div[1]/div/div/table/tbody/tr/td[3]/div/div[2]/select'))
select_servicio.select_by_value('SOLICITAR')
time.sleep(1)

error_msg = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div/ul/li/span')
print("OFICINA CALLE 53: " + error_msg.text)
time.sleep(1)

# OFICINA CENTRO
select_oficina = Select(
    driver.find_element(By.XPATH, '/html/body/div[4]/form/div[1]/div/div/table/tbody/tr/td[1]/div/div[2]/select'))
select_oficina.select_by_value('37')
time.sleep(1)

select_tramite = Select(
    driver.find_element(By.XPATH, '/html/body/div[4]/form/div[1]/div/div/table/tbody/tr/td[2]/div/div[2]/select'))
select_tramite.select_by_value('5')
time.sleep(1)

select_servicio = Select(
    driver.find_element(By.XPATH, '/html/body/div[4]/form/div[1]/div/div/table/tbody/tr/td[3]/div/div[2]/select'))
select_servicio.select_by_value('SOLICITAR')
time.sleep(1)

error_msg = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div/ul/li/span')
print("OFICINA CENTRO: " + error_msg.text)
time.sleep(1)

driver.close()
