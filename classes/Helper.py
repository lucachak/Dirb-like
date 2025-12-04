def print_help():
    print("""
╔══════════════════════════════════════════════════════╗
║                 DIRBPY - Directory Brute Forcer      ║
╚══════════════════════════════════════════════════════╝

Usage:
  python dirbpy.py -w WORDLIST [OPTIONS] URL

Required Arguments:
  -w, --wordlist PATH    Path to wordlist file (required)
  URL                    Target URL to scan (required)

Options:
  -r, --recursive        Enable recursive scanning
  -mt, --multithread     Enable multi-threading (default: 1 thread)
  -t, --threads NUM      Number of threads (default: 10 when -mt used)
  --timeout SEC          Request timeout in seconds (default: 5)
  -h, --help             Show this help message

Examples:
  python dirbpy.py -w wordlists/common.txt http://example.com
  python dirbpy.py -w wordlists/big.txt -r -mt http://target.com
  python dirbpy.py -w /path/to/wordlist.txt -t 20 http://test.com

Wordlist Format:
  • One directory/path per line
  • Lines starting with # are ignored
  • Example: admin, backup, config, phpmyadmin

Exit Codes:
  0 - Success
  1 - Missing required arguments
  2 - File not found
  3 - Invalid URL

For more information: https://github.com/lucachak/dirbpy
""")
