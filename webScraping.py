import requests
import bs4
import pandas as pd
'''
data_web = requests.get('https://www.gadisline.com/listado-de-productos/?idListProd=13131')
data = bs4.BeautifulSoup(data_web.text, 'lxml')
#print(data.select('.product-title')[0].getText())

chain = ''
chain2 = ''
chain3 = ''

for i in data.select('.product-title')[0].getText():
    chain += i.replace('\n','')

for i in chain:
    chain2 += i.replace('\t','')
for i in chain:
    chain3 += i.replace('\r','')
prices = data.select('.price-product')
products = data.select('.product-title')
#print(chain2)
#print(products)
products_list = []
prices_list = []

for product in products:
    products_list.append(product.getText().replace('\t','').replace('\r','').replace('\n',''))

for price in prices:
    prices_list.append(price.getText().replace('\t','').replace('\r','').replace('\n',''))

products_list = list(set(products_list))
supermarket_list = pd.DataFrame(
    {'products': products_list,
     'prices': prices_list
    })

print(supermarket_list)
'''


'''
WEBSCRAPING SUPERMERCADOS DIA
'''
data_web = requests.get('https://www.dia.es/compra-online/productos/lacteos-y-huevos/yogures/c/WEB.005.050.00000?page=0&disp=')
data = bs4.BeautifulSoup(data_web.text, 'lxml')
#print(data.select('.product-title')[0].getText())

prices = data.select('.price')
products = data.select('.details')
#print(chain2)
#print(products)
products_list = []
prices_list = []

for product in products:
    products_list.append(product.getText().replace('\t','').replace('\r','').replace('\n',''))

for price in prices:
    prices_list.append(price.getText().replace('\t','').replace('\r','').replace('\n','').replace('\xa0',''))

'''
products_list = list(set(products_list))
supermarket_list = pd.DataFrame(
    {'products': products_list,
     'prices': prices_list
    })
'''

prices_list = [item for item in prices_list if len(item)>0]
products_list = [item for item in products_list if len(item)>0]
prices_list.pop(0)
#products_list = list(set(products_list))
supermarket_list = pd.DataFrame(
    {'products': products_list,
     'prices': prices_list
    })
print(supermarket_list)
