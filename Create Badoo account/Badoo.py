import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
random_number = random.randint(10000000, 99999999)

Name = "Marty"
Birth = "15062002"
Email = str(random_number)+"@gmail.com"
Password = "supersecret667^^"
AreYouAMale = True
AreYouCute = True


if AreYouCute:
    options = Options()
    options.add_argument("--use-fake-ui-for-media-stream")
    prefs = {
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.media_stream_mic": 1,
    }

    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
else:
    options = Options()
    options.add_argument("--use-fake-ui-for-media-stream")
    options.add_argument("--use-fake-device-for-media-stream")
    video_file_path = "E:/COURS/4CITE/01-BackendTesting/Exemple/Exercice05/images/video.mp4"
    options.add_argument(f"--use-file-for-fake-video-capture={video_file_path}")

    prefs = {
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.media_stream_mic": 1,
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# driver = webdriver.Chrome()

# Extension part
# driver.get("https://chromewebstore.google.com/detail/rumola-bypass-captcha/bjjgbdlbgjeoankjijbmheneoekbghcg")
# driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/main/div/section[1]/section/div[2]/div/button/span[6]').click()
# time.sleep(1)
# actions = ActionChains(driver)
# actions.send_keys(Keys.ARROW_LEFT).send_keys(Keys.ENTER).perform()

# time.sleep(2)

# time.sleep(2)

driver.get("https://badoo.com/")

time.sleep(1000)

# Remove dirty cookie
try:
    iframe = driver.find_element(By.XPATH, '//*[@id="sp_message_iframe_1006183"]')
    driver.switch_to.frame(iframe)
    cookie_button = driver.find_element(By.XPATH, '//*[@id="notice"]/div[2]/div[3]/div[3]/button[2]')
    cookie_button.click()
    driver.switch_to.default_content()
except NoSuchElementException:
    print("Cookie not found.")

# Create new account
text_area = driver.find_element(By.XPATH, '//*[@id="signin-name"]')
text_area.clear()
text_area.send_keys(Email)
driver.find_element(By.XPATH, '//*[@id="hero"]/div/div/div[1]/div[1]/form/div[1]/div[2]/button').click()

# Remove by yourself the capchat
try:
    time.sleep(20)
    # driver.find_element(By.XPATH, '//*[@id="hero"]/div/div/div[1]/div[1]/form/div[1]/div[2]/button').click()
    # driver.find_element(By.XPATH, '//*[@id="hero"]/div/div/div[1]/div[1]/form/div[1]/div[2]/button').click()
except NoSuchElementException:
    print("No capchat lucky boy.")

driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div[4]/div/div/div/div/div[2]/div/div[3]/div/div/button').click()


time.sleep(1)

# Choose gender, default = male
if AreYouAMale:
    driver.find_element(By.XPATH, '//*[@id="page-container"]/div/div/div[2]/div[2]/form/div/div[2]/fieldset/div[2]/div[2]/label/span[2]/span/input').click()
else:
    driver.find_element(By.XPATH, '//*[@id="gender-female"]').click()
    

# Choose name
text_area = driver.find_element(By.XPATH, '//*[@id="signup-name"]')
text_area.clear()
text_area.send_keys(Name)

# Choose birth
text_area = driver.find_element(By.XPATH, '//*[@id="signup-dob"]')
text_area.clear()
text_area.send_keys(Birth)

# Validate
driver.find_element(By.XPATH, '//*[@id="page-container"]/div/div/div[2]/div[3]/button').click()

time.sleep(1)

# Add photo
driver.find_element(By.XPATH, '//*[@id="page-container"]/div/div/div[4]/div/div/button').click()
driver.find_element(By.XPATH, '//*[@id="page-container"]/div/div/div[3]/div[1]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="page-container"]/div/div/div[2]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="page-container"]/div/div/div[3]/div/div[2]/div/button').click()
driver.find_element(By.XPATH, '//*[@id="page-container"]/div/div/div[3]/div[1]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="page-container"]/div/div/div[2]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="page-container"]/div/div/div[3]/div/div[3]/div/button').click()
driver.find_element(By.XPATH, '//*[@id="page-container"]/div/div/div[3]/div[1]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="page-container"]/div/div/div[2]/button').click()
time.sleep(5)

# Validate
driver.find_element(By.XPATH, '//*[@id="page-container"]/div/div/div[4]/div/div/button').click()

time.sleep(1)

# Add password, default = supersecret667^^
text_area = driver.find_element(By.XPATH, '//*[@id="new-password"]')
text_area.clear()
text_area.send_keys(Password)
time.sleep(1)

# Validate
driver.find_element(By.XPATH, '//*[@id="page-container"]/div/div/div[3]/div/div/button').click()

time.sleep(1000)







