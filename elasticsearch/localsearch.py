# Elasticsearch create index and query it.


from datetime import datetime
from elasticsearch import Elasticsearch
from pprint import pprint

es = Elasticsearch()

doc = {
    'author': 'g8gg',
    'text': 'Elasticsearch: cool. 棒棒哒!',
    'timestamp': datetime.now(),
}
# res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
# print(res['created'])
#
# res = es.get(index="test-index", doc_type='tweet', id=1)
# print(res['_source'])
#
# es.indices.refresh(index="test-index")

# res = es.search(index="logstash-2015.12.16",body={
#   "query" : {"match" : {"duration":64}},
#  })

res = es.search(index="logstash-2015.12.16", body={
    "query": {"matchall{}"}
})

print("Got %d Hits:" % res['hits']['total'])
pprint(res['hits']['hits'][0]['_source']['url'])
