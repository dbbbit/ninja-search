#!/bin/bash
# v2 --> ik
# [why use alias?] http://www.elasticsearch.org/blog/changing-mapping-with-zero-downtime/
# [Doc] http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-aliases.html

curl -XPOST localhost:9200/_aliases -d '
{
    "actions": [
        { "add": {
            "alias": "v2",
            "index": "ik"
        }}
    ]
}
'
