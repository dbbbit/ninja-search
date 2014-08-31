#!/usr/bin/python
import time
from elasticsearch import Elasticsearch
from datetime import datetime
from pymongo import MongoClient

START = 1
es = Elasticsearch()
client = MongoClient('mongodb://localhost:27017/')


def index(index_name):
    db = client['v2ex']['topic'] 
    cursor = db.find({"_id":{"$gt":START}}).sort('_id')
    for item in cursor:
        item['created'] = item['created'] * 1000
        item['last_modified'] = item['last_modified'] * 1000
        item['last_touched'] = item['last_touched'] * 1000
        item['rcontent'] = get_replies(item['_id'])
        try:
            a = time.time()
            es.index(index=index_name, doc_type="topic", id=item['_id'], body=item)
            b = time.time()

        except Exception, e:
            print(e)
            time.sleep(5)
            continue
       
        info = "indexed topic %d cost time %d"%(item['_id'],b-a)
        print(info)


def get_replies(topic_id):

    """
        return replies like:
            'username created content  [username created content ...]'
    """

    rcontent = u""
    db = client['v2ex']['reply']
    for r in db.find({"topic_id":topic_id}):
        rcontent += r['member']['username']     
        rcontent += " " + datetime.fromtimestamp(r['created']).strftime('%Y-%m-%d')
        rcontent += " " + r['content'] + "    "

    return rcontent


if __name__ == '__main__':
    index('v2_1')

