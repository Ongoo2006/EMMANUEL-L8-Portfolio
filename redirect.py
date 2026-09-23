import requests
print("Bug Hunter - Open Redirect Check")
url = input("Weka URL: ").strip()
if not url:
    url = "https://example.com?next="
full_url = url + "//google.com"
print(f"Tunajaribu: {full_url}")
try:
    r = requests.get(full_url, allow_redirects=False, timeout=10)
    print(f"Status: {r.status_code}")
    print(f"Location: {r.headers.get('Location','Hakuna')}")
    if r.status_code in [301,302,303,307,308] and "google.com" in str(r.headers.get('Location','')):
        print("BUG FOUND!")
    else:
        print("Hakuna bug")
except Exception as e:
    print(f"Error: {e}")
