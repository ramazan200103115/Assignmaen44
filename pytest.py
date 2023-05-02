from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

driver: WebDriver = webdriver.Chrome()
driver.get('https://gate2home.com/English-Keyboard')
time.sleep(2)

maga = driver.find_element(By.TAG_NAME, 'input')
time.sleep(2)

Caps=driver.find_element(By.ID, 'kb_bcaps').click()
A = driver.find_element(By.ID, 'kb_b26').click()
Caps2=driver.find_element(By.ID, 'kb_bcaps').click()
U = driver.find_element(By.ID, 'kb_b20').click()
T = driver.find_element(By.ID, 'kb_b18').click()
O = driver.find_element(By.ID, 'kb_b22').click()
M = driver.find_element(By.ID, 'kb_b43').click()
A2 = driver.find_element(By.ID, 'kb_b26').click()
T2 = driver.find_element(By.ID, 'kb_b18').click()
I = driver.find_element(By.ID, 'kb_b21').click()
O2 = driver.find_element(By.ID, 'kb_b22').click()
N = driver.find_element(By.ID, 'kb_b42').click()

space = driver.find_element(By.ID, 'kb_bspace').click()

I2 = driver.find_element(By.ID, 'kb_b21').click()
N2 = driver.find_element(By.ID, 'kb_b42').click()

space2 = driver.find_element(By.ID, 'kb_bspace').click()

T3 = driver.find_element(By.ID, 'kb_b18').click()
E = driver.find_element(By.ID, 'kb_b16').click()
S = driver.find_element(By.ID, 'kb_b27').click()
T4 = driver.find_element(By.ID, 'kb_b18').click()
I3 = driver.find_element(By.ID, 'kb_b21').click()
N3 = driver.find_element(By.ID, 'kb_b42').click()
G = driver.find_element(By.ID, 'kb_b30').click()
result = driver.find_element(By.ID, 'textbox1_freetext')
time.sleep(5)

actions = ActionChains(driver)
actions.click(A)
actions.click(U)
actions.click(T)
actions.click(O)
actions.click(M)
actions.click(A)
actions.click(T)
actions.click(I)
actions.click(O)
actions.click(N)
actions.click(space)
actions.click(I)
actions.click(N)
actions.click(space)
actions.click(T)
actions.click(E)
actions.click(S)
actions.click(T)
actions.click(I)
actions.click(N)
actions.click(G)
actions.click(result)

result_txt = result.text
print("The result is", result)
driver.implicitly_wait(5)
