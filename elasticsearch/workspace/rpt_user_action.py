# learning json utility and get report from ES service via REST API

from json import encoder, decoder, dumps, dump
from jsonschema import validate
from requests import request
from datetime import datetime
from elasticsearch import Elasticsearch
from pprint import pprint

es = Elasticsearch(hosts="139.196.20.147:9200")
query = """{
  "query": {
    "filtered": {
      "query": {
        "query_string": {
          "analyze_wildcard": true,
          "query": "*"
        }
      },
      "filter": {
        "bool": {
          "must": [
            {
              "range": {
                "dt": {
                  "gte": 1452009600000,
                  "lte": 1452095999999,
                  "format": "epoch_millis"
                }
              }
            }
          ],
          "must_not": []
        }
      }
    }
  },
  "size": 0,
  "aggs": {
    "2": {
      "terms": {
        "field": "action_method",
        "size": 50,
        "order": {
          "_count": "desc"
        }
      }
    }
  }
}"""

# res = es.get(index="user_action", doc_type='user_action', params=query)
# pprint(res['_source'])

res = es.search(index="user_action", body=query)
print("Got %d Hits:" % res['hits']['total'])

for hit in res['aggregations']['2']['buckets']:
    print("%(key)s → %(doc_count)d" % hit)
