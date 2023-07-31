# selenium
# https://sites.google.com/chromium.org/driver/?pli=1
#Version 113.0.5672.127 (Official Build) (64-bit)

'''Basic example of using Selenium WebDriver with the Chrome browser driver (chromedriver.exe). This script automates the process of signing in to a Google account using a provided email address.'''

'''Also, keep in mind that automating sign-in processes may be subject to the terms and conditions of the target website.'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime


def check():
    PATH = "C:\Program Files (x86)\chromedriver.exe"#path you need to remember
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    #we create an instance of the webdriver and initialize the chrome browser
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument(f'user-agent={user_agent}')
    #driver = webdriver.Chrome()
    driver = webdriver.Chrome(options=options)

    
    try:
        file = open(".\prices.txt","r")
        content = file.readlines()
        if content==[]:
            i=0
        else:
            for j in content:
                pass
            temp = j.split('|')
            i=int(temp[0])
            i+=1
    except:
        file = open(".\prices.txt","w")
        file.close()
        i=0

    driver.get("https://www.makemytrip.com/flight/search?itinerary=JAI-BLR-27/08/2023&tripType=O&paxType=A-1_C-0_I-0&intl=false&cabinClass=E&ccde=IN&lang=eng&pft=AF")#by using'get()' method on the 'driver' object we open the google sign-in page

    #driver.implicitly_wait(10)
    time.sleep(20)
    try:
        #code to take screenshot of certain element --> element.screenshot('path')
        driver.get_screenshot_as_file(".\static\screenshot.png")
        driver.find_element('xpath','//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div/div[3]/button').click()
        driver.get_screenshot_as_file(".\static\screenshot.png")
    except:
        pass

    now = datetime.now()
    mainel = driver.find_element('xpath','//*[@id="listing-id"]/div/div[2]/div[1]/div[1]/div[1]')
    driver.get_screenshot_as_file(".\static\screenshot.png")
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    dep_time = driver.find_element('xpath','//*[@id="listing-id"]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label/div/div/div/div[1]/p[1]/span').text
    arr_time = driver.find_element('xpath','//*[@id="listing-id"]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/label/div/div/div/div[3]/p[1]/span').text
    if (dep_time=='12:55' and arr_time=='19:30'):
        price = '₹ ' + driver.find_element('xpath','//*[@id="listing-id"]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/div').text[9:14]
        file = open(".\prices.txt","a+", encoding="utf-8")
        input = str(i)+"|"+dt_string[:10]+"|"+dt_string[11:]+"|"+price+"\n"
        file.write(input)
        print("Updated")
        file.close()
    else:
        print("No Flight Found")
    driver.close()#closing the driver

#-----------------------------------------------------------
