import requests
from bs4 import BeautifulSoup


url = 'https://www.sba.gov/sitemap'

r = requests.get(url)
res = None
if r.status_code < 300:
    res = r.text
else:
    print(r.status_code)

soup = BeautifulSoup(res, 'html.parser')
desired_paths = ['/business-guide', '/funding-programs', '/federal-contracting']
links = set()
for link in soup.find_all('a'):
    href = link.get('href')
    for desired_path in desired_paths:
        if href is not None and href.startswith(desired_path):
            links.add(href)

links = sorted(list(links))
for link in links:
    print(link)

url = 'https://www.sba.gov' + links[1]
print(url)
r = requests.get(url)
res = None
if r.status_code < 300:
    res = r.text
else:
    print(r.status_code)
soup = BeautifulSoup(res, 'html.parser')
print(soup.get_text())

# class Scraper
# gets HTML data from a webpage
#   - with appropriate error handling
# parser html sites to only get relevant text (try not to get text of urls)
# saves text a local file
