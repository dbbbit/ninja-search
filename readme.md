ninja-search
===

[shixiz.com](http://shixiz.com)

### require:

* [flask]()
* [elasticsearch]()
* [v2ex-scrapy (crawlers)]()

新建索引
--------

创建 index  

    curl -XPUT 'localhost:9200/v2'

mapping scheme  

    ./search/init.sh

索引数据

    ./util/mongo2es.py



