# Dirb-like

Dirpy is a program inspired by Dirb, a lightweight Python implementation of a directory brute-forcing tool
It discovers hidden files and directories on web servers by trying common paths from wordlists.


## ✨ Features
    ⚡ Multi-threaded scanning using ThreadPoolExecutor

    🎯 Status-code filtering (--filter 200,302,403)

    🌌 One-level recursion (re-scan discovered paths)

    🌈 ANSI-colored output (no libraries required)

    📡 HTTP & HTTPS support

    🧩 Simple URL builder

    🧵 Randomized or fixed wait times

    📁 Pluggable wordlists

## 📸 Terminal Preview
```bash
[+] https://target.com:443/admin

(status 200)
[+] https://target.com:443/login
 (status 403)
[+] https://target.com:443/api/v1
 (status 200)
[*] Scanning 350 URLs with 15 threads...
```


## 📦 Installation

Requires Python 3.9+

```bash
git clone https://github.com/<yourname>/CourierIQ.git
cd CourierIQ
python3 main.py -h
```

No dependencies. No pip. Pure Python.




## 🛠 Usage

### Run a simple scan:
```bash
python3 main.py https://example.com
```
### Use custom wordlist
```bash
python3 main.py https://example.com -w wordlist/custom.txt
```
### Multi-threading
```bash
python3 main.py https://example.com -t 20
```
### Filter by status code
```bash
python3 main.py https://example.com --filter 200,403
```
### Recursive scan (1 level deep)
```bash
python3 main.py https://example.com -r
```
### Full example
```bash
python3 main.py https://example.com \
    -w wordlist/default.txt \
    -t 25 \
    -r \
    --filter 200,301,302,403
```
