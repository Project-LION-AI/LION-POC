import os
import psycopg2
import psycopg2.extras
import pandas as pd
from queries import get_messages
import sys
sys.path.insert(0, '/Users/kennycavanagh/Desktop/files/lab/repositories/lion/cfg')
from sql_config import Config 



class postgres():
    '''
    Load config variables, status variables, gm messages and intents
    '''
    config = Config()
    
    #connection object
    conn = psycopg2.connect(
        host=config['host'],
        database=config['database'],
        user=config['user'],
        password=config['password'],
        sslmode=config['sslmode'],
        port=config['port']
    )

    #get dataframe from query
    def get_dataframe(self, query):
        df = pd.read_sql_query(query, self.conn)
        return df



# msg_df = postgres().get_dataframe(get_messages)

# print(msg_df)