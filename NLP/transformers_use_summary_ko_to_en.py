#!/usr/bin/env python
# coding: utf-8

# In[1]:


from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


# In[2]:


# 모델과 토크나이저 로드
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ko-en")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ko-en")


# In[3]:


# 요약할 텍스트 입력
input_text = "Queue는 한쪽 끝(rear)에서는 enqueue, 또 다른 끝(front)에서는 dequeue 연산을 하는 유한 순서리스트이다.Queue는 FIFO(First in First out) 리스트이다.front는 dequeue할 위치를 기록하고 rear은 enqueue할 위치를 기록한다.front와 rear가 같으면 큐는 비었다는 의미와 같다.rear는 입력할 데이터의 인덱스를 가리키기에 큐의 마지막 인덱스라면 더이상 원소를 집어넣을 수 없기에 에러를 발생시킨다. 그렇지 않다면 그 다음 인덱스에 원소를 넣는다.큐가 비었다면(rear == front) 빼낼 원소가 없기에 에러를 발생시키고 deque할 원소를 기록할 front를 1 더해준다.deque 연산과 비슷한 방식이다.peek: front가 가리키는 원소를 리턴한다.delete: front가 가리키는 원소를 삭제한다.(front + 1)순차표현의 문제점: 크기가 8인 배열에서 rear = 7, front = 3일때 0,1,2 인덱스는 비었지만 사용하지 못한다.순차표현의 문제를 해결하기 위해 원형 큐 고안rear를 하나 증가시켰을 때 rear = front 라면 가득찼다는 의미와 같다.원형 큐는 순차표현 큐에 비해 빈공간을 남기지 않아 메모리 공간을 잘 활용하지만 배열로 구현되기에 큐의 크기는 제한된다는 단점이 있다.한정된 크기를 개선하기 위해 연결리스트 큐 고안.연결리스트 표현으로 바뀌었지만 내부 동작은 순차표현 큐와 비슷하다."


# In[4]:


# 입력 텍스트를 토큰화하여 모델 입력 형식으로 변환
input_ids = tokenizer.encode(input_text, return_tensors ="pt")


# In[5]:


summary_ids = model.generate(input_ids)


# In[6]:


summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)


# In[7]:


print(summary_text)


# In[ ]:




