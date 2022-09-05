#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#kaggle_data = pd.read_csv('/wines_SPA.csv') set your own path


# In[3]:


kaggle_data.head()


# In[4]:


kaggle_data.info("deep")


# In[5]:


kaggle_data.drop_duplicates().shape, kaggle_data.shape
#how many duplicates, a lot


# In[6]:


kaggle_data.drop_duplicates(inplace=True) #drop duplicates


# In[7]:


kaggle_data.shape


# In[8]:


kaggle_data['country'].value_counts() 


# In[9]:


kaggle_data['rating'].value_counts() #everything correct on this column


# In[10]:


kaggle_data[kaggle_data['num_reviews'] <= 25] #all wines have at least 25 reviews so everything OK


# In[11]:


kaggle_data['region'].value_counts().head(30)


# In[12]:


kaggle_data['year'].value_counts().head(50)


# In[13]:


lst_null_year = list(kaggle_data[kaggle_data['year']=='N.V.'].index)


# In[14]:


for i in lst_null_year:
        kaggle_data.loc[i,"year"] = None

#wines with no year are set to None


# In[15]:


#vivino_data = pd.read_csv('/scraped_data_header.csv') set your own path


# In[16]:


vivino_data.head()


# In[17]:


vivino_data.info("deep")


# In[18]:


vivino_data['rating'] = [i.replace(",",".") for i in vivino_data['rating']] #to leave ratings as previous dataframes


# In[19]:


vivino_data['rating'].value_counts()


# In[20]:


vivino_data['rating'] = vivino_data['rating'].astype('float64')


# In[21]:


vivino_data.info("deep")


# In[22]:


vivino_data['year'].value_counts()


# In[23]:


lst_future_wines = list(vivino_data[vivino_data['year'] > 2022].index)


# In[24]:


vivino_data.shape


# In[25]:


vivino_data.drop(lst_future_wines,inplace=True) #drop 72 wines with year over 2022 (current year)


# In[26]:


vivino_data.shape


# In[27]:


lst_ancient_wines = list(vivino_data[vivino_data['year'] <= 1900].index)


# In[28]:


for i in lst_ancient_wines:
        vivino_data.loc[i,"year"] = None

#wines with ancient year are set to None, they are good reads


# In[29]:


vivino_data['year'] = vivino_data['year'].astype(str).apply(lambda x: x.replace('.0',''))


# In[30]:


lst_wines_both = list(vivino_data[vivino_data['rating'] >= 4.2].index)


# In[31]:


vivino_data.drop(lst_wines_both, inplace=True) #we drop the very few wines with ratings overlapping the previous database


# In[32]:


lst_null_year2 = list(vivino_data[vivino_data['year']=="nan"].index)


# In[33]:


for i in lst_null_year2:
        vivino_data.loc[i,"year"] = None

#wines with "nan" year are set to None


# In[34]:


kaggle_data.info("deep")


# In[35]:


vivino_data.info("deep")


# In[36]:


vivino_data.rename(columns = {'num_review':'num_reviews'}, inplace = True) #fixed column name that was different


# In[37]:


vivino_data['price']


# In[38]:


vivino_data['price'] = [str(i).replace(",",".") for i in vivino_data['price']] #to leave price as previous dataframe


# In[39]:


vivino_data['price'] = vivino_data['price'].astype('float64')


# In[40]:


grouped_data = pd.concat([kaggle_data,vivino_data])


# In[41]:


grouped_data.info("deep")


# In[42]:


grouped_data.drop('country', axis=1, inplace=True) #country is always Spain so I delete it


# In[43]:


#grouped_data.to_csv('/grouped_data.csv')


# In[44]:


grouped_data


# In[45]:


#parker_data = pd.read_csv('/parker_wines_headers4.csv') set your own path


# In[46]:


parker_data


# In[47]:


parker_data.drop('Unnamed: 0', axis=1, inplace=True)


# In[48]:


parker_data.info("deep")


# In[49]:


null_year_parker = list(parker_data[parker_data['year']==' cl.'].index)


# In[50]:


null_year_parker


# In[51]:


for i in null_year_parker:
        parker_data.loc[i,"year"] = None

#wines with no year are set to None


# In[52]:


parker_data.loc[31,"wine"] = "Colosía Pedro Ximénez"
parker_data.loc[31,"year"] = None


# In[53]:


parker_data.loc[28,"wine"] = "Moscatel Superior Emilín"
parker_data.loc[28,"year"] = None


# In[54]:


parker_data['price'] = [str(i).replace(",",".") for i in parker_data['price']] #to leave price as previous dataframe


# In[55]:


parker_data.loc[33,"price"] = 1230.25


# In[56]:


parker_data['price'] = parker_data['price'].astype('float64')


# In[57]:


def create_columns():
    parker_data['winery'] = None
    parker_data['rating'] = None
    parker_data['num_reviews'] = None
    parker_data['type'] = None
    parker_data['body'] = None
    parker_data['acidity'] = None   


# In[58]:


create_columns()


# In[59]:


grouped_data['parker_score'] = None


# In[60]:


parker_data = parker_data.reindex(columns=list(grouped_data.columns))


# In[61]:


#both tables can be concatenated now


# In[62]:


grouped_data.info("deep")


# In[63]:


final_data = pd.concat([grouped_data,parker_data])


# In[64]:


final_data.info("deep")


# In[65]:


final_data['rating'] = final_data['rating'].astype('float64')


# In[77]:


final_data[final_data['wine'].str.contains('Contador')] #search for duplicates manually


# In[ ]:


final_data.loc[400,"parker_score"] = 93
final_data.drop([16], axis=0, inplace=True) #wine that was in both datasets


# In[ ]:


final_data.loc[2033,"parker_score"] = 93
final_data.drop([2008], axis=0, inplace=True)
final_data.drop([21], axis=0, inplace=True) #wine that was in both datasets


# In[78]:


#final_data.to_csv('/final_data.csv') for saving the file


# In[79]:


from sqlalchemy import create_engine


# In[80]:


with open('password.txt', 'r') as file:
    pass_=file.readlines()[0]

str_conn=f'mysql+pymysql://root:{pass_}@localhost:3306'


# In[81]:


cursor=create_engine(str_conn)


# In[82]:


str_conn=f'mysql+pymysql://root:{pass_}@localhost:3306/wines' #database was already created on workbench


# In[83]:


cursor_sql=create_engine(str_conn)


# In[84]:


final_data.to_sql(name='data', index=True, con=cursor_sql)


# In[85]:


final_data.shape


# In[ ]:


#everything uploaded correctly

