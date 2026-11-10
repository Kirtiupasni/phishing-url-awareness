# Test Results

Python version used: 3.13.13 | Operating system: Windows 11 | Date: 10 Nov 2026
________

| # | Input | Expected result | Actual result | Pass/Fail |
|---|-------|-----------------|---------------|-----------|
| 1 | https://www.example.com/login | No listed warning signs | No listed warning signs found. This does NOT prove safety. | PASS |
| 2 | http://192.0.2.10/account | IP address + HTTP | Uses an IP address...; Uses HTTP... ; REVIEW CAREFULLY: 2 warning sign(s) | PASS |
| 3 | http://example.com@sample.invalid/login | @ symbol + HTTP | Contains an @ symbol...; Uses HTTP... ; REVIEW CAREFULLY: 2 warning sign(s) | PASS |
| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname segments | Contains many hostname segments/subdomains. | PASS |
| 5 | https://xn--example.invalid/ | Punycode-style hostname | Contains a punycode-style hostname. | PASS |

## Bonus checks

| Input | Actual result |
|-------|---------------|
| (empty Enter) | No URL entered. |
| www.example.com | Uses HTTP. HTTPS alone does not prove trust. |
| https://secure-login.example.invalid | No listed warning signs found. (A tricky name can slip through.) |
| http://[bad | This text is not a valid URL format. (no crash after Improvement C) |

## Notes

I learned that the hostname tells you the real website. I was surprised that a link with no warnings can still be dangerous