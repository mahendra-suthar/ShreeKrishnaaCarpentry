from elasticsearch import Elasticsearch, helpers
from datetime import datetime
import bson
import json

elastic = Elasticsearch('http://192.168.1.105:9200', http_auth=('elastic','elastic@pb1'))
print("--------elas",elastic)


# index=elastic.index(index="dfg-index", id=1, body={"name": "mahe", "timestamp": datetime.now()})
# print(index)
# get = elastic.get(index="dfg-index", id=1)['found']
# print(get)
# elastic.indices.create(index='dfg-index', ignore=400)
# elastic.get(index="employee",id=)['_source']

def generate_uuid():
    return str(bson.ObjectId())


data1 = {
            "name":"john",
            "age":38,
            "cars":"bmw",     
        }
data2 = {
            "name":"john",
            "age":15,
            "cars":"suzuki"
        }
index = elastic.index(index='employee',id=generate_uuid(), body=data1)
print('Inserted',index['result'])
index = elastic.index(index='employee', id=generate_uuid(), body=data2)
print('Inserted',index['result'])



# def insert_data(obj):
#     result = []
#     json_file =  open('employee.json', 'r')
#     print("-------------json",json_file)
#     for line in open('employee.json', 'r'):
#         print('ggdf',line)
#         doc = json.loads(line)
#         print('ggdf')
#         data_ = dict()
#         data_["_id"] = generate_uuid()
#         data_["_index"] = obj
#         data_["_source"] = doc
#         result.append(data_)
#         print('ggdf')
#     helpers.bulk(elastic, result)

# insert_data('employee')


