from pyspark.sql import SparkSession
from pyspark.sql.functions import col, countDistinct, avg

class SparkProcessor:
    def __init__(self, hbase_table_name):
        self.spark = SparkSession.builder.appName('ClickstreamProcessing').getOrCreate()
        self.hbase_table_name = hbase_table_name

    def process_data(self):
        clickstream_data = self.spark.read.format('hbase').option('table', self.hbase_table_name).load()
        aggregated_data = clickstream_data.groupBy('click_data:url', 'geo_data:country').agg(
            countDistinct('click_data:user_id').alias('unique_users'),
            countDistinct('row_key').alias('clicks'),
            avg('click_data:timestamp').alias('average_time_spent')
        )
        return aggregated_data
