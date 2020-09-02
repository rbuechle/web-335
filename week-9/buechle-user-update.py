#
# ======================================================
# Title:  – Updating and deleting docs 
# Author: Professor Itskovich
# Modified by: Becca Buechle
# Date:   8-31-2020
# Description: Assignment 9.3 Python
#=====================================================
#

from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost', 27017)

db = client.web335

db.users.update_one(

    {"employee_id": "0000100"},

    {

        "$set": {

            "email": "rbuechle@my365.bellevue.edu"

        }

    }

)

pprint.pprint(db.users.find_one({"employee_id": "0000100"}))