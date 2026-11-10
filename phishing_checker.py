"""EWB Phishing URL Awareness Checker.

Educational tool. It only reads the TEXT of a URL. It never opens a URL,
scans a website or sends data anywhere.
"""

import re
from urllib.parse import urlparse

# Warning messages are stored once so the code and the reasons table stay in sync.
MSG_AT = "Contains an @ symbol; inspect carefully."
MSG_LONG = "Unusually long URL (over 100 characters)."
MSG_IP = "Uses an IP address instead of a familiar domain."
MSG_SEGMENTS = "Contains many hostname segments/subdomains."
MSG_PUNY = "Contains a punycode-style hostname."
MSG_HTTP = "Uses HTTP. HTTPS alone does not prove trust."
MSG_NONE = "No listed warning signs found. This does NOT prove safety."
MSG_EMPTY = "No URL entered."
MSG_NO_HOST = "Could not identify a hostname."
MSG_INVALID = "This text is not a valid URL format."

# Improvement D: a one-line reason for each warning.
REASONS = {
    MSG_AT: "The browser ignores the text before @, so the link can look like one site but go to another.",
    MSG_LONG: "A long link can hide the real destination far to the right.",
    MSG_IP: "Honest services normally use readable names, not bare numbers.",
    MSG_SEGMENTS: "Stacking many names (a.b.c.d.e) can make a link look official.",
    MSG_PUNY: "xn-- can hide look-alike foreign letters that mimic a real name.",
    MSG_HTTP: "HTTP is not encrypted, so data can be seen on the way.",
}

# Messages that are information, not real warnings (used by Improvement B).
INFO_MESSAGES = (MSG_EMPTY, MSG_NO_HOST, MSG_NONE, MSG_INVALID)


def inspect_url(raw_url):
    """Check visible URL text for selected warning signs."""
    url = raw_url.strip()
    findings = []

    if not url:
        return [MSG_EMPTY]

    candidate = url if "://" in url else "http://" + url

    # Improvement C: malformed input (e.g. "http://[bad") must not crash.
    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return [MSG_INVALID]

    if not host:
        return [MSG_NO_HOST]

    if "@" in candidate:
        findings.append(MSG_AT)

    if len(url) > 100:
        findings.append(MSG_LONG)

    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append(MSG_IP)

    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append(MSG_SEGMENTS)

    if "xn--" in host:
        findings.append(MSG_PUNY)

    if parsed.scheme.lower() == "http":
        findings.append(MSG_HTTP)

    if not findings:
        findings.append(MSG_NONE)

    return findings


def has_warnings(findings):
    """Improvement B helper: True only when real warning signs were found."""
    return not findings[0].startswith(INFO_MESSAGES)


def main():
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")

    # Improvement A: keep checking URLs until the user quits.
    while True:
        raw_url = input("\nEnter a sample URL (or type q to quit): ")
        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break

        findings = inspect_url(raw_url)
        print("\nResult:")
        for number, item in enumerate(findings, start=1):
            print(str(number) + ". " + item)
            # Improvement D: explain why this warning matters.
            if item in REASONS:
                print("   Why: " + REASONS[item])

        # Improvement B: clear summary when real warnings exist.
        if has_warnings(findings):
            print("\nREVIEW CAREFULLY: " + str(len(findings)) + " warning sign(s) found.")

        print("Never enter passwords from unexpected links.")


if __name__ == "__main__":
    main()
