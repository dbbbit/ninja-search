ninja-search
===

[shixiz.com](http://shixiz.com)

### require:

* flask
* elasticsearch + [ik分词插件](https://github.com/medcl/elasticsearch-analysis-ik)
* v2ex-scrapy 

爬取数据
--------

[准备数据](https://github.com/dbbbit/v2ex_scrapy)


elasticsearch 配置
-------------------

[安装 ik 分词](https://github.com/medcl/elasticsearch-analysis-ik)

esroot /config /elasticsearch.yml

    #: 启用 ES 动态脚本,以提供综合排序
    script.disable_dynamic: false


索引
--------

Scheme Mapping in ES 
    
    sh ninja-search/deploy/mapping_ik.sh

手动创建 Mongo 索引

    db.reply.createIndex({topic_id:1})

索引数据
    
    deploy/mongo2es.py 
    
将线上索引指向新的索引
    
    sh deploy/alias_v2_ik.sh


Run
----
  
    python index.py


Then you can search v2ex
