from time import sleep
from urllib import response
from main import app

from fastapi.testclient import TestClient

client = TestClient(app)

def test_events_status():
    response = client.post("/api/v1/events")
    assert response.status_code == 200

def test_stats_status():
    response = client.get("/api/v1/stat/")
    assert response.status_code == 200

def test_counter_words():
    #Testing the flow of counting sentence and then check the reusult
    response = client.post("/api/v1/events", "Avanan is a leading Enterprise Solution\
for Cloud Email and Collaboration Security")
    response2 = client.get("/api/v1/stat/?interval=2")
    assert response.status_code == 200
    assert response2.status_code == 200
    assert response2.json() == {"checkpoint":0,"avanan":1,"email":1,"security":1}

def test_counter_words_not_appear():
    #Testing the flow of counting sentence and then check the reusult
    response = client.post("/api/v1/events", "Leading Enterprise Solution for Cloud")
    response2 = client.get("/api/v1/stat/?interval=3")

    assert response2.status_code == 200
    assert response2.json() == {"checkpoint":0,"avanan":1,"email":1,"security":1}

def test_counter_words_correctness():
    #Testing the flow of counting sentence and then check the reusult
    response = client.post("/api/v1/events", "Leading Enterprise Solution for Cloud")
    response2 = client.get("/api/v1/stat/?interval=3")

    assert response2.status_code == 200
    assert response2.json() != {"checkpoint":4,"avanan":1,"email":1,"security":1}


def test_stat_bad_input():
    #Testing the raise error if input is not number
    response = client.post("/api/v1/events", "Leading Enterprise Solution for Cloud")
    response2 = client.get("/api/v1/stat/?interval=input")
    assert response.status_code == 200
    assert response2.status_code == 422
    
    
async def wait_for_5sec_and_check():
    #the test wait 5 seconds and then check the results. should be zero
    await sleep(5.0)
    response = client.get("/api/v1/stat/?interval=1")
    response.json() == {"checkpoint":0,"avanan":0,"email":0,"security":0}

async def wait_and_check():
    #the test wait 5 seconds and then check the results. should be zero
    await sleep(5.0)
    response = client.get("/api/v1/stat/?interval=1")
    response.json() != {"checkpoint":2,"avanan":0,"email":0,"security":0}