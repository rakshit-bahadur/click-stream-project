from utils.common_utils import read_json_config
from ingestion.kafka_consumer import KafkaConsumer
from data_store.hbase_utils import HBaseUtils
from processing.spark_processing import SparkProcessor
from indexing.elasticsearch_indexing import ElasticsearchIndexer

def main():
    # Read configurations from config files
    kafka_config = read_json_config('config/kafka_config.json')
    hbase_config = read_json_config('config/hbase_config.json')
    spark_config = read_json_config('config/spark_config.json')
    es_config = read_json_config('config/elasticsearch_config.json')

    # Instantiate KafkaConsumer and process incoming data
    kafka_consumer = KafkaConsumer(kafka_config['topic'], kafka_config['bootstrap_servers'])
    for message in kafka_consumer.consume():
        data = kafka_consumer.process_message(message)

        # Assuming data is in the format {'row_key': ..., 'click_data': ..., 'geo_data': ..., 'user_agent_data': ...}
        row_key = data['row_key']
        click_data = data['click_data']
        geo_data = data['geo_data']
        user_agent_data = data['user_agent_data']

        # Store data in HBase
        hbase_utils = HBaseUtils(hbase_config['host'], hbase_config['port'], hbase_config['table_name'])
        hbase_utils.store_data(row_key, click_data, geo_data, user_agent_data)

    # Process data periodically with Spark
    spark_processor = SparkProcessor(hbase_config['table_name'])
    processed_data = spark_processor.process_data()

    # Index processed data in Elasticsearch
    es_indexer = ElasticsearchIndexer([es_config['host']], es_config['index_name'])
    es_indexer.index_data(processed_data)

if __name__ == "__main__":
    main()
