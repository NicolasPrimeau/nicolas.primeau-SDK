import json
import unittest

from test import utils
from the_one_api_sdk.api import base
from the_one_api_sdk.api.movies import MovieListRequest, MovieRequest
from the_one_api_sdk.config import SdkConfig
from the_one_api_sdk.resources.base import Movie


class MovieListRequestTest(unittest.TestCase):
    def test_list_movies(self):
        config = SdkConfig(client=utils.MockClient(
            responses=[
                base.Response(
                    request=None,
                    content=json.dumps({
                        "docs": [
                            {"_id": "a", "name": "test"},
                            {"_id": "b", "name": "test2"}
                        ]
                    }),
                    status_code=200
                ),
                base.Response(
                    request=None,
                    content=json.dumps({
                        "docs": [
                            {"_id": "c", "name": "test3"},
                            {"_id": "d", "name": "test4"}
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
        movie_list = MovieListRequest(config).fetch()
        self.assertEquals(movie_list, [
            Movie(movie_id="a", name="test"),
            Movie(movie_id="b", name="test2"),
            Movie(movie_id="c", name="test3"),
            Movie(movie_id="d", name="test4")
        ])


class MovieRequestTest(unittest.TestCase):
    def test_get_movie(self):
        config = SdkConfig(client=utils.MockClient(
            responses=[base.Response(
                request=None, content=json.dumps({"docs": [{"_id": "a", "name": "test"}]}), status_code=200
            )]
        ))
        movie = MovieRequest(config, "a").fetch()
        self.assertEquals(movie, Movie(movie_id="a", name="test"))
