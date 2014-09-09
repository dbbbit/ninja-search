#!/bin/bash
#：定时更新索引
now()  
{  
    date "+%Y-%m-%d"  
}  

t=`now`

cd `dirname $0`
/usr/bin/python ./deploy/mongo2es.py 


# crontab -e
# add next line to the file
# */35     *       *       *       *       sh /home/ubuntu/Repo/ninja-search/index.sh > /tmp/cron_index.log 2>&1
