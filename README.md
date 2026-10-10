# TBH-JSLeak

<p align="center">
  <a href="https://github.com/TulungagungBlackHat/TBH-JSLeak/actions/workflows/ci.yml"><img src="https://github.com/TulungagungBlackHat/TBH-JSLeak/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <img src="https://img.shields.io/badge/license-MIT-red.svg" alt="License">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/severity-high-red.svg" alt="Severity">
</p>

Scans JavaScript files for accidentally shipped secrets: API keys, tokens, and credentials hardcoded in frontend code.

Part of the [Tulungagung Black Hat](https://github.com/TulungagungBlackHat) toolset.

## What It Checks

- JS assets referenced by the target page
- Regex patterns for common secret shapes: API keys, JWTs, AWS-style keys, generic `token`/`secret`/`password` assignments
- Reports file location + matched value for manual verification

Secrets in JS are public by definition — **verify validity before reporting** (a dead test key is noise), and never use a found credential beyond confirming it works.

## Install

```bash
git clone https://github.com/TulungagungBlackHat/TBH-JSLeak
cd TBH-JSLeak
pip install -r requirements.txt
```

## Usage

```
usage: jsleak.py [-h] -u URL [--json JSON]

options:
  -u, --url URL     Target page URL
  --json JSON       Save JSON
```

```bash
python3 jsleak.py -u "https://example.com" --json secrets.json
```

## Sample Output

```
[*] Scanning https://example.com...
[+] JS Links: /assets/app.js, /assets/config.js
[!] Secrets found: AWS_ACCESS_KEY_ID=AKIA... -> Potensi High, segera lapor!
[✓] JSON: secrets.json
```

## Authorized Use Only

Only against scopes you own or are authorized to test. Found credentials: report them, don't use them. See [SECURITY.md](SECURITY.md).

## Related Tools

- [TBH-DirFinder](https://github.com/TulungagungBlackHat/TBH-DirFinder) — find exposed `.env` and backup files
- [TBH-ParamFinder](https://github.com/TulungagungBlackHat/TBH-ParamFinder) — parameters referenced in JS

## License

[MIT](LICENSE) — Tulungagung Black Hat, East Java, Indonesia. Always Smile :)
