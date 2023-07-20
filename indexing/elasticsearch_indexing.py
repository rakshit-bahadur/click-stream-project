from elasticsearch import Elasticsearch

class ElasticsearchIndexer:
    def __init__(self, es_hosts, index_name):
        self.es = Elasticsearch(es_hosts)
        self.index_name = index_name

    def index_data(self, data):
        for _, row in data.iterrows():
            doc = {
                'url': row['click_data:url'],
                'country': row['geo_data:country'],
                'unique_users': row['unique_users'],
                'clicks': row['clicks'],
                'average_time_spent': row['average_time_spent']
            }
            self.es.index(index=self.index_name, doc_type='_doc', body=doc)
