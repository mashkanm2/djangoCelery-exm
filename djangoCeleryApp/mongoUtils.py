

import pymongo
from django.conf import settings


class MongoDBConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Initialize the MongoDB client and database connection here
            cls._instance.client = pymongo.MongoClient(settings.DATABASEMONGO['host'])
            cls._instance.db = cls._instance.client[settings.DATABASEMONGO['dbname']]  
        return cls._instance

    def get_db(self):
        return self.db
    
    def getcount(self,cellection_name:str):
        collection = self.db[cellection_name] 
        # Get the count of documents in the collection
        count = collection.count_documents({})
        return count


    def save_data_to_db(self,data,cellection_name:str):
        collection = self.db[cellection_name]  

        # Insert the data into the collection
        result = collection.insert_one(data)

        # Check if the insertion was successful
        if result.acknowledged:
            return "Data saved successfully"
        else:
            return "Failed to save data"


    def get_data_from_db(self,cellection_name:str):
        collection = self.db[cellection_name]  

        # Retrieve all documents from the collection
        documents = collection.find()

        # Process the retrieved data
        for document in documents:
            # Handle each document as per your requirement
            print(document)


    def update_data_in_db(self,query, update_data,cellection_name:str):
        collection = self.db[cellection_name]  

        # Update the matching documents in the collection
        result = collection.update_many(query, {'$set': update_data})

        # Check if the update was successful
        if result.modified_count > 0:
            return "Data updated successfully"
        else:
            return "Failed to update data"

    def delete_data_from_db(self,query,cellection_name:str):
        collection = self.db[cellection_name]  
        # Delete the matching documents from the collection
        result = collection.delete_many(query)

        # Check if the deletion was successful
        if result.deleted_count > 0:
            return "Data deleted successfully"
        else:
            return "Failed to delete data"