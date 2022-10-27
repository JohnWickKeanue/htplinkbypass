
import time
import cloudscraper
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from requests import get

url = "https://htpmovies.lol/exit.php?url=M3hGellLam5SSmI0Q3FHU01sRFI1UWtha2YrOWpRWGMwcEtWU1F2NXkyd3ljeVFxM2ZubVlpczUxMXlHM3hqSg=="

def htp(url):
    download = get(url, stream=True, allow_redirects=False) 
    xurl =download.headers["location"]   
    client = cloudscraper.create_scraper(allow_brotli=False)
    param = xurl.split("/")[-1]
    DOMAIN = "https://go.kinemaster.cc"
    final_url = f"{DOMAIN}/{param}"
    resp = client.get(final_url)
    soup = BeautifulSoup(resp.content, "html.parser")    
    try: inputs = soup.find(id="go-link").find_all(name="input")
    except: return "Incorrect Link"
    data = { input.get('name'): input.get('value') for input in inputs }
    h = { "x-requested-with": "XMLHttpRequest" }
    time.sleep(10)
    r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
    try:
        return r.json()['url']
    except: return "Something went wrong :("
print(htp(url))
