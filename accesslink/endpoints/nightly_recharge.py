#!/usr/bin/env python

from .resource import Resource


class NightlyRecharge(Resource):

    def list(self, access_token):
        return self._get(endpoint="/users/nightly-recharge",
                         access_token=access_token)
