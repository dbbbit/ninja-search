#!/usr/bin/python
import time
from elasticsearch import Elasticsearch
from datetime import datetime
from pymongo import MongoClient


es = Elasticsearch()
client = MongoClient('mongodb://localhost:27017/')


def index():
    db = client['v2ex']['topic'] 

    for item in db.find():
        item['created'] = item['created'] * 1000
        item['last_modified'] = item['last_modified'] * 1000
        item['last_touched'] = item['last_touched'] * 1000
        item['rcontent'] = get_replies(item['_id'])
        try:
            es.index(index='v2', doc_type="topic", id=item['_id'], body=item)
        except Exception, e:
            print(e)
            time.sleep(5)
       
        info = "indexed topic %d"%(item['_id'])
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
    index()
    print(get_replies(1000))
