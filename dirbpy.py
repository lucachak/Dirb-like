"""
main entry point/ execution of code, as it seems to not be that big, i dont think i'll need much more
"""
import os
from classes.ConnectionHandler import ConnectionHandler

def get_wordlist()



def main() -> None:

    url = 'http://127.0.0.1:8000/Api/products/'

    conn = ConnectionHandler(
            url=url
            )


    conn.connect()

if __name__ == "__main__":
    main()  
