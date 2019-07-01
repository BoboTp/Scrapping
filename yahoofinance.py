#!/usr/bin/env python3



import requests
import pandas as pd


################### Code for getting the S&P 500 Companies ##############################


wikiurl = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

wikiresponse = requests.get(wikiurl)

data = {"Company":[]}

wikihtmltext = wikiresponse.text


wikisplitone = wikihtmltext.split("Component Stocks")[0]
wikisecondsplit = wikisplitone.split("href=")



for pos in range(len(wikisecondsplit)):
		if "nyse" in wikisecondsplit[pos]:
			if "quote" in wikisecondsplit[pos]:
				answer = wikisecondsplit[pos].split('">')[1].split("</")[0]
				data["Company"].append(answer)
		if "nasdaq" in wikisecondsplit[pos]:
                        if "symbol" in wikisecondsplit[pos]:
                                answer = wikisecondsplit[pos].split('">')[1].split("</")[0]
                                data["Company"].append(answer)




print(len(data["Company"]))
print(data)




################### Code for fetching data for all the 500 Companies from Yahoo Finance ################



indicators = {"Previous Close":[],
                "Open":[],
                "Volume":[],
                "Avg. Volume":[],
                "Market Cap":[],
                "Beta (3Y Monthly)":[],
                "PE Ratio (TTM)":[],
                "EPS (TTM)":[],
                "Earnings Date":[],
                "1y Target Est":[]}


#example : https://finance.yahoo.com/quote/AAPL?p=AAPL


counter = 0
for tickersymbol in data["Company"]:
 	response = requests.get(url)
	htmltext = response.text
	print()
	print(tickersymbol)
	print()
	for i in indicators:
		print(i)
		Splitlist = htmltext.split(i)
		aftersplitlist = Splitlist[1].split("\">")[2]
		secondsplit = aftersplitlist.split("</span>")[0]
		indicators[i].append(secondsplit)
		print(secondsplit)	

print(indicators)
data.update(indicators)

df =pd.DataFrame(data)



print(data)
