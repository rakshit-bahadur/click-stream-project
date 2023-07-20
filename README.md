# click-stream-project

## Overview

This is a data pipeline built to ingest clickstream data from Kafka, process it, and index the processed data in Elasticsearch. The pipeline performs real-time data processing and analysis on clickstream data from a web application. It includes the following components:

- Kafka Consumer: Consumes clickstream data from a Kafka topic.
- HBase Data Store: Stores the ingested data with a specific schema.
- Apache Spark Processor: Periodically processes the stored clickstream data for aggregations.
- Elasticsearch Indexer: Indexes the processed data in Elasticsearch for easy querying and analysis.

## Requirements

- Python 3.7+
- Apache Kafka
- Apache HBase
- Apache Spark
- Elasticsearch

## Installation

### Clone the repository:

git clone <repository_url>
cd data_pipeline_project

### Install dependencies for each component. Navigate to each subdirectory (ingestion, data_store, processing, indexing) and run:
pip install -r requirements.txt

### Set up Kafka, HBase, Spark, and Elasticsearch with proper configurations. Make sure all components are running.

### Configuration
Update the configuration files in the config/ directory with the appropriate settings for Kafka, HBase, Spark, and Elasticsearch.

### Start the Kafka Consumer:
python ingestion/kafka_consumer.py

### Run the main data pipeline:


### Folder Structure
The project folder structure is as follows:
data_pipeline_project/
│
├── ingestion/
│   ├── kafka_consumer.py
│   └── requirements.txt
│
├── data_store/
│   ├── hbase_utils.py
│   └── requirements.txt
│
├── processing/
│   ├── spark_processing.py
│   └── requirements.txt
│
├── indexing/
│   ├── elasticsearch_indexing.py
│   └── requirements.txt
│
├── config/
│   ├── kafka_config.json
│   ├── hbase_config.json
│   ├── spark_config.json
│   └── elasticsearch_config.json
│
├── utils/
│   └── common_utils.py
│
├── main.py
├── README.md
└── requirements.txt

Contributors
Your Name - Rakshit Bahadur

