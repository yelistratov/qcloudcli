# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyEipAttributesRequest(Request):

    def __init__(self):
        super(ModifyEipAttributesRequest, self).__init__(
            'eip', 'qcloudcliV1', 'ModifyEipAttributes', 'eip.api.qcloud.com')

    def get_eipId(self):
        return self.get_params().get('eipId')

    def set_eipId(self, eipId):
        self.add_param('eipId', eipId)

    def get_eipName(self):
        return self.get_params().get('eipName')

    def set_eipName(self, eipName):
        self.add_param('eipName', eipName)
