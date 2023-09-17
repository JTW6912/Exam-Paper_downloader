from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


wd = webdriver.Chrome()
url = 'https://www.exam-mate.com/pastpapers?cat=3&sub=244'

wd.get(url)
with open('cookies.txt', 'r') as f:
    cookies = eval(f.read())

for cookie in cookies: wd.add_cookie(cookie)

wait = WebDriverWait(wd,10)
Paper = wait.until(EC.element_to_be_clickable(By.XPATH('/html/body/div/div[5]/div[2]/div[2]/div[1]/div/div[2]/div[1]/ul/li[1]')))

input()