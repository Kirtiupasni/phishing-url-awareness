# EWB Phishing URL Awareness Checker

## Overview
Phishing is a trick where criminals send fake links to steal passwords, card numbers or OTPs. This project is a Python tool that reads the text of a URL and shows simple warning signs, such as an @ symbol or an IP address. It only checks text and never opens the link.

## Features
- Detects an @ symbol in the URL
- Flags unusually long URLs (over 100 characters)
- Flags IP-address hostnames
- Flags many hostname segments (5 or more)
- Flags punycode-style hostnames (xn--)
- Flags the HTTP scheme
- Loop mode: check many URLs in one run, type `q` to quit
- "REVIEW CAREFULLY" summary with a warning count
- Handles malformed input without crashing
- Short "Why" explanation under each warning

## Requirements
Python 3.10 or later. No extra packages.

## How to Run
Windows: `python phishing_checker.py`

Mac/Linux: `python3 phishing_checker.py`

## Example Output
```
EWB Phishing URL Awareness Checker
Text checks only - this program does not open URLs.

Enter a sample URL (or type q to quit): http://192.0.2.10/account

Result:
1. Uses an IP address instead of a familiar domain.
   Why: Honest services normally use readable names, not bare numbers.
2. Uses HTTP. HTTPS alone does not prove trust.
   Why: HTTP is not encrypted, so data can be seen on the way.

REVIEW CAREFULLY: 2 warning sign(s) found.
Never enter passwords from unexpected links.
```

## Testing
| # | Input | Expected | Actual | Result |
|---|-------|----------|--------|--------|
| 1 | https://www.example.com/login | No warning signs | No listed warning signs found | PASS |
| 2 | http://192.0.2.10/account | IP address + HTTP | IP address + HTTP flagged | PASS |
| 3 | http://example.com@sample.invalid/login | @ symbol + HTTP | @ symbol + HTTP flagged | PASS |
| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname segments | Many segments flagged | PASS |
| 5 | https://xn--example.invalid/ | Punycode-style hostname | Punycode flagged | PASS |

Full table: `tests/test_samples.md`

## Screenshots
![Sample run](screenshots/sample_run.png)
![Test results](screenshots/test_results.png)

## Improvements
1. Loop with quit - Before, the program closed after one URL. Now it keeps asking until I type q, so I can test many URLs in one run. I tested it by entering all five sample URLs and then quitting.
2. Review carefully summary - I added a helper function called has_warnings() and a line that says "REVIEW CAREFULLY" with the number of warnings. I tested it with the IP address URL, which shows 2 warnings.
3. Malformed input handling - Typing http://[bad used to crash the program with a ValueError. I put the parsing line inside try/except, so now it prints "This text is not a valid URL format." I tested it by typing http://[bad.
4. Warning explanations - I added a dictionary called REASONS that gives a one-line reason under each warning. This helps a beginner understand why each sign matters. I tested it by checking that every warning shows a Why line.

After each change I ran all five sample tests again and they still passed.

## Limitations
This is an educational tool. It only reads URL text. It does not visit
URLs, scan for malware or prove that a URL is safe. No warning signs
found does NOT mean a URL is safe.

## Ethical Use
Use sample strings only. Do not collect credentials. Do not use this
project to deceive anyone or to test websites without permission.

## Author
Kirti Sanjay Upasni, Cybersecurity Internship, EWB Courses
