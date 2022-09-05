#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

import warnings
warnings.filterwarnings('ignore')


# In[ ]:


#driver configuration
opciones=Options()

opciones.add_experimental_option('excludeSwitches', ['enable-automation'])
opciones.add_experimental_option('useAutomationExtension', False)
opciones.headless=False    # si True, no aperece la ventana (headless=no visible)
opciones.add_argument('--start-maximized')         # comienza maximizado
#opciones.add_argument('user-data-dir=selenium')    # mantiene las cookies
#opciones.add_extension('driver_folder/adblock.crx')       # adblocker
opciones.add_argument('--incognito')


# In[ ]:


PATH=ChromeDriverManager().install()

driver = webdriver.Chrome(PATH,options = opciones)


# In[ ]:


url = 'https://www.vivino.com/explore?e=eJzLLbI11jNTy83MszVQy02ssDU1MFBLrrR1DVZLtnUNDVIrsDVUS0-zLUssykwtScxRyy9KsU0sTlbLT6q0LSjKTE5VKy-JjgUqAlNGEMoYQplAKHOonAnQ4GIgI7UYALibJko%3D'


# In[ ]:


driver.get(url)


# In[ ]:


time.sleep(4)


# In[ ]:


#cookies banner selection
btn_cookie = driver.find_element(By.XPATH, '//*[@id="cookie-notice-container"]/div/button')


# In[ ]:


#cookie banner click
btn_cookie.click()


# In[ ]:


time.sleep(3)


# In[ ]:


def obtain_links():
        try:
            #info of websites with links (keeps growing when scrolling down)
            web = driver.find_element(By.CSS_SELECTOR, '#explore-page-app > div > div > div.explorerPage__columns--1TTaK > div.explorerPage__results--3wqLw > div:nth-child(1)')
            #all the links
            links_web = [i.get_attribute('href') for i in web.find_elements(By.TAG_NAME, "a") if i.get_attribute('href') and "users" not in i.get_attribute('href')]
        except:
            pass
        return links_web


# In[ ]:


iters = 0
i = 0
start = 0
while 1:
    
    height = int(driver.execute_script("return document.documentElement.scrollHeight"))
    driver.execute_script(f'window.scrollTo({start}, {height});')
    time.sleep(10)
    i += 1
    start = height
    if i == 50:
        total_links = obtain_links()
        iters += 1
        i = 0
    
    if iters == 20:
        break


# In[ ]:


len(total_links)


# In[ ]:


textfile = open("wine_links.txt", "w")
for element in total_links:
    textfile.write(element + "\n")
textfile.close()


# In[ ]:


#it stops scrolling after 1200 wines. I have to chech the code or tackle other parameters to add new data.

