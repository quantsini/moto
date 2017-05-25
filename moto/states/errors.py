from __future__ import unicode_literals

from moto.core.exceptions import JsonRESTError


class StatesClientError(JsonRESTError):
    code = 400

