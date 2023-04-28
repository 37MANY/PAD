from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os

driver = webdriver.Chrome()
driver.get("https://www.pap.pl/")

#Zadanie 1.
#oczekiwanie na pojawienie się przycisku
try:
    cookies_accept = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='ok closeButton']"))
    )
    cookies_accept.click()
    print("Cookies accepted")
except:
    print("Unable to accept cookies.")

#Zadanie 2.
driver.maximize_window()

#Zadanie 3.
try:
    language_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='http://www.pap.pl/en']"))
    )
    language_link.click()
    print("Language changed to English.")
except:
    print("Unable to change language.")

#Zadanie 4
try:
    business_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, ('//a[@href="/en/business"]'))
    ))
    business_link.click()
    print("Navigated to the Business section")
except:
    print("Unable to navigate to the Business section")

#Zadanie 5.
news_titles = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//h2[@class='title']/a"))
)

# Extract the titles and append them to the titles list
titles = []
print("Tytuły artykułów:")
for title in news_titles:
    print(title.text)

#Zadanie 6