#!/bin/bash
# v2 --> ik
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
