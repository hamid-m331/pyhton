from datetime import datetime
from elasticsearch import Elasticsearch
from random import getrandbits
import json
import sys
import time
import requests
# Written by Hamid Madahian with help of DevOps team
es = Elasticsearch(
    'https://elk.charisma.tech:443',
    # ca_certs="/path/to/http_ca.crt"
    basic_auth=("madahian", "123@abc"),
    verify_certs=False
)

MyFile= open("/home/hamid/Downloads/Sample-employee-JSON-data.json",'r').read()
URL="https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
get=requests.get(URL)

while True:
    response = get.json()
    for i in response:
        if i['id'] == "ethereum":
            dt = datetime.now()
            es.index(index="k8s", id=dt, document=i)
    time.sleep(1)
