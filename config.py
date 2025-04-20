#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os
from pymongo import MongoClient

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7705829246:AAGkrOC-1RiFyhqndeuva45RIbUGs54HfRI")
    API_ID = int(os.environ["API_ID", 23454876]
    API_HASH = os.environ["API_HASH", "b42626ee535fcaf915232af564a95bea"]
    AUTH_USERS = "662494886"
    MONGO_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://saik:F@v@NHpt@7TFAb9@cluster0.brflswq.mongodb.net/?retryWrites=true&w=majority")
    
