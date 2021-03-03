# 导入BaiduSpider
from baiduspider import BaiduSpider
from pprint import pprint
import time
import random

# 实例化BaiduSpider
spider = BaiduSpider()

# 搜索网页
for i in range(0,100):

    resultDic = spider.search_ads(query='防水补漏',pn=i)
    if len(resultDic["results"]) == 0:
        continue

    with open("./resultDic.txt", 'a', encoding='utf-8', newline='') as file:
        file.write(str(resultDic))

    resultList = spider.flat(resultDic)
    pprint(resultList)
    time.sleep(random.random())
