# -*- coding: utf8 -*-
import sys
from frame import log
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

SEARCH_URL = "https://search.jd.com/Search?"


def good_detail_parser(keyword):
    params = {
        "keyword": keyword,
        "enc": "utf-8"
    }

    search_page = requests.get(SEARCH_URL, params=params).content
    bs = BeautifulSoup(search_page, "lxml")

    # get all good detail page href
    selector = "div.p-name > a"
    div = bs.select(selector)
    urls = [item.attrs["href"] for item in div]

    urls = [urljoin(SEARCH_URL, url) for url in urls]

    return urls[0]


def jd_specification_spider(keyword):
    log.info("jd specification spider: %s" % keyword)

    detail_url = good_detail_parser(keyword)
    detail_page = requests.get(detail_url).content
    bs = BeautifulSoup(detail_page, "lxml")
    
    selector = "div.Ptable-item"
    div = bs.select(selector)

    data = dict()
    for table in div:
        title = table.find("h3").string
        dt = table.find_all("dt", {"class": None})
        dd = table.find_all("dd", {"class": None})

        res = dict()
        for i in range(len(dt)):
            desc = {dt[i].string: dd[i].string}
            res.update(desc)

        data.update({title: res})

    return data


if __name__ == '__main__':
    if len(sys.argv) < 2:
        pass
    jd_specification_spider(sys.argv[1])
