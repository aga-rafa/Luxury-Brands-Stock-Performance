import yfinance as yahooFinance
import datetime
import pandas as pd
# Here We are getting  financial information
# We need to pass STOCK NAMES as argument for that
stocks = ["MC.PA", "RMS.PA", "KER.PA"]
# startDate , as per our convenience we can modify
startDate = datetime.datetime(2019, 1, 1)
# endDate , as per our convenience we can modify
endDate = datetime.datetime(2021, 10, 31)

dfs = {}

for stock in stocks:
    GetInformation = yahooFinance.Ticker(stock)
    # Valid options are 1d, 5d, 1mo, 3mo, 6mo, 1y,
    # 2y, 5y, 10y and ytd.
    # CHECKING FOR CONSISTENCY: print(GetInformation.info)
    #for key, value in GetInformation.info.items():
    #    print(key, ":", value)
    dfs[stock] = GetInformation.history(start=startDate,
                                     end=endDate)
ds = [frame.assign(Variable=name) for name,frame in dfs.items()]
combined = pd.concat(ds)
combined.reset_index(inplace=True)
df=combined.pivot(index='Date', columns='Variable', values='Open')

#plot
import matplotlib.pyplot as plt
import seaborn as sns
g = sns.lineplot(x='Date', y="Close", hue="Variable", data=combined, legend = False)
g.set(xlabel='Date', ylabel='Price at Close - EUR', title='Stocks Prices per Day (2019/01/01-2021/10/31)')
plt.legend(title = "Companies", loc='upper left', labels=['LVMH', 'Hermès', 'Kering (Gucci)'])
plt.show()
