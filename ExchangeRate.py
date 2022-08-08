import requests
from bs4 import BeautifulSoup


naver_url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=won+dollar+exchangerate&oquery=원달러환율&tqi=hYZPulprvh8ssnO%2Bed8ssssstCZ-144787"
naver = requests.get(naver_url)
print(naver.status_code)                  # 200 if successfully opened

moin_url = "https://www.themoin.com/"
moin = requests.get(moin_url)
print(moin.status_code)


naver_root = "#_cs_foreigninfo > div > div.api_cs_wrap > div > div.c_rate > div > div.rate_compare > div.compare_area > div > div:nth-child(3) > div.input_box._input_box > span.recite._recite.result"
moin_root = "#root > div > div.sc-hNMcUi.hOSnjg > section.sc-gPZUKb.bfpTxx > div > div.sc-gOPDNC.hMzDhc > div.sc-ktyGiW.kGrFMJ > div:nth-child(3) > div.sc-jEsDcK.fmGFYZ"



naver_soup = BeautifulSoup(naver.content, "html.parser")
naver_rate = naver_soup.select_one(naver_root)
naver_exchange_rate = naver_rate.get_text()
print(naver_exchange_rate)

moin_soup = BeautifulSoup(moin.content, "html.parser")
moin_rate = moin_soup.select_one(moin_root)
moin_exchange_rate = moin_rate
print(moin_exchange_rate)


def remover(text):
    original = text.split(",")
    longOriginal = "".join(original)
    integer = longOriginal.split(" ")
    naver_exchange_rate_int = int(integer[0])
    return naver_exchange_rate_int

naver_exchange_rate_int = remover(naver_exchange_rate)
print(remover(naver_exchange_rate))

def exchange_rate(AmountToExchange):
    print("base exchange rate: 1200 KRW == 1 USD")
    ExchangeRate = (input("your exchange rate"))
    if ExchangeRate == "naver":
        ExchangeRate = float(naver_exchange_rate_int)
    else:
        ExchangeRate = float(ExchangeRate)
    print("given exchange rate:", ExchangeRate, "KRW == 1 USD")
    USD = (1/ExchangeRate) * AmountToExchange
    Diff = USD - (1/1200) * AmountToExchange
    print("you will receive ", end="")
    if Diff < 0:
        print(abs(Diff), "less USD than base exchange rate")
    if Diff > 0:
        print(Diff, "more USD than base exchange rate")
    print("difference in KRW:", abs(Diff) * ExchangeRate)
