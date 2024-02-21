import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get("https://addyconceptstore.com/account/register#RegisterForm-email")

# Répondre Email
text_area = driver.find_element(By.XPATH, '//*[@id="RegisterForm-email"]')
text_area.clear()
random_number = random.randint(10000000, 99999999)
text_area.send_keys(str(random_number)+"@exemple.exemple")

# Répondre Prénom
text_area = driver.find_element(By.XPATH, '//*[@id="RegisterForm-FirstName"]')
text_area.clear()
text_area.send_keys("sorry")

# Répondre Nom
text_area = driver.find_element(By.XPATH, '//*[@id="RegisterForm-LastName"]')
text_area.clear()
text_area.send_keys("im just ken")

# Répondre Mot de passe
text_area = driver.find_element(By.XPATH, '//*[@id="RegisterForm-password"]')
text_area.clear()
text_area.send_keys("menfou123!")

time.sleep(1)

driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/button[3]').click()
driver.find_element(By.XPATH, '//*[@id="RegisterForm"]/p/input').click()

time.sleep(1)

try:
    element = driver.find_element(By.XPATH, '//*[@id="RegisterForm-email-error"]/span[2]')
    print(element.text)
except NoSuchElementException:
    print("Connexion valided !")

driver.find_element(By.XPATH, '//*[@id="SiteNav"]/li[2]/button/span').click()
driver.find_element(By.XPATH, '//*[@id="SiteNavLabel-bijoux"]/ul/li[1]/a/span').click()
driver.find_element(By.XPATH, '//*[@id="Collection"]/ul[1]/li[2]/div/a').click()

time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="product_form_8595236716882"]/div[2]/div/div/div/div/div/button[1]').click()

time.sleep(1)

# Répondre Email
text_area = driver.find_element(By.XPATH, '//*[@id="email"]')
text_area.clear()
random_number = random.randint(10000000, 99999999)
text_area.send_keys(str(random_number)+"@exemple.exemple")

# Répondre Prénom
text_area = driver.find_element(By.XPATH, '//*[@id="TextField0"]')
text_area.clear()
text_area.send_keys("sorry")

# Répondre Nom
text_area = driver.find_element(By.XPATH, '//*[@id="TextField1"]')
text_area.clear()
text_area.send_keys("im just ken")

time.sleep(1)

text_area = driver.find_element(By.XPATH, '//*[@id="shipping-address1"]')
text_area.clear()
text_area.send_keys("8 Rue des Poireaux")

text_area = driver.find_element(By.XPATH, '//*[@id="TextField2"]')
text_area.clear()
text_area.send_keys("07000")

text_area = driver.find_element(By.XPATH, '//*[@id="TextField3"]')
text_area.clear()
text_area.send_keys("Privas")

text_area = driver.find_element(By.XPATH, '//*[@id="TextField4"]')
text_area.clear()
text_area.send_keys("0836656565")

time.sleep(3)

text_area = driver.find_element(By.XPATH, '//*[@id="number"]')
text_area.send_keys("3566000020000410")
time.sleep(0.1)

text_area = driver.find_element(By.XPATH, '//*[@id="expiry"]')
text_area.send_keys("02/2026")
time.sleep(0.1)

text_area = driver.find_element(By.XPATH, '//*[@id="verification_value"]')
text_area.send_keys("123")

time.sleep(100)

driver.find_element(By.XPATH, '//*[@id="pay-button-container"]/div/div/button').click()

time.sleep(10)


