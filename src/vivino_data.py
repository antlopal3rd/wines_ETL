#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#upload the data to python


# In[ ]:


raw_list = open("linksv1.txt", "r")


# In[ ]:


data = raw_list.read()


# In[ ]:


data_into_list = data.replace('\n', ' ').split(" ")


# In[ ]:


data_into_list


# In[ ]:


raw_list.close()


# In[ ]:


from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time


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


complete_data = []


# In[ ]:


def data_from_links(url):
    try:
        # start driver 
        driver=webdriver.Chrome(PATH)
        driver.get(url)

        time.sleep(4)
    
        #cookies banner selection
        btn_cookie = driver.find_element(By.XPATH, '//*[@id="cookie-notice-container"]/div/button')
        #cookie banner click
        btn_cookie.click()
    
        time.sleep(4)
    
        #first data
        top_web = driver.find_element(By.XPATH, '/html/body/div[2]/div[5]/div/div/div[2]')
        wine = [i.text for i in top_web.find_elements(By.TAG_NAME, "a")]
        #second data
        mid_web = driver.find_element(By.XPATH, '/html/body/div[2]/div[5]/div/div/div[4]')
        #save data to variables
        bodega = wine[0]
        nombre = wine[1]
        pais = wine[2]
        zona = wine[3]
        tipo = wine[5]
        uva= wine[6]
        valoracion = wine[7].split("\n")[0]
        num_valoraciones = wine[7].split("\n")[1].split(" ")[0]
        año = url.split("?")[1].split("&")[0][-4:]
        precio = mid_web.text.split("\n")[0][1:]
        #save data to a dictionary and export
        complete_data = []
        complete_data.append({
    
        'winery': bodega,
        'wine': nombre,
        'year': año,
        'rating': valoracion,
        'num_review': num_valoraciones,
        'country': pais,
        'region': zona,
        'price': precio,
        'type': tipo,
        'body': None,
        'acidity': None    
    
        })   
    
        return complete_data
    except:
        pass


# In[ ]:


from joblib import Parallel, delayed

import pandas as pd


# In[ ]:


from tqdm.notebook import tqdm 


# In[ ]:


get_ipython().run_cell_magic('time', '', 'data = []\n\ndata = [Parallel(n_jobs=6, verbose=True)(delayed(data_from_links)(url) for url in tqdm(data_into_list))]')


# In[ ]:


#data was 1276 in length with one null value. after eliminating that one I iterated over them to leave a list of dictionaries


# In[ ]:


lst3 = []
for i in range(len(lst2)):
    print(type(lst2[i][0]))
    lst3.append(lst2[i][0])   


# In[ ]:


data_dataframe = pd.DataFrame(lst3)


# In[ ]:


#data_dataframe.to_csv(r'/scraped_data_header.csv',index=False, header=True) set your own path

