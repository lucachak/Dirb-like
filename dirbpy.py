"""
main entry point/ execution of code, as it seems to not be that big, i dont think i'll need much more

... i was wrong >:(


main()                                  # entry point, validate/count sys args
    |-> start_program()                 # check if paramn are correct, wordlist path, URLBuilder
            |
            |-> get_wordlist()          # get_defaul_one /wordlist/default.txt
            |
            V
       single_or_multi()                # where the magic will happen
            \                           # smashing URLBuilder, args, ThreadPoolExecutor to exec 
             |                           # everything. so, for each worker, one ConnectionHandler
             |
|=============================|
|                             |
|           SCAN              |
|                             |
|=============================|

"""
import os
import sys
from concurrent.futures import ThreadPoolExecutor,as_completed 

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
    
        


def scan_url(url:str):
    conn = ConnectionHandler(url=url)
    path,status = conn.connect()
    return (path, status) 
    

def single_or_multi(cores:int=1):
    """
        ill create a function to handle either a single core single 
        multiple cores. 
    """
        
    with ThreadPoolExecutor(max_workers=cores) as executor:
        futures = [executor.submit(scan_url, url) 
                       for url in url_builder.get_built_urls()]

        for future in as_completed(futures):
            path, status = future.result()
            if status in {200, 301, 302, 403}:
                print(f"[{status}] {path}")


    single_or_multi()






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
