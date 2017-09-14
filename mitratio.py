import collections
import json
import ast
import requests
import pymongo
from pymongo import MongoClient
import unicodedata
from unidecode import unidecode
from ast import literal_eval
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pprint

client = MongoClient('mongodb://ec2-34-203-200-197.compute-1.amazonaws.com:27017')
db=client.appcreator_dev
collection =db.projects
agg = [{ "$group": {"_id": "$totalmonth","total": { "$sum": "$solar_radius" } }}]
pprint.pprint(list(collection.aggregate(agg)))
collections = db.wordcloud_copy
collections.insert(collection.aggregate(agg))
