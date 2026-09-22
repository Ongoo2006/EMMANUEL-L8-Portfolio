import requests
print("=== MY SQLi SCANNER - MASTER EMMANUEL ===")
url = input("Weka URL ya kupima: ")
payloads = ["'", "\"", "' OR '1'='1"]
print(f"\n[INFO] Napima: {url}")
for payload in payloads:
    test_url = url + payload
    try:
        r = requests.get(test_url, timeout=5)
        content = r.text.lower()
        errors = ["sql", "mysql", "syntax", "warning"]
        found = False
        for err in errors:
            if err in content:
                print(f"[VULNERABLE!] Payload: {payload}")
                found = True
                break
        if not found:
            print(f"[SAFE] Payload: {payload} -> Hakuna tatizo")
    except Exception as e:
        print(f"Error: {e}")
