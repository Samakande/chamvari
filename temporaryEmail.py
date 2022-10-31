
import pyperclip, time, sys
from selenium.webdriver.common.by import By
import random

#color
class color:
   PURPLE = '\033[95m'
   GREEN = '\033[92m'
   BOLD = '\033[1m'
   CWHITE  = '\33[37m'

def getEmail(driver):

    # Create temporary email
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    try:
        driver.get("https://mail.tm")
    except:
        pass
    time.sleep(random.uniform(6.157863, 10.578612))
    driver.execute_script("window.stop();")
    copy_button = driver.find_element(By.XPATH, """//*[@id="DontUseWEBuseAPI"]""")
    copy_button.click()
    generated_email = pyperclip.paste()
    driver.switch_to.window(driver.window_handles[0])

    return generated_email

def getOpt(driver):
    #get opt
    driver.switch_to.window(driver.window_handles[1])
    print()
    print(color.GREEN + "[!] " + color.CWHITE + "Waiting for otp ")

    print(color.GREEN + "[!] " + color.CWHITE + "Opening mail box in 15 seconds")

    for remaining in range(15, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write("\rComplete!            \n")
    try:
        driver.refresh()
    except:
        pass
    time.sleep(2)

    read_otp = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/main/div/div[2]/ul/li/a/div/div[1]/div[2]/div[2]/div/div[1]').text

    # Read otp from mail

    # Save response to response.Text

    with open("response.text","w") as file:
        file.write(str(read_otp))

    read_otp_file = open("response.text")

    lines = read_otp_file.readlines()

    for line in lines:
     my_otp = str(line[0:6])

    print(color.GREEN + "[!] " + color.CWHITE + "OTP Recieved : " + my_otp)
    driver.switch_to.window(driver.window_handles[0])
    return my_otp

