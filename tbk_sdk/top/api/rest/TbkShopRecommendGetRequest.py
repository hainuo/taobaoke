'''
Created by auto_sdk on 2018.07.25
'''
from ..base import RestApi
class TbkShopRecommendGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.count = None
		self.fields = None
		self.platform = None
		self.user_id = None

	def getapiname(self):
		return 'taobao.tbk_sdk.shop.recommend.get'
