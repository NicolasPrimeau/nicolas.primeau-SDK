import json
import unittest

from test import utils
from the_one_api_sdk.components import base
from the_one_api_sdk.resources.quotes import QuoteListRequest, QuoteRequest
from the_one_api_sdk.config import SdkConfig
from the_one_api_sdk.resources.base import Quote


class QuoteListRequestTest(unittest.TestCase):
    def test_list_quotes(self):
        config = SdkConfig(client=utils.MockClient(
            responses=[
                base.Response(
                    request=None,
                    content=json.dumps({
                        "docs": [
                            {"_id": "a", "dialog": "test"},
                            {"_id": "b", "dialog": "test2"}
                        ]
                    }),
                    status_code=200
                ),
                base.Response(
                    request=None,
                    content=json.dumps({
                        "docs": [
                            {"_id": "c", "dialog": "test3"},
                            {"_id": "d", "dialog": "test4"}
                        ]
                    }),
                    status_code=200
                ),
                base.Response(
                    request=None,
                    content=json.dumps({"docs": []}),
                    status_code=200
                )
            ]
        ))
        quote_list = QuoteListRequest(config).fetch()
        self.assertEquals(quote_list, [
            Quote(quote_id="a", dialog="test"),
            Quote(quote_id="b", dialog="test2"),
            Quote(quote_id="c", dialog="test3"),
            Quote(quote_id="d", dialog="test4")
        ])


class QuoteRequestTest(unittest.TestCase):
    def test_get_quote(self):
        config = SdkConfig(client=utils.MockClient(
            responses=[base.Response(
                request=None, content=json.dumps({"docs": [{"_id": "a", "dialog": "test"}]}), status_code=200
            )]
        ))
        quote = QuoteRequest(config, "a").fetch()
        self.assertEquals(quote, Quote(quote_id="a", dialog="test"))
