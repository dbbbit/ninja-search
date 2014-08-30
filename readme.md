ninja-search
===

[shixiz.com](http://shixiz.com)

### require:

* [flask]()
* [elasticsearch]()
* [v2ex-scrapy (crawlers)]()

索引
--------

创建 index  

    curl -XPUT 'localhost:9200/v2'

mapping scheme  

    ./search/init.sh

mongo index

    db.reply.createIndex({topic_id:1})

索引数据
    
    ./util/mongo2es.py



