#!/usr/bin/env python
# coding: utf-8

# In[1]:


from konlpy.tag import Kkma
from konlpy.tag import Twitter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
import numpy as np


# In[2]:


news_content = "Queue는 한쪽 끝(rear)에서는 enqueue, 또 다른 끝(front)에서는 dequeue 연산을 하는 유한 순서리스트이다.Queue는 FIFO(First in First out) 리스트이다.front는 dequeue할 위치를 기록하고 rear은 enqueue할 위치를 기록한다.front와 rear가 같으면 큐는 비었다는 의미와 같다.rear는 입력할 데이터의 인덱스를 가리키기에 큐의 마지막 인덱스라면 더이상 원소를 집어넣을 수 없기에 에러를 발생시킨다. 그렇지 않다면 그 다음 인덱스에 원소를 넣는다.큐가 비었다면(rear == front) 빼낼 원소가 없기에 에러를 발생시키고 deque할 원소를 기록할 front를 1 더해준다.deque 연산과 비슷한 방식이다.peek: front가 가리키는 원소를 리턴한다.delete: front가 가리키는 원소를 삭제한다.(front + 1)순차표현의 문제점: 크기가 8인 배열에서 rear = 7, front = 3일때 0,1,2 인덱스는 비었지만 사용하지 못한다.순차표현의 문제를 해결하기 위해 원형 큐 고안rear를 하나 증가시켰을 때 rear = front 라면 가득찼다는 의미와 같다.원형 큐는 순차표현 큐에 비해 빈공간을 남기지 않아 메모리 공간을 잘 활용하지만 배열로 구현되기에 큐의 크기는 제한된다는 단점이 있다.한정된 크기를 개선하기 위해 연결리스트 큐 고안.연결리스트 표현으로 바뀌었지만 내부 동작은 순차표현 큐와 비슷하다."


# In[3]:


kkma = Kkma()


# In[4]:


def text2sentences(text):
    sentences = kkma.sentences(text)
    for idx in range(0,len(sentences)):
        if len(sentences[idx]) <= 10:
            sentences[idx-1] +=(' '+ sentences[idx])
            sentences[idx] = ''
    
    return sentences


# In[5]:


sentences = text2sentences(news_content)


# In[19]:


twitter = Twitter()
from konlpy.tag import Okt

okt = Okt()


# In[20]:


# nouns = okt.morphs(sentences)


# In[71]:


def get_nouns(sentences):
    nouns = []
    for sentence in sentences:
        if sentence is not '':
            nouns.append(' '.join([noun for noun in twitter.nouns(str(sentence))
                                  if len(noun)>1]))
                                
            
    return nouns


# In[72]:


nouns = get_nouns(sentences)


# In[73]:


print(sentences[0])


# In[74]:


print(nouns[0])


# In[75]:


tfidf = TfidfVectorizer()
cnt_vec = CountVectorizer()
graph_sentence =[]


# In[76]:


def build_sent_graph(sentence):
    tfidf_mat = tfidf.fit_transform(sentence).toarray()
    graph_sentence = np.dot(tfidf_mat, tfidf_mat.T)
    return graph_sentence

sent_graph = build_sent_graph(nouns)


# In[77]:


sent_graph


# In[78]:


def build_words_graph(sentence):
    cnt_vec_mat = normalize(cnt_vec.fit_transform(sentence).toarray().astype(float), axis =0)
    vocab = cnt_vec.vocabulary_
    return np.dot(cnt_vec_mat.T,cnt_vec_mat),{vocab[word] :word for word in vocab}
    words_graph , idx2word = build_words_graph(nouns)
                 


# In[79]:


words_graph = build_words_graph(nouns)


# In[80]:


words_graph


# In[81]:


def get_ranks(graph, d =0.85):
    A=graph
    matrix_size = A.shape[0]
    for id in range(matrix_size):
        A[id,id]=0
        link_sum = np.sum(A[:,id])
        if link_sum != 0:
            A[:,id] /= link_sum
        A[:,id] *= -d
        A[id,id]= 1
        
    B = (1-d) * np.ones((matrix_size,1))
    
    ranks = np.linalg.solve(A,B)
    return {idx: r[0] for idx , r in enumerate(ranks)}


# In[82]:


sent_rank_idx = get_ranks(sent_graph)


# In[83]:


sent_rank_idx


# In[84]:


sorted_sent_rank_idx = sorted(sent_rank_idx , key = lambda k : sent_rank_idx[k] , reverse=True)


# In[85]:


sorted_sent_rank_idx


# In[86]:


word_rank_idx = get_ranks(words_graph)
sorted_word_rank_idx = sorted(word_rank_idx , key=lambda k : word_rank_idx[k], reverse = True)


# In[90]:


def summarize(sent_num = 2):
    summary = []
    index = []
    for idx in sorted_sent_rank_idx[:sent_num]:
        index.append(idx)
    index.sort()
    
    for idx in index:
        summary.append(sentences[idx])
        
    for text in summary:
        print(text)
        print("\n")


# In[91]:


summarize()


# In[ ]:




