# classes/URLBuilder.py


class URLBuilder:
    def __init__(self, base: str, endpoint_list: list[str]):
        self.base = base.rstrip("/")
        self.words = endpoint_list

    def get_built_urls(self):
        return [f"{self.base}/{w}" for w in self.words if w.strip()]
