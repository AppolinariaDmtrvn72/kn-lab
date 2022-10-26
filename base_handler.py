from typing import Any, Union


class BaseHandler:
    def __init__(self, model):
        self._model = model

    def score(self, pic) -> Any:
        return 0
