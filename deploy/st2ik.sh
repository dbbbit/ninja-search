#!/bin/bash
# v2-->st   ==> v2-->ik
curl -XPOST localhost:9200/_aliases -d '
{
    "actions": [
        { "remove": {
            "alias": "v2",
            "index": "st"
        }},
        { "add": {
            "alias": "v2",
            "index": "ik"
        }}
    ]
}
'
