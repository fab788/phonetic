import requests
from bs4 import BeautifulSoup
#word = input( '請輸入詩人名稱:' )
def read(word):
    url = f'https://fanti.dugushici.com/ancient_proses/query?utf8=✓&q%5Bauthor_name_cont%5D={word}&q%5Btitle_cont%5D=&commit=搜++尋'

    html = requests.get( url )
    bs = BeautifulSoup(html.text,'lxml')
    data = bs.find('table',width="100%")
    try:
        row = data.find_all('tr')[1]
        poem = row.find('td').text
        return '作品:' + poem 
    except:
        return '查無此人' 
