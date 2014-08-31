#!/bin/bash
curl -XPOST localhost:9200/_aliases -d '
{
    "actions": [
        { "remove": {
            "alias": "v2",
            "index": "v2_1"
        }},
        { "add": {
            "alias": "v2",
            "index": "v2_2"
        }}
    ]
}
'