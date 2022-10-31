from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from fake_useragent import UserAgent
import accountInfoGenerator as account
import temporaryEmail as tempEmail
from temporaryEmail import color
import randomFiller as rFiller
import getVerifCode as verifiCode
from selenium import webdriver
import fakeMail as email
import sys , os , random , requests , time , pyperclip
import argparse
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.chrome.options import Options

ua = UserAgent()
userAgent = ua.random
print(userAgent)

options = Options()

#replace 'your path here' with your chrome binary absolute path
driver = webdriver.Chrome(executable_path=CM().install(), options = options)
driver.get("https://www.instagram.com/accounts/emailsignup/")
time.sleep(8)
try:
    cookie = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/button[1]'))).click()
except:
	pass

#generate user credentials
generated_email = tempEmail.getEmail(driver)
fullName = account.generatingName()
print(generated_email)
userName = "ndiniuya151"
acc_password = account.generatePassword()
birth_year = str(random.randint(1990,2003))
birth_month = str(random.randint(1,12))
birth_day = str(random.randint(1,30))



#saves the login & pass into accounts.txt file.
acc = open("accounts.txt", "a")
print(userName+":"+acc_password, file=acc)
acc.close()

time.sleep(random.uniform(1.4783,2.3215))

#Fill the email value
email_field = driver.find_element_by_name('emailOrPhone')
rFiller.fill(email_field, generated_email)
time.sleep(random.uniform(1.568, 2.8952102))

# Fill the fullname value
fullname_field = driver.find_element_by_name('fullName')
rFiller.fill(fullname_field, fullName)
time.sleep(random.uniform(1.568, 3.8952102))

# Fill username value
username_field = driver.find_element_by_name('username')
rFiller.fill(username_field, userName)
time.sleep(random.uniform(1.568, 2.8952102))

# Fill password value
password_field = driver.find_element_by_name('password')

rFiller.fill(password_field, acc_password)
time.sleep(random.uniform(3.568, 7.8952102))
password_field.send_keys(Keys.ENTER)

#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[7]/div/button"))).click()
time.sleep(random.uniform(6.57896, 8.8952102))

birth_month_field = Select(driver.find_element_by_class_name("_aau-"))
birth_month_field.select_by_value(birth_month)
time.sleep(random.uniform(1.57896, 3.895210))

birth_day_field = Select(driver.find_element(By.XPATH, """//*[@title="Day:"]"""))
birth_day_field.select_by_value(birth_day)
time.sleep(random.uniform(1.457896, 2.895210))

birth_year_field = Select(driver.find_element(By.XPATH, """//*[@title="Year:"]"""))
birth_year_field.select_by_value(birth_year)
time.sleep(random.uniform(0.57896, 3.895210))

#birthday_next_button = driver.find_element_by_class_name("_acan _acap _acaq _acas")
birthday_next_button =  driver.find_element(By.XPATH, """//*[@class="_acan _acap _acaq _acas"]""")
birthday_next_button.click()

#get opt
instCode=tempEmail.getOpt(driver)
time.sleep(random.uniform(2.57896, 5.895210))

otpField =driver.find_element(By.XPATH, """//*[@value=""]""")
rFiller.fill(otpField, instCode)
otpField.send_keys(Keys.ENTER)
time.sleep(random.uniform(10.57896, 16.895210))

#accepting the notifications.
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
time.sleep(random.uniform(2.57896, 5.895210))

#logout
driver.find_element_by_xpath(
    "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img").click()
driver.find_element_by_xpath(
    "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div").click()

try:
    not_valid = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[4]/div')
    if(not_valid.text == 'That code isn\'t valid. You can request a new one.'):
      time.sleep(1)
      driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[1]/div[2]/div/button').click()
      time.sleep(10)
      instCodeNew = verifiCode.getInstVeriCodeDouble(mailName, domain, driver, instCode)
      confInput = driver.find_element_by_name('email_confirmation_code')
      confInput.send_keys(Keys.CONTROL + "a")
      confInput.send_keys(Keys.DELETE)
      confInput.send_keys(instCodeNew, Keys.ENTER)
except:
      pass

time.sleep(5)
driver.quit()
