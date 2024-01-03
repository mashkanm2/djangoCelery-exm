
import psycopg2
from psycopg2 import sql
from django.conf import settings



class PostgresDBConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # # Connect to the PostgreSQL database
            cls._instance.kwconn={"dbname":settings.DATABASEPSQL['dbname'],
                "user":settings.DATABASEPSQL['user'],
                "password":settings.DATABASEPSQL['password'],
                "host":settings.DATABASEPSQL['host'],
                "port":settings.DATABASEPSQL['port']}
            # cls._instance.conn = psycopg2.connect(
            #     dbname=settings.DATABASEPSQL['dbname'],
            #     user=settings.DATABASEPSQL['user'],
            #     password=settings.DATABASEPSQL['password'],
            #     host=settings.DATABASEPSQL['host'],
            #     port=settings.DATABASEPSQL['port']
            # )

        return cls._instance
    
    def __init__(self):
        # Create DB if not exist
        db_name = settings.DATABASEPSQL['dbname']
        conn = psycopg2.connect(database="postgres", 
                                user=settings.DATABASEPSQL['user'], 
                                password=settings.DATABASEPSQL['password'], 
                                host=settings.DATABASEPSQL['host'], 
                                port=settings.DATABASEPSQL['port'])
        
        cursor = conn.cursor()
        cursor.execute("SELECT datname FROM pg_database;")
        rows = cursor.fetchall()
        if db_name in [row[0] for row in rows]:
            print(f"Database {db_name} already exists.")
        else:
            cursor = conn.cursor()
            cursor.execute(f"CREATE DATABASE {db_name};")
            print(f"Database {db_name} created successfully.")
        
    
    def createTable(self,table_name='',schema=None):
        '''
        input : dict {user_session: 
                    company:
                    currentValue:
                    countUser:
                    lastValue:
                    saledValue:
                    onineValue:
                    onpayValue:
                    saledUserCount:
                    payedUserCount:
                    }
        '''
        db_name=settings.DATABASEPSQL['dbname']
        if schema is None:
            schema = "(id SERIAL PRIMARY KEY, \
                currentValue REAL,\
                countUser INTEGER,\
                lastValue REAL,\
                saledValue REAL,\
                onineValue REAL,\
                onpayValue REAL,\
                saledUserCount INTEGER,\
                payedUserCount INTEGER)"
            
        try:
            conn=psycopg2.connect(**self.kwconn)
        
            conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = conn.cursor()
            cursor.execute(f"SELECT datname FROM pg_database WHERE datname='{db_name}';")
            rows = cursor.fetchall()
            if len(rows) == 0:
                print(f"Database {db_name} does not exist.")
                raise ValueError('DB is not connected')
            conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} {schema};")
            print(f"Table {table_name} created successfully in database {db_name}.")
        except:
            print("ERROR: Failed to create Tabel {table_name}")
        finally:
            if (conn):
                # Close the cursor and connection
                cursor.close()
                conn.close()
        
    def getcount(self,cellection_name:str):
        count=0
        try:
            conn=psycopg2.connect(**self.kwconn)
            # create a cursor object
            cursor = conn.cursor()
            # execute a SELECT statement
            cursor.execute("SELECT COUNT(*) FROM "+cellection_name)
            # fetch all rows from the last executed statement using `fetchall` method
            records = cursor.fetchall()
            # print each row
            count=int(records[0])
        except:
            print("ERROR: Failed to SELECT data")
        finally:
            if (conn):
                # Close the cursor and connection
                cursor.close()
                conn.close()
        return count

    def save_data_to_db(self,data,cellection_name:str):
        cols_names='('
        values_=[]
        v_str="()"
        for k,v in data.items():
            cols_names=cols_names+str(k)+', '
            values_.append(str(v))
            v_str=v_str+"%s ,"
        cols_names=cols_names[:-2]+")"
        v_str=v_str[:-2]+")"
        
        try:
            conn=psycopg2.connect(**self.kwconn)
            # Create a cursor object
            cursor = conn.cursor()
            query_="INSERT INTO "+cellection_name+cols_names+" VALUES "+v_str
            # Define your SQL query to insert data
            # insert_query = sql.SQL("INSERT INTO your_table_name (column1, column2, column3) VALUES (%s, %s, %s)")
            insert_query = sql.SQL(query_)
            # Data to be inserted
            data_to_insert = tuple(values_)
            # Execute the query
            cursor.execute(insert_query, data_to_insert)
            # Commit the transaction
            conn.commit()
            
            print("Data saved successfully")
        except:
            print("ERROR: Failed to save data")
        finally:
            if (conn):
                # Close the cursor and connection
                cursor.close()
                conn.close()
            


    def get_data_from_db(self,cellection_name:str,limitV=100,ofcetV=0):
        try:
            conn=psycopg2.connect(**self.kwconn)
            # create a cursor object
            cursor = conn.cursor()
            # execute a SELECT statement
            cursor.execute("SELECT * FROM "+cellection_name+f"ORDER BY id DESC LIMIT {limitV} OFFSET {ofcetV}")
            # fetch all rows from the last executed statement using `fetchall` method
            records = cursor.fetchall()
            # print each row
            for record in records:
                print(record)
        except:
            print("ERROR: Failed to SELECT data")
        finally:
            if (conn):
                # Close the cursor and connection
                cursor.close()
                conn.close()


    def update_data_in_db(self,query, update_data,cellection_name:str):
        # collection = self.db[cellection_name]  

        # # Update the matching documents in the collection
        # result = collection.update_many(query, {'$set': update_data})

        # # Check if the update was successful
        # if result.modified_count > 0:
        #     return "Data updated successfully"
        # else:
        #     return "Failed to update data"
        # TODO: complete if need
        pass

    def delete_data_from_db(self,query,cellection_name:str):
        try:
            conn=psycopg2.connect(**self.kwconn)
            # Create a cursor object
            cursor = conn.cursor()
            query_="DELETE FROM "+ cellection_name+" WHERE "+query
            # Define your SQL query to delete data
            # delete_query = sql.SQL("DELETE FROM your_table_name WHERE column_name = %s")
            delete_query = sql.SQL(query_)
            # Data to be deleted
            # data_to_delete = ('value_to_delete',)
            # Execute the query
            cursor.execute(delete_query, ())
            # Commit the transaction
            conn.commit()
            print("Data deleted successfully")
        except:
            print("ERROR: Failed to delete data")
        finally:
            # close the cursor and connection to so the server can allocate bandwidth to other requests
            if (conn):
                cursor.close()
                conn.close()
                print("PostgreSQL connection is closed")













