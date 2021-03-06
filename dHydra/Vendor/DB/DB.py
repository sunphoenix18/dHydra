# -*- coding: utf-8 -*-
"""
# Created on
# @author:
# @contact:
"""
# 以下是自动生成的 #
# --- 导入系统配置
import dHydra.core.util as util
from dHydra.core.Vendor import Vendor
from dHydra.config import connection as CON
from dHydra.config import const as C
# --- 导入自定义配置
from .connection import *
from .const import *
from .config import *
# 以上是自动生成的 #

from pymongo import MongoClient
import redis

class DB(Vendor):
	def __init__(self):
		super().__init__()

	def get_mongodb(self, host = "localhost", port = 27017, timeout = 1500):
		try:
			self.logger.info("尝试连接到Mongodb")
			client = MongoClient(host=host,port=port,serverSelectionTimeoutMS=timeout)
			client.server_info()
			self.logger.info("已经成功连接到mongodb")
			return client
		except:
			self.logger.warning(">>>>>>>>>>>>>>>>>>连接到mongodb失败<<<<<<<<<<<<<<<<<<<")
			return False

	def get_redis(self, host="127.0.0.1", port = 6379):
		try:
			self.logger.info("Trying to connect to redis")
			self.redis = redis.StrictRedis(decode_responses = True, host = host, port = port)
			self.redis.client_list()
			return self.redis
		except:
			self.logger.warning("Failed to connect to redis")
			return False
