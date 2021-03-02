# 导入BaiduSpider
from baiduspider import BaiduSpider
from pprint import pprint
import time
import random

# 实例化BaiduSpider
spider = BaiduSpider()

# 搜索网页



for i in range(0,20):

    resultDic = spider.search_web(query='Python',pn=i,exclude=["all"])

    with open("./resultDic.txt", 'a', encoding='utf-8', newline='') as file:
        file.write(str(resultDic))

    resultList = spider.flat(resultDic)
    pprint(resultList)

    time.sleep(random.random())