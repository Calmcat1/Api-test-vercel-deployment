from fastapi import FastAPI
import json

app = FastAPI()


@app.get('/data/Application/v1')
async def get_json_data():
  with open('../Data/testData.json', 'r') as json_file:
    json_data = json_file.read()
  return json.loads(json_data)
