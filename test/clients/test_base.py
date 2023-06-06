import unittest

from the_one_api_sdk.clients import base


class RequestTest(unittest.TestCase):
    def test_full_url_with_path(self):
        request = base.Request(url="http://something", path="folder", method=base.HttpMethods.GET)
        self.assertEquals(request.full_url, "http://something/folder")

    def test_full_url_no_path(self):
        request = base.Request(url="http://something", method=base.HttpMethods.GET)
        self.assertEquals(request.full_url, "http://something")
