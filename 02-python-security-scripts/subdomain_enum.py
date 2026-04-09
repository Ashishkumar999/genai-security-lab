import requests

subdomains = ["api", "dev", "test", "admin"]

domain = "example.com"

for sub in subdomains:
    url = f"https://{sub}.{domain}"
    try:
        r = requests.get(url)
        print(url, r.status_code)
    except:
        pass
