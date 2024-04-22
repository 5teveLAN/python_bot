import requests
import pandas as pd
from bs4 import BeautifulSoup

def getTitle(page):
    try:
        global n
        URL = "https://www.roccpa.org.tw/member_search/list2?AntiToken=MtCwPLmlBK4tpbJ8YKLhGjiPfOp5b2AjXZc6SUvy3a4%3d&location=C&fields=1&keys=&p="
        URL += str(page)
        web = requests.get(URL)
        target = BeautifulSoup(web.text, "html.parser")
        tag_td = target.find_all('td')
        #print(len(tag_td))
        for i in range(0, 40, 4):
            data_dict[1][n] = tag_td[i].getText()
            if tag_td[i+3].getText().strip() == "more":
                more = "https://www.roccpa.org.tw/member_search/"
                more += tag_td[i+3].find('a').attrs['href']
                webMore = requests.get(more)
                targetMore = BeautifulSoup(webMore.text, "html.parser")
                tags = targetMore.select('ol li')
                for tag in tags:
                    b_tag = tag.find('b')
                    div_tag = tag.find('div')

                    if b_tag is not None:
                        if (b_tag.text == "高市會籍編號") or b_tag.text == "中市會籍編號" or b_tag.text == "省會籍編號":
                            continue
                        #     data_dict[1].pop(n)
                        #     data_dict["E-mail"].pop(n)
                        #     data_dict["E-mailname"].pop(n)
                        #     data_dict["事務所傳真"].pop(n)
                        #     data_dict["事務所傳真name"].pop(n)
                        #     data_dict["事務所名稱"].pop(n)
                        #     data_dict["事務所名稱name"].pop(n)
                        #     data_dict['事務所地址'].pop(n)
                        #     data_dict["事務所地址name"].pop(n)
                        #     data_dict['事務所電話'].pop(n)
                        #     data_dict['事務所電話name'].pop(n)
                        #     data_dict['北市會籍編號'].pop(n)
                        #     data_dict["北市會籍編號name"].pop(n)
                        #     data_dict["會計師姓名"].pop(n)
                        #     data_dict["會計師姓名name"].pop(n)
                        #     break
                        data_dict[b_tag.text][n] = div_tag.text
                        data_dict[b_tag.text+"name"][n] = b_tag.text

            else:
                data_dict["會計師姓名"][n] = tag_td[i+1].getText()
                data_dict["事務所名稱"][n] = tag_td[i+2].getText()
            n+=1
    except:
        print("page" + str(n) + "has an error")    
        n+=1
    
n = 0
START_PAGE = 1
END_PAGE = 237
DATA = (END_PAGE - START_PAGE+2) * 10
number = ['']*DATA
name = ['']*DATA
corp = ['']*DATA
address = ['']*DATA
phone = ['']*DATA
fax = ['']*DATA
email = ['']*DATA
no = ['']*DATA

# make a dic to store data
data_dict = {
    1: ['']*DATA,
    "會計師姓名name": ["會計師姓名"]*DATA,
    "會計師姓名": ['']*DATA,
    "事務所名稱name": ["事務所名稱"]*DATA,
    "事務所名稱": ['']*DATA,
    "事務所地址name": ["事務所地址"]*DATA,
    "事務所地址": ['']*DATA,
    "事務所電話name": ['']*DATA,
    "事務所電話": ['']*DATA,
    "事務所傳真name": ['']*DATA,
    "事務所傳真": ['']*DATA,
    "E-mailname": ['']*DATA,
    "E-mail": ['']*DATA,
    "北市會籍編號name": ['']*DATA,
    "北市會籍編號": ['']*DATA
}

# 获取数据
for i in range(START_PAGE, END_PAGE+1):
    getTitle(i)


# 创建DataFrame
df = pd.DataFrame(data_dict)

# 将DataFrame写入CSV文件
df.to_csv("file.csv", index=False)


