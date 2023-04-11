#!/usr/bin/env python
# coding: utf-8

# In[3]:


import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest


# In[4]:


from newspaper import Article   #뉴스기사 text크롤링 해주는 라이브러리


# In[97]:


url = 'https://www.nytimes.com/2023/04/09/world/europe/europe-shells-ukraine-ammunition.html'


# In[98]:


article = Article(url)


# In[99]:


article.download()


# In[100]:


article.parse()


# In[101]:


newsTitle = article.title


# In[102]:


newstext= article.text


# In[115]:


# summarize code

def summarize(text,per):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    tokens = [token.text for token in doc]
    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text]=1
                else:
                    word_frequencies[word.text] += 1
    max_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word]= word_frequencies[word]/max_frequency
    sentence_tokens = [sent for sent in doc.sents]
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                sentence_scores[sent]=word_frequencies[word.text.lower()]
            else:
                sentence_scores[sent]+=word_frequencies[word.text.lower()]
    
    select_length = int(len(sentence_tokens)*per)
    summary = nlargest(select_length,sentence_scores,key=sentence_scores.get)
    final_summary =[word.text for word in summary]
    summary = ''.join(final_summary)
    return summary
    


# In[116]:


# 번역 코드

import googletrans

translator = googletrans.Translator()

instr = '안녕하세요'

outstr = translator.translate(instr,dest='en', src = 'auto')

print(f"{instr} => {outstr.text}")


# In[117]:


summarized_text = summarize(newstext,0.05)
summarized_text


# In[ ]:




