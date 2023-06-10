from pymongo import MongoClient
from pandas import DataFrame
import time
import json
from time import process_time_ns
import time
#print(time.time_ns())


start_time = time.time_ns()


CONNECTION_STRING = "mongodb+srv://danielsaed99:031099@cluster0.k8ed7vw.mongodb.net/test"
client = MongoClient(CONNECTION_STRING)
dbname = client['checobot']
collection_name = dbname["fechas"]

def get_item(key,value):
    #start_time = time.time()
   
    item_details = collection_name.find_one({key: value})
    #do some stuff
    #finish_time = (time.time()) - start_time 
    
    
    result = item_details
    print(result)
    return result

def insert_items(ruta):
    f = open(ruta)
    data = json.load(f)
    start_time = time.time()
    for i in data:
        collection_name.insert_one(i)
    finish_time = (time.time()) -start_time 
    print(finish_time)
    f.close()
    return "Datos insertados"

def delete_items():
    
    start_time = time.time()
    collection_name.delete_many({})
    finish_time = (time.time()) -start_time 
    print(finish_time)
    return "Datos eliminados"

def update_items():
    start_time = time.time()
    collection_name.update_many({},{"$set":{"city":"Visakhapatnam"}})
    finish_time = (time.time()) -start_time 
    print(finish_time)
    return "Datos actualizados"

#insert_items('C:\\Users\\admin\\Desktop\\Peliculas.json')
#delete_items()
#print(get_item("CRSDepTime","1040"))

get_item("id","1")