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

# Queries workload

1. Given a list of topics (tags), find the question easiest to answer in each topic. We measure easiness using the time it took to receive an accepted answer. The
shorter the time, the easier the question. For instance, the question easiest to answer in topic ‘neural-networks’ is question with id 1: What is ‘‘backprop’’?. The
question was posted on 2016-08-02T15:39:14 and received an accepted answer on 2016-08-02T15:40:24. It took only a little over 1 minute to receive an accepted answer.

2. Assuming each tag represents a topic, find the most viewed question in a given topic.

3. Given a list of topics (tags), find the question easiest to answer in each topic. We measure easiness using the time it took to receive an accepted answer. The shorter the time, the easier the question. For instance, the question easiest to answer in topic ‘neural-networks’ is question with id 1: What is ‘‘backprop’’?. The question was posted on 2016-08-02T15:39:14 and received an accepted answer on 2016-08-02T15:40:24. It took only a little over 1 minute to receive an accepted answer.

4. Given a time period as indicated by starting and ending date, find the top 5 topics in that period. We rank a topic by the number of users that has either posted a question in that topic or has answered a question in that topic. This would help us to understand the trending topics in different periods of time.

5. Given a topic, find the champion user and all questions the user has answers accepted in that topic. We define a champion user as the one who has the most answers accepted in a given topic. For instance, the champion user of topic ‘deep-learning’ is 4398 and 1847. Both users have 9 answers being accepted in this topic. Your result may show either of the two users.

6. Some question may have been posted for a period of time but may not have an accepted answers yet. We refer to such question as unanswered question. We would like to recommend unanswered questions to potential answerers. For any user with n answers accepted in a certain topic with n greater than or equal to a threshold value , we consider the user a potential answerer of unanswered questions in that topic. For instance, given a user with id 4398, an  value 4 and a cutoff date of question creation as 2018-08-30T00:00:00. We will find user 4398 is a potential answerer in the following topics: reinforcement-learning, deep-learning, machine-learning and ai-design. The user has 10 answers accepted in reinforcement-learning area, 9 in deeplearning area, 5 in machine-learning area and 4 in ai-design area.

7. Users can give upVote to both question and answer. Usually the accepted answer of a question receives the highest number of upVote among all answers of this question.
In rare case, another answer(s) may receive higher upVote count than the upVotecount of the accepted answer. In this query, you are asked to discover such questions
whose accepted answer has less upVote count than the upVote count of one of its other answers. Note We are only interested in questions with upVote count greater than a given threshold value . With high  value, you are likely to get an empty set as the result. A reasonable  value would be between 5-15.

8. Discover the top five coauthors of a given user.Consider all users involved in a question as co-authors, for a given user, we rank the coauthors by the number of questions this user and the coauthor appear together either as originator or answerer. For instance, user 4398 has the following top co-authors: 1671(5), 11571(4), 9161(4), 4302(3) and 6019(3). User 4398 and user 1671 appeared together in five questions; user 4398 and user 1571 appeared together in 4 questions. Your result should include both the user id and the number of questions the pair appeared together (co-authored).

# Dataset 
The dataset that we use is the latest dump (publication date: 2018-06-05) of the Artificial Intelligence Stack Exchange question and answer site (https://ai.stackexchange.
com/). The dump is released and maintained by stackexchange: https://archive.org/details/stackexchange. The original dump contains many files in XML format. This project 
uses a subset of the data stored in four tsv files. 
The dataset contains the following files:
• Posts.tsv stores information about post, each row represents a post, which could be a question or an answer
• Users.tsv stores user’s profile, each row represents a user
• Votes.tsv stores detailed vote information about post, each row represents a vote,
including the vote type, the date this vote is made and a few other information
• Tags.tsv contains summary of tag usage in this site.

# Schema design in MongoDB example

![image](https://github.com/FredericChai/NoSQl_Data_Model/blob/master/src/1.jpg)

Posts collection: It contains both question and answer which would be identified by PostTypeId.
Question collection: the dataset would be identified as question if PostTypeId is 1, which contains id(string), PostTypeId(string), AcceptAnswerId(string), CreationDate(date), ViewCount(int), OwnerUserId(string), Title(string), Tags(string). Id would be identified as Primary key and AcceptAnswerId would be DBRefs reference to answer collection; OwneruserId would be DBRefs reference to Users collection; Tags would be DBRefs reference to Tags collection. 
Answer collection: the dataset would be identified as question if PostTypeId is 2, which contains id(string), PostTypeId(string), ParentId(string), CreationDate(date), OwnerUserId(string), Tags(string). Id would be identified as Primary key and ParentId would be DBRefs reference to question collection; OwneruserId would be DBRefs reference to Users collection; Tags would be f DBRefs reference to Tags collection.  2)Topic collection is evolved from tags collection, containing _id and question.

# Schema design in Neo4j example
![image](https://github.com/FredericChai/NoSQl_Data_Model/blob/master/src/2.jpg)

Posts nodes are divided into two parts as question and answer, judging by PostTypeId, which is designed to be suitable for the questions. The relationships between two nodes contain: 1.belong: question and answer are belonged to each other, which is matched by ParentId of answer and Id of the question; 2.accept: it represents the answer which is accepted and this would be matched by AcceptAnswerId. 2) Users nodes mean the end users of this website who may have pointed out questions or gave answers to questions. In that case, the relationship between users and posts should correspond as Questioned or Answered. 3)For Votes node, it means the vote to question or answer. The relationship is Voted which matched to two types of posts, identifying by PostId.4)Tags means the tag of the question and the relationships between question、answer and tags is have. ( ps: Additionally, tags are connected into the answer node manually, for comparing neo4j with MongoDB in Aq2, as performance comparing. However, this relationship would not be shown in schema designed for the query workload)
To improve the performance and efficiency of code execution, there is four indexes need to be created: 1)PostTypeId、2)VoteTypeId、3)VoteVoteTypeId


# Query Performance comparison
 
|  Query | MongoDB (ms) | Neo4j (ms) |
|:--------------:|:----------------:|:----------------:|
| 1|  1.66   | 2.06  |
| 2  | 3.25 |	4.75 |
| 3  | 6.51	| 27.7 |
| 4  | 2.29	| 19 |
| 5  | 33.4	| 25 |
| 6  | 70.8	| 19.8 |
| 7  |  N/A	| 33.1 |
| 8  | 15.6	| 3.19 |



# Query excution example

![image](https://github.com/FredericChai/NoSQl_Data_Model/blob/master/src/3.jpg)

![image](https://github.com/FredericChai/NoSQl_Data_Model/blob/master/src/5.png)

![image](https://github.com/FredericChai/NoSQl_Data_Model/blob/master/src/4.png)

Details for query was stored in report


