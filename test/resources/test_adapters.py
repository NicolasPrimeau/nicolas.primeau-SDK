import unittest

from the_one_api_sdk.resources.adapters import MovieResponseAdapter, QuoteResponseAdapter
from the_one_api_sdk.resources.base import Movie, Quote


class MovieResponseAdapterTest(unittest.TestCase):
    def test_adapter(self):
        adapter = MovieResponseAdapter()
        resource = adapter.convert_to_resource({
            "_id": "a",
            "name": "test",
            "runtimeInMinutes": 1,
            "budgetInMillions": 2,
            "boxOfficeRevenueInMillions": 3,
            "academyAwardNominations": 4,
            "academyAwardWins": 5,
            "rottenTomatoesScore": 6
        })
        self.assertEquals(resource, Movie(
            movie_id="a",
            name="test",
            runtimeInMinutes=1,
            budgetInMillions=2,
            boxOfficeRevenueInMillions=3,
            academyAwardNominations=4,
            academyAwardWins=5,
            rottenTomatoesScore=6
        ))


class QuoteResponseAdapterTest(unittest.TestCase):
    def test_adapter(self):
        adapter = QuoteResponseAdapter()
        resource = adapter.convert_to_resource({
            "_id": "a",
            "dialog": "test",
            "character": "b",
            "movie": "d"
        })
        self.assertEquals(resource, Quote(
            movie_id="d",
            quote_id="a",
            character_id="b",
            dialog="test",
        ))
