from fastapi import FastAPI
from fastapi.testclient import TestClient

import pytest
import httpx

# importing the sys module
import sys        
 
# inserting the mod.py directory at 
# position 1 in sys.path
sys.path.insert(1, '/workspace/fastapi-docker/') 

from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}