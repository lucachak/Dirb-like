"""
main entry point/ execution of code, as it seems to not be that big, i dont think i'll need much more
"""

import sys
import http.client
from classes.Helper import Helper
from classes.ConnectionHandler import ConnectionHandler


def main() -> None:
    conn = ConnectionHandler( http.client.HTTPConnection, "http://localhost:1000/")

if __name__ == "__main__":
    main()  
