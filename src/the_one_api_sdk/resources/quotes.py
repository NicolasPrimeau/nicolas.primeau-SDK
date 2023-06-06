from the_one_api_sdk import request
from the_one_api_sdk.resources import base, adapters
from the_one_api_sdk.config import SdkConfig


class QuoteRequest(request.ResourceRequest):
    def __init__(self, config: SdkConfig, quote_id: str):
        super().__init__(config)
        self._quote_id = quote_id

    @property
    def path(self) -> str:
        return f"quote/{self._quote_id}"

    @property
    def adapter(self):
        return adapters.QuoteResponseAdapter()


class QuoteListRequest(request.ResourceListRequest[base.Quote]):
    def __init__(self, config: SdkConfig, movie_id: str = None):
        super().__init__(config)
        self._movie_id = movie_id

    @property
    def path(self) -> str:
        if not self._movie_id:
            return "quote"
        else:
            return f"movie/{self._movie_id}/quote"

    @property
    def adapter(self):
        return adapters.QuoteResponseAdapter()


class QuotesRequest:
    def __init__(self, config: SdkConfig):
        self.config = config

    def __call__(self, quote_id: str):
        return QuoteRequest(self.config, quote_id)

    def list(self, **kwargs) -> QuoteListRequest:
        return QuoteListRequest(self.config, **kwargs)
