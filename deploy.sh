
sudo apt-get install default-jre
sudo apt-get install default-jdk
cd ..
curl -L -O https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.3.0.tar.gz
tar -xvf elasticsearch-1.3.0.tar.gz
cd elasticsearch-1.3.0/bin
./elasticsearch -d


sudo pip install uwsgi

sudo pip install flask