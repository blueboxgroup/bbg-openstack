# -*- coding: utf-8 -*-
#
# Copyright © 2015 Blue Box Group, LLC
# Author: Craig Tracey <craigtracey@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from bbg_openstack.middleware.ssl import SSLMiddlewareMixin
from nova import wsgi


class NovaSSLMiddleware(SSLMiddlewareMixin, wsgi.Middleware):

    @staticmethod
    def factory(global_conf):
        def filter(app):
            return NovaSSLMiddleware(app)
        return filter

    def __init__(self, application):
        SSLMiddlewareMixin.__init__(self)
        wsgi.Middleware.__init__(self, application)
