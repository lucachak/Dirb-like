# classes/ConnectionHandler.py
import http.client as hc
import random
import time
from urllib.parse import urlparse


class ConnectionHandler:
    def __init__(self, url: str, wait: float = 0):
        self.scheme, self.host, self.port, self.path = self.url_parser(url)
        self.wait = wait

    def url_parser(self, url: str):
        p = urlparse(url)

        scheme = p.scheme
        host = p.hostname
        port = p.port or (80 if scheme == "http" else 443)
        path = p.path if p.path else "/"

        return scheme, host, port, path

    def connect(self):
        conn_cls = hc.HTTPConnection if self.scheme == "http" else hc.HTTPSConnection
        conn = conn_cls(self.host, self.port, timeout=4)

        try:
            conn.request("GET", self.path.replace(" ", "%20"))
            time.sleep(self.wait if self.wait > 0 else random.uniform(0.1, 0.5))

            resp = conn.getresponse()
            status = resp.status

            url = f"{self.scheme}://{self.host}:{self.port}{self.path}"

            return status, url

        finally:
            conn.close()

    @staticmethod
    def fetch(url: str):
        return ConnectionHandler(url).connect()
