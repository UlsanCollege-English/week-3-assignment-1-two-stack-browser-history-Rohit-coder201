
class BrowserHistory:
    def __init__(self, start="home"):
        self.cur = start
        self.back_stack = []
        self.fwd_stack = []

    def visit(self, url):
        if self.cur != "home" or self.back_stack or self.fwd_stack:
            self.back_stack.append(self.cur)
        self.cur = url
        self.fwd_stack.clear()

    def back(self):
        if not self.back_stack:
            raise IndexError("No pages in back history")
        self.fwd_stack.append(self.cur)
        self.cur = self.back_stack.pop()
        return self.cur

    def forward(self):
        if not self.fwd_stack:
            raise IndexError("No pages in forward history")
        self.back_stack.append(self.cur)
        self.cur = self.fwd_stack.pop()
        return self.cur

    def current(self):
        return self.cur