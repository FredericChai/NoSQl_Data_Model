import json
import csv


def transTags(path):
    # create json file
    jsonfile = open('Tags.json', 'w')
    # variable to store components
    bucket = []
    with open(path) as tsvfile:
        tsvfile = csv.reader(tsvfile, delimiter='\t')
        next(tsvfile)
        for row in tsvfile:
            # row[0] = Id
            # row[1] = Tagname
            # row[2] = Count
            # row[3] = ExcerptPostId
            # row[4] = WikiPostId
            # 拼装语句
            temp = {'Id': row[0], 'Tagname': row[1], 'Count': row[2], 'ExcerptPostId': row[3], 'WikiPostId': row[4]}
            bucket.append(temp)
    # write
    json.dump(bucket, jsonfile, sort_keys=False, indent=4, separators=(',', ': '))

def transPosts(path):
    # create json file
    jsonfile = open('Posts.json', 'w')
    # variable to store components
    bucket = []
    with open(path) as tsvfile:
        tsvfile = csv.reader(tsvfile, delimiter='\t')
        next(tsvfile)
        for row in tsvfile:
            # 拼装语句
            temp = {'Id': row[0], 'PostTypeId': row[1], 'AcceptedAnswerId': row[2], 'CreationDate': row[3],
                    'Score': row[4], 'ViewCount': row[5], 'OwnerUserId': row[6], 'Title': row[7], 'Tags': row[8],
                    'AnswerCount': row[9], 'TaCommentCountgs': row[10], 'FavoriteCount': row[11], 'ParentId': row[12],
                    'ClosedDate': row[13], 'OwnerDisplayName': row[14]}
            bucket.append(temp)
    # write
    json.dump(bucket, jsonfile, sort_keys=False, indent=4, separators=(',', ': '))

def transUsers(path):
    # create json file
    jsonfile = open('Users.json', 'w')
    # variable to store components
    bucket = []
    with open(path) as tsvfile:
        tsvfile = csv.reader(tsvfile, delimiter='\t')
        next(tsvfile)
        for row in tsvfile:
            # 拼装语句
            temp = {'Id': row[0], 'Reputation': row[1], 'CreationDate': row[2], 'DisplayName': row[3],
                    'LastAccessDate': row[4], 'Location': row[5], 'Views': row[6], 'UpVotes': row[7],
                    'DownVotes': row[8]}
            bucket.append(temp)
    # write
    json.dump(bucket, jsonfile, sort_keys=False, indent=4, separators=(',', ': '))

def transVotes(path):
    # create json file
    jsonfile = open('Votes.json', 'w')
    # variable to store components
    bucket = []
    with open(path) as tsvfile:
        tsvfile = csv.reader(tsvfile, delimiter='\t')
        next(tsvfile)
        for row in tsvfile:
            # 拼装语句
            temp = {'Id': row[0], 'PostId': row[1], 'VoteTypeId': row[2], 'CreationDate': row[3],
                    'UserId': row[4], 'BountyAmount': row[5]}
            bucket.append(temp)
    # write
    json.dump(bucket, jsonfile, sort_keys=False, indent=4, separators=(',', ': '))

transPosts('/Users/chaizhizhi/Desktop/5338 data/Posts.tsv')
transUsers('/Users/chaizhizhi/Desktop/5338 data/Users.tsv')
transVotes('/Users/chaizhizhi/Desktop/5338 data/Votes.tsv')