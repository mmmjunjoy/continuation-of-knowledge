# main.py 파일 생성 후 서버 코드 작성하기


from fastapi import FastAPI
app = FastAPI()

@app.get("/")

def one():
    return 'good'


# app.get("/ ") -> 이 부분을 변경 해줌으로써 저 부분에는 다른 데이터가 들어간것을
# 확인 할 수 있다.

@app.get("/secondpage")
def two():
    return {'today':'soso'}


# BaseModel을 사용한 유저에게 데이터 받기

from pydantic import BaseModel

class Model(BaseModel):
    name : str
    phonenumber : int

@app.post("/send")

def datacommit(data:Model):
    print(data)
    return '전송완료'




# async/await 키워드 비동기 처리 기능


# 특정 로직의 실행이 끝날때까지 기다려주지 않고 나머지 코드를 먼저 실행하는 것을 비동기 처리라고 한다.

@app.get("/")

async def bee():
    result = await some_library()
    
    return result