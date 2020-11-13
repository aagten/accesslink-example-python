#!/usr/bin/env python

from .resource import Resource


class SleepData(Resource):

    def list(self, access_token):
        return self._get(endpoint="/users/sleep",
                         access_token=access_token)
