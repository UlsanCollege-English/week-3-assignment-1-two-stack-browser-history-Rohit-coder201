
### /src/history.py (starter)

class BrowserHistory:
    def __init__(self, start="home"):
        # TODO: choose your internal representation (two stacks)
        self._cur = start
        self._back = []   # TODO
        self._fwd = []    # TODO

    def visit(self, url: str) -> None:
        # TODO: push current to back, set current, clear forward
        raise NotImplementedError

    def back(self) -> str:
        # TODO: move to previous page; decide error behavior on underflow
        raise NotImplementedError

    def forward(self) -> str:
        # TODO: move to next page; decide error behavior on underflow
        raise NotImplementedError

    def current(self) -> str:
        return self._cur
