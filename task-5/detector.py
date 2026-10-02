from urllib.parse import urlparse
import re


def detect_phishing(url):
    score = 0
    indicators = []

    parsed = urlparse(url)
    domain = parsed.netloc.lower()

    # Check for HTTP instead of HTTPS
    if parsed.scheme == "http":
        score += 1
        indicators.append("Uses HTTP instead of HTTPS")

    # Check for IP address instead of domain name
    ip_pattern = r"^\d{1,3}(\.\d{1,3}){3}$"

    if re.match(ip_pattern, domain.split(":")[0]):
        score += 2
        indicators.append("Uses an IP address instead of a domain name")

    # Check for @ symbol
    if "@" in url:
        score += 2
        indicators.append("Contains an @ symbol")

    # Check for suspicious keywords
    keywords = [
        "login",
        "verify",
        "verification",
        "account",
        "password",
        "urgent",
        "secure",
        "update"
    ]

    found_keywords = [
        word for word in keywords
        if word in url.lower()
    ]

    if found_keywords:
        score += 1
        indicators.append(
            "Contains suspicious keywords: "
            + ", ".join(found_keywords)
        )

    # Check for URL shorteners
    shorteners = [
        "bit.ly",
        "tinyurl.com",
        "t.co",
        "goo.gl"
    ]

    if any(shortener in domain for shortener in shorteners):
        score += 2
        indicators.append("Uses a URL shortening service")

    # Check for excessive subdomains
    # Do not apply this check to IP addresses
    if not re.match(ip_pattern, domain.split(":")[0]):
        if domain.count(".") >= 3:
            score += 1
            indicators.append("Contains multiple subdomains")

    print("\n--- Phishing Detection Result ---")
    print("URL:", url)
    print("Risk Score:", score)

    if score >= 4:
        print("Classification: HIGH RISK / POSSIBLE PHISHING")
    elif score >= 2:
        print("Classification: SUSPICIOUS")
    else:
        print("Classification: LOW RISK")

    print("\nIndicators:")

    if indicators:
        for indicator in indicators:
            print("- " + indicator)
    else:
        print("- No obvious phishing indicators detected")


print("====================================")
print("       PHISHING DETECTION TOOL")
print("====================================")

url = input("\nEnter a URL to analyze: ")

detect_phishing(url)
