import requests

url = input("Enter website URL: ").strip()

if not url.startswith(("http://", "https://")):
    url = "https://" + url

security_headers = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]

try:
    response = requests.get(url, timeout=10)

    print("\nHTTP Security Header Audit")
    print("----------------------------")
    print("URL:", url)
    print("Status Code:", response.status_code)
    print()

    for header in security_headers:
        if header in response.headers:
            print("[+] " + header + ": Present")
        else:
            print("[-] " + header + ": Missing")

except requests.RequestException as error:
    print("Could not connect to the website.")
    print("Error:", error)
