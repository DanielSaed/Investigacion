from hmac import new
from logging.config import valid_ident
from msilib import PID_TITLE
from pydoc import doc
from azure.cosmos import CosmosClient
from azure.cosmos.partition_key import PartitionKey
import uuid
import json
from pandas import DataFrame

URL = 'https://localhost:8081'
KEY = ''
client = CosmosClient(URL, credential=KEY)
DATABASE_NAME = 'DataSet'
database = client.get_database_client(DATABASE_NAME)
CONTAINER_NAME = 'RutaAviones'
container = database.get_container_client(CONTAINER_NAME)


def read_item(doc_id):
    print('\n1.2 Reading Item by Id\n')
    # Note that Reads require a partition key to be specified.
    response = container.read_item(item=doc_id, partition_key=doc_id)
    print(response)

def get_items(key,value):
    query = list(container.query_items(query="SELECT * FROM c WHERE c.%s = '%s'" %(key,value), enable_cross_partition_query=True, populate_query_metrics=True))
    print(query)
    for item in query:
        #print(json.dumps(item, indent=True))
        dic = json.dumps(item, indent=True)
    #return item

def get_items1():
    query = list(container.query_items(query="SELECT * FROM c WHERE c.TaxiIn = '27'", enable_cross_partition_query=True, populate_query_metrics=True))
    query.QueryMetrics
    
    for item in query:
        #print(json.dumps(item, indent=True))
        dic = json.dumps(item, indent=True)
        

def delete_items():
    for item in container.query_items(query="SELECT * FROM c ",enable_cross_partition_query=True):
        id = item['_id']
        container.delete_item(item, partition_key=id)
    return "Datos eliminados"

def insert_items(ruta):
    f = open(ruta)
    data = json.load(f)
    for item in data:
        #Assign id to the item
        item['id'] = item['_id']
        container.create_item(body=item) 
    f.close()
    return "Datos insertados"

def update_items(key,value,id):
    item = get_items('_id',id)
    item[key] = value
    container.upsert_item(item)
    return "Datos actualizados"

#insert_items('C:\\Users\\admin\\Desktop\\Aviones2007.json')
#update_items()
get_items1()
#get_items('_id','2')
#delete_items()
#read_item("1")


