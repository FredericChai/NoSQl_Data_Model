from pymongo import MongoClient

class MDBconnector:

  #initialize the mongoDB settings parameter
    def __init__(self,hostname,port,db_name):
        self._db = MongoClient(hostname, port)[db_name]
  #get the collection by name
    def get_collection(self,collection_name):
        self._collection = self._db[collection_name]
        return self._collection

    # def query_sq1(collection_name):
    #     collection = connection.get_collection(collection_name).find()
    #     return collection['AllAnswerOwner']

    def query_find(self,collection_name):
        self._collection = self._db[collection_name].find()
