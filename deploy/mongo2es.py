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


def index(index_name, start_id=None, end_id=None):
    
    if not end_id:
        end_id = max_id()
    if not start_id:
        start_id = end_id - 200

    #: select * from topic where _id < end_id order by _id desc limit (end_id - start_id)
    cursor = db.find({"_id":{"$lt": end_id}})  \
                    .sort([('_id',-1)])     \
                        .batch_size(10)     \
                            .limit(end_id - start_id)

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

    """
        usage:
            1    ./deploy/mongo2es.sh
            2    ./deploy/mongo2es.sh start_id=1 end_id=3

    """
    args = {}

    for i in range(len(sys.argv)):
        kv = sys.argv[i].split('=')
        if len(kv) == 2:
            args[kv[0]]= int(kv[1])

    index('ik', **args)

