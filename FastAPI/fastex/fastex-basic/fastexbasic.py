### 기본 API 만들기기(PUT,PATCH) ###


# FastAPI는 Pydantic에서 제공하는 BaseModel을 기반으로 하여금 
# Request,Response타입의 문서를 자동화 시켜줍니다.


# PUT , PATCH 메소드는 UPDATE에 해당하는 메소드입니다. 
# 두 개의 차이는 모든 내용을 바꾼다 -> put 
# 일부의 내용을 바꾼다 -> patch 


# 문제점 ; field 가 import 가 안된다.

import json
import requests
from typing import Optional
import uuid
from fastapi import FastAPI  #,Field  -> import 가 안된다.
from pydantic import BaseModel 


from starlette.responses import JSONResponse


app = FastAPI()

@app.route('/health')
async def health_check():
    return "ok"

# name , description 파라미터를 사용하여 제목과 설명을 바꿀 수 있다.

@app.get("/get/{name}", name = "사용자 ID 생성" , description="사용자 이름을 받고 ID를 생성하는 API 입니다.")


async def generate_id_for_name(name:str):
  return JSONResponse({
      'id' : str(uuid.uuid4()),
      'name' : name
  })
  


class Item(BaseModel):
    user_id: str #= Field(title='사용자가 사용할 ID')
    password : str #= Field(title='사용자가 사용할 Password')

#응답 파라미터에 대한 상세 사항 

class ResponseItem(Item):
    success: bool #= Field(True, "처리 여부/결과")


@app.post("/register", response_model=ResponseItem)

async def register_item(item: Item):
  global dicted_item
  dicted_item = dict(item)
  dicted_item['success'] = True

  return JSONResponse(dicted_item)


@app.put("/update")
async def update_item(item : Item):
  dicted_item = {k:v for k,v in dict(item).items()}
  dicted_item['success'] = True

  return JSONResponse(dicted_item)


class PatchItem(BaseModel):
    user_id: Optional[str] #= Field(None,title='사용자가 사용할 ID')
    password: Optional[str] #= ##Field(None,title='사용자가 사용할 Password')


@app.patch("/update")
async def update_item_sub(item: PatchItem):
    dicted_item ={}
    for k,v in dict(item).Itmes():
        if v:
            dicted_item[k] = v
    dicted_item['success'] = True
    
    return JSONResponse(dicted_item)

@app.delete("/delete")
async def delete_item():
    dicted_item = None
    return Response(status_code=HTTP_204_NO_CONTENT)



