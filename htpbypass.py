
import time
import cloudscraper
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from requests import get

url = "https://htpmovies.art/go.php?url=M3hGellLam5SSmI0Q3FHU01sRFI1UWtha2YrOWpRWGMwcEtWU1F2NXkyd3ljeVFxM2ZubVlpczUxMXlHM3hqSg=="

def htp(url):
    download = get(url, stream=True, allow_redirects=False) 
    xurl =download.headers["location"]
    client = cloudscraper.create_scraper(allow_brotli=False)
    p = urlparse(xurl)
    final_url = f'{p.scheme}://{p.netloc}/links/go'
    res = client.head(xurl)
    header_loc = res.headers['location']
    param = xurl.split("/")[-1]
    req_url = f'{p.scheme}://{p.netloc}/{param}'
    p = urlparse(header_loc)
    ref_url = f'{p.scheme}://{p.netloc}/'
    h = { 'referer': ref_url }
    res = client.get(req_url, headers=h, allow_redirects=False)

    bs4 = BeautifulSoup(res.content, 'html.parser')
    inputs = bs4.find_all('input')
    data = { input.get('name'): input.get('value') for input in inputs }

    h = {
        'referer': ref_url,
        'x-requested-with': 'XMLHttpRequest',
    }
    time.sleep(10)
    res = client.post(final_url, headers=h, data=data)
    try:
        return res.json()['url'].replace('\/','/')
    except: return 'Something went wrong :('

print(htp(url))
