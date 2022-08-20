#!/usr/bin/env python
# coding: utf-8

# In[1]:


#What does an empty dictionary's code look like?#


# In[4]:


a = {"foo" : 42}


# In[5]:


a


# In[6]:


#What is the most significant distinction between a dictionary and a list?


# In[7]:


# list store in order form 
#  dic not store in order from its unorderd


# In[8]:


#What happens if you try to access spam['foo'] if spam is {'bar': 100}?


# In[12]:


a= {'bar' : 100}


# In[13]:


spam["foo"]


# In[14]:


#NameError: name 'spam' is not defined it will give this error


# In[15]:


#If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?


# In[33]:


spam ={"cat": 100}


# In[34]:


"cat" in spam


# In[35]:


"cat" in spam.keys()


# In[36]:


# both expression will give true bcoz of we have cat in dic 


# In[37]:


# q 6 If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?


# In[39]:


spam = {"cat":23}


# In[40]:


"cat" in spam # it will chack key in dic "cat then return true or false 


# In[42]:


"cat" in spam.values() # it will check "cat" in value then return true or false


# In[45]:


#What is a shortcut for the following code?


# In[44]:


spam = {"foo" : "soo"}


# In[46]:


spam.setdefault("color","green")


# In[48]:


spam


# In[51]:


import pprint as pp  # importing of ppprint module 


# In[58]:


dct = [ {'Name': 'Sonu', 'Age': '33', 'city': 'alwar'},
  {'Name': 'monu', 'Age': '34', 'city': 'mathura'},
  {'Name': 'tonu', 'Age': '39', 'city': 'ramgarh'},
  {'Name': 'munna', 'Age': '35', 'city': 'delhi'}
]


# In[61]:


pp.pprint(dct) # using of pp print function


# In[ ]:





# In[ ]:




