#!/usr/bin/env python
# coding: utf-8

# In[5]:


def pig_latin(word):
    
    first_letter=word[0]
    
    if first_letter in 'aeiou':
        pig_word=word+'ay'
    else:
        pig_word=word[1:]+first_letter+'ay'
    return pig_word


# In[6]:


pig_latin('chintan')


# In[7]:


pig_latin('akshay')


# In[8]:


pig_latin('book')


# In[ ]:




