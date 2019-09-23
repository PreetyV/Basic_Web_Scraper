#!/usr/bin/env python
# coding: utf-8

# In[10]:


from nltk import tokenize
import requests
import csv
import re
requests.adapters.DEFAULT_RETRIES = 5
from bs4 import BeautifulSoup


# In[11]:


# In[ ]:
counter = 0
Helist = []
Shelist = []
while counter != 50:
    response = requests.get("https://theyfightcrime.org")
    l_objContent = response.content
    l_objSoup = BeautifulSoup(l_objContent)
    l_objList = l_objSoup.findAll('p')
    l_objPara = l_objList[1]
    sentenceList = tokenize.sent_tokenize(l_objPara.text)
    Helist.append(sentenceList[0])
    Shelist.append(sentenceList[1])
    counter = counter + 1
   
# l_objList = l_objList[:-1]
# # print(l_objList)
# print("++++++++++++++++++++++++++++++++++++++++++")
# print(Helist)
# print("++++++++++++++++++++++++++++++++++++++++++")
# print(Shelist)

with open('Helist.txt', 'w') as f:
    for character in Helist:
        f.write("%s\n" % character)
with open('Shelist.txt', 'w') as f:
    for character in Shelist:
        f.write("%s\n" % character)


# In[ ]:





# In[ ]:




