#!/usr/bin/python
import time
import sys
from elasticsearch import Elasticsearch
from datetime import datetime
from pymongo import MongoClient
import requests

es = Elasticsearch()
client = MongoClient('mongodb://localhost:27017/')
db = client['v2ex']['topic'] 


def max_id():

    #: get max document id 
    return db.find().sort("_id", -1).limit(1)[0]['_id']


def index(index_name, size):
    
    MAX = max_id()

    #: select * from topic where _id < MAX order by _id desc limit 200
    cursor = db.find({"_id":{"$lt": MAX}})  \
                    .sort([('_id',-1)])     \
                        .batch_size(10)     \
                            .limit(size)

    for item in cursor:
        item['created'] = item['created'] * 1000
        item['last_modified'] = item['last_modified'] * 1000
        item['last_touched'] = item['last_touched'] * 1000

        #: merge repies to topic 
        item['rcontent'] = get_replies(item['_id'])
        try:
            a = time.time()
            es.index(index=index_name, doc_type="topic", id=item['_id'], body=item)
            b = time.time()

        except Exception, e:
            print(e)
            time.sleep(5)
            continue
       
        info = str(datetime.now()) + "cost %d ms: topic %d indexed."%((b-a)*1000, item['_id'])
        print(info)


def get_replies(topic_id):

    """
        get repies of topic_id
        return 
            string:
                'username created content username created content ...'
    """

    rcontent = u""
    db = client['v2ex']['reply']
    
    for r in db.find({"topic_id":topic_id}):
        rcontent += r['member']['username']     
        rcontent += " " + datetime.fromtimestamp(r['created']).strftime('%Y-%m-%d')
        rcontent += " " + r['content'] + "    "
    
    return rcontent


if __name__ == '__main__':
    #: index the last 200 topics with replies
    index('ik', 200)

