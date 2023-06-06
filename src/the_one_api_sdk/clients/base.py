import dataclasses
import json
from typing import Optional, Dict

from the_one_api_sdk import utils


class HttpMethods(utils.StrEnum):
    GET = "GET"
    POST = "POST"


@dataclasses.dataclass
class Request:
    url: str
    path: str
    method: str
    headers: Optional[Dict[str, str]] = dataclasses.field(default_factory=dict)
    query_params: Optional[Dict[str, str]] = dataclasses.field(default_factory=dict)
    body: Optional[str] = None

    def add_query_param(self, key: str, value):
        self.query_params[key] = str(value)

    @property
    def full_url(self) -> str:
        return f"{self.url.rstrip('/')}/{self.path.lstrip('/')}"


@dataclasses.dataclass
class Response:
    request: Request
    status_code: int
    headers: Optional[Dict[str, str]] = dataclasses.field(default_factory=dict)
    content: Optional[str] = None

    def to_json(self):
        return json.loads(self.content)