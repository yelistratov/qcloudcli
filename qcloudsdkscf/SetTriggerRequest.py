# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class SetTriggerRequest(Request):

    def __init__(self):
        super(SetTriggerRequest, self).__init__(
            'scf', 'qcloudcliV1', 'SetTrigger', 'scf.api.qcloud.com')

    def get_functionName(self):
        return self.get_params().get('functionName')

    def set_functionName(self, functionName):
        self.add_param('functionName', functionName)

    def get_newTriggerName(self):
        return self.get_params().get('newTriggerName')

    def set_newTriggerName(self, newTriggerName):
        self.add_param('newTriggerName', newTriggerName)

    def get_triggerDesc(self):
        return self.get_params().get('triggerDesc')

    def set_triggerDesc(self, triggerDesc):
        self.add_param('triggerDesc', triggerDesc)

    def get_triggerName(self):
        return self.get_params().get('triggerName')

    def set_triggerName(self, triggerName):
        self.add_param('triggerName', triggerName)

    def get_type(self):
        return self.get_params().get('type')

    def set_type(self, type):
        self.add_param('type', type)
