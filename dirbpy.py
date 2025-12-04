"""
main entry point/ execution of code, as it seems to not be that big, i dont think i'll need much more
"""
from ast import match_case
import os
import sys
from multiprocessing import Pool, Value
from classes.ConnectionHandler import ConnectionHandler
from classes.URLBuilder import URLBuilder
from classes import Helper

def get_wordlist(file:str="default.txt") -> list[str]:
    line = []
    wd_dir = os.path.join(os.getcwd(), "wordlist")
    file = os.path.join(wd_dir,file)

    if os.path.exists(file):
        with open(file, "r") as f:
            line = f.read().split("\n")
    else:
        raise LookupError()
    return line


def start_program(args:list):
    url_builder = URLBuilder()
    for i in range(1,len(args)):
        match args[i]:
            case "-r":
                print(args[i])
            case "--recursive":
                print(args[i])

            case "-w":
                print(args[i])
            case "--wordlist":
                print(args[i])

            case "-t":
                print(args[i])
            case "--threads":
                print(args[i])

            case "-mt":
                print(args[i])
            case "--multithread":
                print(args[i])
                
            case "--timeout":
                print(args[i])

            case _ :
                url_builder = URLBuilder(
                        base = args[i],
                        endpoint_list=get_wordlist()
                        )

    url_builder.build()

    
    def single_core()
        for url in url_builder.get_built_urls():
            conn = ConnectionHandler(url=url)
            conn.connect()
    
    def multi_core(cores:int):
        pass



def main() -> None:
    valid_method = sys.argv[-1]
    try: 
        if len(sys.argv) <= 2:
            raise ValueError
        if not valid_method.startswith("http"): 
            if not valid_method.startswith("https"):
                raise ValueError
            else:
                pass
        else:
            start_program(sys.argv)

    except ValueError as e:
        Helper.print_help()

    

if __name__ == "__main__":
    main()  
