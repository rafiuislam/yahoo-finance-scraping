import re
import json
import csv
from io import StringIO
from bs4 import BeautifulSoup
import requests

url_stats = 'https://finance.yahoo.com/quote/{}/key-statistics?p={}'
url_profile = 'https://finance.yahoo.com/quote/{}/profile?p={}'
url_financials = 'https://finance.yahoo.com/quote/{}/financials?p={}'

stock = 'AAPL'

# response = requests.get(url_financials.format(stock, stock))
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
response = requests.get(url_financials.format(stock,stock),headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

pattern = re.compile(r'\s--\sData\s--\s')
script_data = soup.find('script', text=pattern).contents[0]

#beginning
# print(script_data[:500])
#Ending
# print(script_data[-500:])

start = script_data.find("context")-2

json_data = json.loads(script_data[start:-12])


# print(json_data['context'].keys())

# print(json_data['context']['dispatcher']['stores']['QuoteSummaryStore'].keys())

annual_is = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['incomeStatementHistory']['incomeStatementHistory']
quarterly_is = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['incomeStatementHistoryQuarterly']['incomeStatementHistory']

annual_cf = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['cashflowStatementHistory']['cashflowStatements']
quarterly_cf = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['cashflowStatementHistoryQuarterly']['cashflowStatements']

annual_bs = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['balanceSheetHistory']['balanceSheetStatements']
quarterly_bs = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['balanceSheetHistoryQuarterly']['balanceSheetStatements']

# print(annual_is[0]['operatingIncome'])



# financial Data:

# income Statements:
annual_is_stmts = []
quarterly_is_stmts = []

#annual
for s in annual_is:
    statement = {}
    for key, val in s.items():
        try:
            statement[key] = val['raw']
        except TypeError:
            continue
        except KeyError:
            continue
    annual_is_stmts.append(statement)

#quarterly
for s in quarterly_is:
    statement = {}
    for key, val in s.items():
        try:
            statement[key] = val['raw']
        except TypeError:
            continue
        except KeyError:
            continue
    quarterly_is_stmts.append(statement)

# print(annual_is_stmts[0])
# print(quarterly_is_stmts[0])

# cashflow Statements:
annual_cf_stmts = []
quarterly_cf_stmts = []

#annual
for s in annual_cf:
    statement = {}
    for key, val in s.items():
        try:
            statement[key] = val['raw']
        except TypeError:
            continue
        except KeyError:
            continue
    annual_cf_stmts.append(statement)

#quarterly
for s in quarterly_cf:
    statement = {}
    for key, val in s.items():
        try:
            statement[key] = val['raw']
        except TypeError:
            continue
        except KeyError:
            continue
    quarterly_cf_stmts.append(statement)

# print(annual_cf_stmts[0])
# print(quarterly_cf_stmts[0])

# balance sheet Statements:
annual_bs_stmts = []
quarterly_bs_stmts = []

#annual
for s in annual_bs:
    statement = {}
    for key, val in s.items():
        try:
            statement[key] = val['raw']
        except TypeError:
            continue
        except KeyError:
            continue
    annual_bs_stmts.append(statement)

#quarterly
for s in quarterly_bs:
    statement = {}
    for key, val in s.items():
        try:
            statement[key] = val['raw']
        except TypeError:
            continue
        except KeyError:
            continue
    quarterly_bs_stmts.append(statement)

# print(annual_bs_stmts[0])
# print(quarterly_bs_stmts[0])



# profile Data:

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
response = requests.get(url_profile.format(stock,stock),headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

pattern = re.compile(r'\s--\sData\s--\s')
script_data = soup.find('script', text=pattern).contents[0]

start = script_data.find("context")-2

json_data = json.loads(script_data[start:-12])

# print(json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['assetProfile']['companyOfficers']) #Key Executives
# print(json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['assetProfile']['longBusinessSummary']) #Description
# print(json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['secFilings']['filings']) #sec filings
print(json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['summaryDetail']) #summary details