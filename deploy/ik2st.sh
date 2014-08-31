#!/bin/bash
# v2--> ik  ==> v2-->st
curl -XPOST localhost:9200/_aliases -d '
{
    "actions": [
        { "remove": {
            "alias": "v2",
            "index": "ik"
        }},
        { "add": {
            "alias": "v2",
            "index": "st"
        }}
    ]
}
'
