#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class CreateKeyPairRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cvm', 'qcloudcliV1', 'CreateKeyPair', 'cvm.api.qcloud.com')

	def get_keyName(self):
		return self.get_params().get('keyName')

	def set_keyName(self, keyName):
		self.add_param('keyName', keyName)

