import requests
from bs4 import BeautifulSoup
from pprint import pprint

URL = "https://www.kivano.kg/"
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

# Get HTML
def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

# Get data
def get_data(html):
    bs = BeautifulSoup(html, 'html.parser')
    items = bs.find_all('div', class_='item product_listbox oh')
    kivano_lst = []
    for item in items:
        kivano_lst.append({
            'title': item.find('div', class_='listbox_title').get_text(),
            'price': item.find('div', class_='listbox_price').get_text(),
            'image': URL + item.find('div', class_='listbox_img pull-left').find('img').get('src'),
        })
    return kivano_lst

# Parser
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        kivano_lst_all_nouts = []
        for page in range(0, 1):
            html = get_html('https://www.kivano.kg/noutbuki', params=page)
            kivano_lst_all_nouts.extend(get_data(html.text))
        return kivano_lst_all_nouts
    else:
        raise Exception('Oops, something went wrong!')


pprint(parser())




