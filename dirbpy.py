"""
main entry point/ execution of code, as it seems to not be that big, i dont think i'll need much more
"""
import os
from os.path import isfile
from classes.ConnectionHandler import ConnectionHandler
from classes.URLBuilder import URLBuilder

def get_wordlist(file:str="default.txt") -> list[str]:
    
    line = []

    wd_dir = os.path.join(
            os.getcwd(), "wordlist")
    file = os.path.join(
            wd_dir,file)

    if os.path.exists(file):
        with open(file, "r") as f:
            line = f.read().split("\n")

    else:
        raise LookupError()

    return line



def main() -> None:
    url_builder = URLBuilder(
            endpoint_list= get_wordlist()
            )

    url_builder.build()


    url = 'http://127.0.0.1:8000/Api/products/'

    get_wordlist()
    conn = ConnectionHandler(url=url)
    #conn.connect()

if __name__ == "__main__":
    main()  
