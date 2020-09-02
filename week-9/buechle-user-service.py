#
# ======================================================
# Title:  – Querying and Creating Documents
# Author: Professor Itskovich
# Modified by: Becca Buechle
# Date:   8-31-2020
# Description: Assignment 9.2 Python
#=====================================================
#

from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost', 27017)

db = client.web335

user = {

    "first_name": "Becca",

    "last_name": "Buechle",

    "email": "rbuechle@tree.com",

    "employee_id": "0000100",

    "date_created": datetime.datetime.utcnow()

}

user_id = db.users.insert_one(user).inserted_id

print(user_id)

pprint.pprint(db.users.find_one({"employee_id": "0000100"}))