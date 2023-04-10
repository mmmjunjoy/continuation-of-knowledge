#!/usr/bin/env python
# coding: utf-8

# In[3]:


import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest


# In[4]:


from newspaper import Article   #뉴스기사 text크롤링 해주는 라이브러리


# In[13]:


url = 'https://n.news.naver.com/article/036/0000048024?cds=news_media_pc&type=editn'


# In[16]:


article = Article(url,language = 'ko')


# In[17]:


article.download()


# In[18]:


article.parse()


# In[19]:


newsTitle = article.title


# In[20]:


print(newsTitle)

