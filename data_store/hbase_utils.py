import happybase

class HBaseUtils:
    def __init__(self, host, port, table_name):
        self.connection = happybase.Connection(host, port=port)
        self.table = self.connection.table(table_name)

    def store_data(self, row_key, click_data, geo_data, user_agent_data):
        self.table.put(row_key, {
            'click_data:user_id': click_data['user_id'],
            'click_data:timestamp': click_data['timestamp'],
            'click_data:url': click_data['url'],
            'geo_data:country': geo_data['country'],
            'geo_data:city': geo_data['city'],
            'user_agent_data:browser': user_agent_data['browser'],
            'user_agent_data:os': user_agent_data['os'],
            'user_agent_data:device': user_agent_data['device']
        })
