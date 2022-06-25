from typing import Union
from datetime import datetime
from fastapi import FastAPI, Request, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime, timedelta
import asyncio

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    sentence: str

app = FastAPI()

words = ['checkpoint', 'avanan', 'email', 'security']
word_dict ={'checkpoint': [], 'avanan':[], 'email':[], 'security':[]}

@app.post("/api/v1/events")
async def count_words_sentence(req: Request):
    #Extract the request body
    words = (await req.body()).decode("utf-8")

    #using the asyncio for async operation
    await asyncio.gather(counter_words(words))

async def counter_words(words):
    #define the current time for sentence. 
    dt = datetime.now()
    #Iterate over the sentence and add the dt object to the dictionary
    for word in words.split(" "):
        #validate the wors is one of the required words.
        ## In any time - we can expand the words we are counting
        ## by adding keys to word_count dict above. All the word will covert to lowercase.
        if word.lower() in word_dict: 
            word_dict[word.lower()].append(dt)

@app.get("/api/v1/stat/")
async def count_words_sentence(interval: int = 0):
    try:
        interval = interval
    except:
        raise HTTPException(status_code=404, detail="please enter number to presernt interval(seconds)")
    #Define the datetime object of intervalSeconds ago
    sec_age = datetime.now() - timedelta(seconds= interval)
    #Init result object
    result = {'checkpoint': 0, 'avanan':0 , 'email': 0, 'security': 0}

    for word in word_dict.keys():
        #count the timestemps of the word that appears in the time interval
        temp_count = sum(i >= sec_age for i in word_dict[word])
        #Set the counter in the result 
        result[word] += temp_count
        
    #Convert the result to json object
    json_result = jsonable_encoder(result)
    return JSONResponse(content=json_result)


