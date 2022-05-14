from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import wget


# please put your webdriver path....
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://www.instagram.com")

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# login section.... 
#enter username and password
username.clear()
username.send_keys("your username.....")
password.clear()
password.send_keys("your instagram password.....")

button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(5)
alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
alert2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

searchbox = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()


# searching keyword section..... 

keyword = '#coder'
searchbox.send_keys(keyword)
time.sleep(5)
my_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + keyword[1:] + "/')]")))
my_link.click()
# time.sleep(5)


# scrping section..... 

scroll = 1
for j in range(0,scroll):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

main_tag = driver.find_elements_by_tag_name('a')
main_tag = [a.get_attribute('href') for a in main_tag]
# print(main_tag)
main_tag = [a for a in main_tag if str(a).startswith("https://www.instagram.com/p/")]




img_hash = []

for x in main_tag:
    driver.get(x)
    time.sleep(5)
    img = driver.find_elements_by_tag_name('img')
    img = [i.get_attribute('src') for i in img]
    img_hash.append(img[1])


path = os.getcwd()
path = os.path.join(path, keyword[1:])

# download section start...      
#create the directory
os.mkdir(path)
print(path)

count =0
for zz in img_hash:
    save = os.path.join(path,keyword[1:] + str(count)+'.jpg')
    wget.download(zz,save)
    count+=1

print('mission complate')

driver.quit()