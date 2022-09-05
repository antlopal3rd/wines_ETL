#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time


# In[2]:


#driver configuration
opciones=Options()

opciones.add_experimental_option('excludeSwitches', ['enable-automation'])
opciones.add_experimental_option('useAutomationExtension', False)
opciones.headless=False    # si True, no aperece la ventana (headless=no visible)
opciones.add_argument('--start-maximized')         # comienza maximizado
#opciones.add_argument('user-data-dir=selenium')    # mantiene las cookies
#opciones.add_extension('driver_folder/adblock.crx')       # adblocker
opciones.add_argument('--incognito')


# In[3]:


PATH=ChromeDriverManager().install()

driver = webdriver.Chrome(PATH,options = opciones)


# In[4]:


url = 'https://www.decantalo.com/es/es/vino/q/puntuacion_parker/pais_espana/?page=1'


# In[5]:


urls = []
for i in range(1,41):
    urls.append(f'https://www.decantalo.com/es/es/vino/q/puntuacion_parker/pais_espana/?page={i}')    


# In[6]:


def scrap_pages_multiple(url):
    
    try:

        #start driver 
        driver=webdriver.Chrome(PATH)
        driver.get(url)

        time.sleep(4)
        
        #cookie btn
        cookie_btn = driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
        cookie_btn.click()
        
        time.sleep(2)

        #recomended btn
        recomen_btn = driver.find_element(By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')
        recomen_btn.click()
        
        time.sleep(1)
        
        #zoom out to see more
        driver.execute_script("document.body.style.zoom='25%'")
        
        time.sleep(8)
        
        #select the part of the website with the info I want
        web = driver.find_elements(By.CLASS_NAME, 'products')[0]
        #empty list for each website link
        wines = []
        #for parker score different formulas
        cont = 0
        parker_score_list = []
        for word in web.text.split("\n"):
            if word == 'Parker':
                parker_score_list.append(web.text.split("\n")[cont-1])
            cont += 1
        #for prices
        cont = 0
        price_list = []
        for word in web.text.split("\n"):
            if word == 'IVA incl.':
                price_list.append(web.text.split("\n")[cont-1])
            cont += 1
        #iterate for each wine
        for i in range(len([i.text for i in web.find_elements(By.TAG_NAME, 'h3')])):
                
            name = web.find_elements(By.TAG_NAME, 'h3')[i].text[:-5]
        
            year = web.find_elements(By.TAG_NAME, 'h3')[i].text[-4:]
        
            region = web.find_elements(By.CLASS_NAME, 'name_do')[i].text
        
            parker_score = parker_score_list[i]
            
            price = price_list[i]
        
            wine = {
            
                'wine': name,
                'year': year,
                'price': price,
                'parker_score': parker_score,
                'region': region
                 
            }
        
            wines.append(wine)
    
        return wines
    
    except:
        pass      


# In[7]:


from joblib import Parallel, delayed

import pandas as pd

from tqdm.notebook import tqdm 


# In[8]:


get_ipython().run_cell_magic('time', '', 'data = []\n\ndata = [Parallel(n_jobs=6, verbose=True)(delayed(scrap_pages_multiple)(url) for url in tqdm(urls))]')


# In[9]:


data


# In[24]:


len(data[0])


# In[25]:


final_data = [i[0] for i in data[0]]


# In[26]:


data_dataframe = pd.DataFrame(final_data)


# In[31]:


data_dataframe.head(40)


# In[14]:


data_dataframe.loc[11,"wine"] = "Manzanilla Papirusa" #wrong name and wine with no year


# In[15]:


data_dataframe.loc[11,"year"] = None


# In[16]:


data_dataframe.loc[16,"year"] = 2010 #wrong data


# In[17]:


data_dataframe.loc[16,"parker_score"] = 90


# In[18]:


data_dataframe.loc[25,"wine"] = "Valdespino Moscatel Viejísimo Toneles" #complete name and no year


# In[19]:


data_dataframe.loc[25,"year"] = None


# In[20]:


data_dataframe.loc[31,"wine"] = "Pedro Ximénez Tradición VOS" #merge name and no year


# In[21]:


data_dataframe.loc[31,"year"] = None


# In[50]:


data_dataframe.price = data_dataframe.price.str.replace(" €", "")


# In[51]:


data_dataframe


# In[53]:


#data_dataframe.to_csv('/parker_wines_headers4.csv', header=True) set your own path

