# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeletePolicyRequest(Request):

    def __init__(self):
        super(DeletePolicyRequest, self).__init__(
            'iothub', 'qcloudcliV1', 'DeletePolicy', 'iothub.api.qcloud.com')

    def get_policyName(self):
        return self.get_params().get('policyName')

    def set_policyName(self, policyName):
        self.add_param('policyName', policyName)
