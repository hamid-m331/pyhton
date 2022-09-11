from datetime import datetime
from elasticsearch import Elasticsearch
import time
import requests
# Written by Hamid Madahian with help of DevOps team
es = Elasticsearch(
    'https://elk.example.com:443',
    # ca_certs="/path/to/http_ca.crt"
    basic_auth=("user", "pass"),
    verify_certs=False
)
URL="https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
get=requests.get(URL)

while True:
    response = get.json()
    for i in response:
        if i['id'] == "ethereum":
            dt = datetime.now()
            es.index(index="k8s", id=dt, document=i)
    time.sleep(1)
