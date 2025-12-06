import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

from classes.ConnectionHandler import ConnectionHandler
from classes.Helper import *
from classes.URLBuilder import URLBuilder


def get_wordlist(file: str = "default.txt") -> list[str]:
    wd_dir = os.path.join(os.getcwd(), "wordlist")
    file = os.path.join(wd_dir, file)

    if not os.path.exists(file):
        raise FileNotFoundError(file)

    with open(file, "r") as f:
        return [x.strip() for x in f.readlines() if x.strip()]


def scan_urls(urls, threads=10, allowed_status={200}):
    total = len(urls)
    print(f"{CYAN}[*] Scanning {total} URLs with {threads} threads...{RESET}")

    found = []
    progress = 0

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(ConnectionHandler.fetch, u): u for u in urls}

        for future in as_completed(futures):
            status, full_url = future.result()
            progress += 1

            # progress output
            print(f"{YELLOW}[{progress}/{total}]{RESET}", end="\r")

            if status in allowed_status:
                print(f"{GREEN}[+] {full_url}  (status {status}){RESET}")
                found.append(full_url)

    print()
    return found


def recursive_discovery(positive_urls, wordlist, threads, allowed_status):
    print(f"{CYAN}[*] Starting 1-level recursion...{RESET}")

    new_targets = []
    for u in positive_urls:
        for w in wordlist:
            new_targets.append(f"{u}/{w}")

    return scan_urls(new_targets, threads, allowed_status)


def start_program(args):
    recursive = False
    wordlist_file = "default.txt"
    threads = 10
    allowed_status = {200}

    base_url = None

    for i in range(len(args)):
        if args[i] in ("-r", "--recursive"):
            recursive = True

        elif args[i] in ("-w", "--wordlist"):
            wordlist_file = args[i + 1]

        elif args[i] in ("-t", "--threads"):
            threads = int(args[i + 1])

        elif args[i] in ("--filter", "--status"):
            allowed_status = {int(x) for x in args[i + 1].split(",")}

        elif args[i].startswith("http"):
            base_url = args[i]

    if not base_url:
        print(RED + "No base URL provided." + RESET)
        return

    print(f"{CYAN}[*] Base URL: {base_url}{RESET}")
    print(f"{CYAN}[*] Threads: {threads}{RESET}")
    print(f"{CYAN}[*] Wordlist: {wordlist_file}{RESET}")
    print(f"{CYAN}[*] Filter status: {allowed_status}{RESET}")

    words = get_wordlist(wordlist_file)
    urls = URLBuilder(base=base_url, endpoint_list=words).get_built_urls()

    # first‑level scan
    positives = scan_urls(urls, threads, allowed_status)

    # recursion (optional)
    if recursive and positives:
        _ = recursive_discovery(positives, words, threads, allowed_status)


def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError
        start_program(sys.argv)
    except ValueError:
        print(f"""{YELLOW}
usage:
    python3 main.py <url> [-r] [-w wordlist.txt] [-t threads] [--filter 200,403]

example:
    python3 main.py https://example.com -r -t 15 --filter 200,403
{RESET}""")


if __name__ == "__main__":
    main()
