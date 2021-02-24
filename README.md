# NoSQl_Data_Model
This repo provide the code for NoSQL schema design and query workload implementation. It was designed based on MongoDB and Neo4j.

To run the query on mongoDB, you need to install the jupyter notebook, python and PyMongo at fitst. Then after using the 1_convertTSV.ipynb create three data file in Jason format, you can follow the code in another three  txt file to modify the data, structure and create the index. At last, you can run QueryCode.ipynb file to execute the query. 

There are some sample result already contained in the QueryCode.ipynb file. The execution source code of Neo4j are saved in the Neo4j file. Please run the code in convertTsv.ipynb, Neo4j_schema_design. Then copy the code in query_shell_code and run it on Neo4j browser. 

# Overview comparison between MongoDB and Neo4j
|      | MongoDB | Neo4j |
|:--------------:|:----------------:|:----------------:|
| Description|  General Database    | Graph Database  |
| Primary Database Model| Document store | Graph DBMS|
| Data Schema|  Schema-free | Schema-free/Schema-optional |
| Features | good index, fast query,support javascript | fast graph query based on relation, can be embedded into java program|


# Schema design in MongoDB

