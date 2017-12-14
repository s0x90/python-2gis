# -*- coding: utf-8 -*-


class DgisError(Exception):
    """2Gis API error"""

    def __init__(self, code, error, api_version):
        self.code = code
        self.error = error
        self.api_version = api_version

    def __str__(self):
        return self.error
