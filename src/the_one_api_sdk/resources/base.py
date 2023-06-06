import dataclasses
from typing import Optional


class Resource:
    pass


@dataclasses.dataclass
class Movie(Resource):
    movie_id: str
    name: str
    runtimeInMinutes: str
    budgetInMillions: int
    boxOfficeRevenueInMillions: int
    academyAwardNominations: int
    academyAwardWins: int
    rottenTomatoesScore: int


@dataclasses.dataclass
class Quote(Resource):
    quote_id: str
    dialog: str
    character_id: Optional[str] = None
    movie_id:  Optional[str] = None
