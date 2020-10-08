import requests
from lxml import etree
import os
from urllib.parse import unquote



response = requests.get('https://wiki.biligame.com/yysbwp/%E5%88%86%E7%B1%BB:%E5%BC%8F%E7%A5%9E')
html = etree.HTML(response.text)
href_list = html.xpath('//div[@class="mw-category-group"]/ul/li/a/@href')
s = requests.session()

for href in href_list:
    name = unquote(href.split('/')[2])
    print(name)
    href = 'https://wiki.biligame.com/' + href
    response = s.get(href).text
    html = etree.HTML(response)
    pic0 = html.xpath('//center/img/@src')[0]
    if os.path.exists('./pic/' + name) == False:
        os.mkdir('./pic/' + name)
    with open(f"./pic/{name}/{name}-0.png", "wb") as f:
        f.write(requests.get(pic0).content)
    pic_list = html.xpath('//div[@id="sidebar"]//div/a/img/@src')
    for i, pic in enumerate(pic_list):
        pic_url = pic[:pic.find('.png')+4].replace('/thumb', '')
        with open(f"./pic/{name}/{name}-{i+1}.png", "wb") as f:
            pic = requests.get(pic_url)
            f.write(pic.content)