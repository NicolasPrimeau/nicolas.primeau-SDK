from typing import List

from the_one_api_sdk.clients import client, base


class MockClient(client.Client):
    def __init__(self, responses: List[base.Response]):
        self.responses = responses

    def get_response(self, request: base.Request) -> base.Response:
        response = self.responses.pop(0)
        response.request = request
        return response
