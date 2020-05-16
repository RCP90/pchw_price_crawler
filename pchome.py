'''爬蟲作業二 爬PCHOME品名價格'''
import requests
import codecs
import json
import prettytable

t = prettytable.PrettyTable(["品名","價錢"], encoding="utf8")

item_name = input("搜尋商品關鍵字：")
r1=requests.get(
    "https://ecshweb.pchome.com.tw/search/v3.3/all/results",
    headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0",
        "Accept-Language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    },
    params={
        "q":item_name,
        "page":"1",
        "sort":"sale/dc",
    }
)
r=json.loads(r1.text)
for d in r["prods"]:
    t.add_row([d["name"],d["price"]])
    t.align["品名"] = "l"
    t.align["價錢"] = "l"
print(t)

while True:
    pages=input("請輸入頁數：")
    r2=requests.get(
        "https://ecshweb.pchome.com.tw/search/v3.3/all/results",
        headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0",
            "Accept-Language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        },
        params={
            "q":item_name,
            "page":pages,
            "sort":"sale/dc",
    }
    )
    rr=json.loads(r2.text)
    for d in rr["prods"]:
        t.add_row([d["name"],d["price"]])
        t.align["品名"] = "l"
        t.align["價錢"] = "l"
    print(t)