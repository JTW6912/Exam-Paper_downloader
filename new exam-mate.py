import requests
from lxml import etree
import re
#重复 （ 更换link ）
    #获取页面代码
    #获取所有的列表
    #获取到link

    #下载

def get_Q_info(url):
    header = {
        'cookie': 'em_session=07fba454985e2ea741a2c8bf2b521f0831d31b97; _ga=GA1.2.1181440764.1654418906; _gid=GA1.2.727557872.1654418906; _gat=1'
        ,'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5056.0 Safari/537.36'
    }
    resp = requests.get(url= url,headers=header)
    tree = etree.HTML(resp.text)
    divs = tree.xpath('// *[ @ id = "question_list"]/div[@class="question"]')
    for div in divs:
        text = div.xpath('.//center/a[@onclick]/@onclick')
        print(text)
        for i in text:
            print(i)
        break





    resp.close()

if __name__ == '__main__':
    url = 'https://www.exam-mate.com/topicalpastpapers/?cat=21&subject=617&years=&seasons=&paper=&zone=&chapter=1726,1779&order=desc'
    get_Q_info(url)

