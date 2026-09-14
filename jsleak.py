#!/usr/bin/env python3
# TBH-JSLeak - Find Secrets in JS (Bug Bounty)
import requests, re, argparse, json

BANNER = """\033[91m╔════════════════════════════════════╗
\033[91m║ \033[97mTBH-JSLeak \033[91m- Secret Finder         \033[91m║
\033[91m║ \033[90mTulungagung Black Hat | uchil404 \033[91m║
\033[91m╚════════════════════════════════════╝\033[0m"""

PATTERNS = {
    "API Key": r"api[_-]?key\s*[:=]\s*['\"]([A-Za-z0-9_\-]{10,})['\"]",
    "AWS Key": r"AKIA[0-9A-Z]{16}",
    "Token": r"token\s*[:=]\s*['\"]([A-Za-z0-9\-_\.]{10,})['\"]",
    "Password": r"password\s*[:=]\s*['\"]([^'\"]{4,})['\"]",
}

def scan(url):
    r=requests.get(url,timeout=5,headers={'User-Agent':'TBH-JSLeak/1.0'})
    found={}
    for name, pat in PATTERNS.items():
        m=re.findall(pat, r.text, re.I)
        if m: found[name]=m[:2]
    # Also find .js links
    js_links=re.findall(r'src=["\']([^"\']+\.js)', r.text)
    return {"url":url,"status":r.status_code,"js_links":js_links[:5],"secrets":found}

def main():
    print(BANNER)
    print("\033[91m[!] Hanya untuk scope yang diizinkan!\033[0m\n")
    parser=argparse.ArgumentParser(description="JSLeak")
    parser.add_argument("-u","--url",required=True)
    parser.add_argument("--json",help="Save JSON")
    args=parser.parse_args()
    print(f"[*] Scanning {args.url}...")
    result=scan(args.url)
    print(f"[+] JS Links: {result['js_links'] or 'none'}")
    if result['secrets']:
        print(f"\033[91m[!] Secrets found: {result['secrets']}\033[0m -> Potensi High, segera lapor & jangan disalahgunakan!")
    else: print("[✓] No obvious secrets")
    if args.json:
        open(args.json,'w').write(json.dumps(result,indent=2)); print(f"[✓] JSON: {args.json}")

if __name__=="__main__": main()
