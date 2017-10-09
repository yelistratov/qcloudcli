#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DeprecateProductRequest(Request):

	def __init__(self):
		Request.__init__(self, 'iiot', 'qcloudcliV1', 'DeprecateProduct', 'iiot.api.qcloud.com')

	def get_undoDeprecate(self):
		return self.get_params().get('undoDeprecate')

	def set_undoDeprecate(self, undoDeprecate):
		self.add_param('undoDeprecate', undoDeprecate)

	def get_productName(self):
		return self.get_params().get('productName')

	def set_productName(self, productName):
		self.add_param('productName', productName)

	def get_undoDeprecate(self):
		return self.get_params().get('undoDeprecate')

	def set_undoDeprecate(self, undoDeprecate):
		self.add_param('undoDeprecate', undoDeprecate)

	def get_productName(self):
		return self.get_params().get('productName')

	def set_productName(self, productName):
		self.add_param('productName', productName)

