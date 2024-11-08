import requests
url = 'https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar'

custom_headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36 Edg/130.0.0.0',
    'accept-language': 'en-GB,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Referer': 'https://www.google.com/'
}
response = requests.get(url, headers= custom_headers)
response.encoding = 'utf-8'
print(response.text)