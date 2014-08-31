ninja-search
===

[shixiz.com](http://shixiz.com)

### require:

* [flask]()
* [elasticsearch]() or [elasticsearch-rtf]() (自带中文分词)
* [v2ex-scrapy (crawlers)]()

索引
--------

创建 index  

    curl -XPUT 'localhost:9200/v2'

mapping scheme  

    elasticsearch 下执行
    ./search/init.sh

    elasticsearch-rtf 下执行
    ./search/init_with_ik.sh

mongo index

    db.reply.createIndex({topic_id:1})

索引数据
    
    ./util/mongo2es.py


Run
----

    python index.py
