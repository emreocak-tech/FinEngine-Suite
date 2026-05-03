import yfinance as yf
import matplotlib.pyplot as plt
from abc import ABC,abstractmethod
from datetime import datetime
class AbstractStockMarketPrice(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def write_price(self,ticker,year_start,month_start,day_start,year_end,month_end,day_end):
        pass
    @abstractmethod
    def show_price(self,ticker,year_start,month_start,day_start,year_end,month_end,day_end):
        pass
    @abstractmethod
    def show_info_about_stock(self,ticker):
        pass
    @abstractmethod
    def compare_stockmarket(self,ticker1,ticker2,ticker3,year_start,month_start,day_start,year_end,month_end,day_end):
        pass
class StockMarketPrice(AbstractStockMarketPrice):
    def write_price(self,ticker,year_start,month_start,day_start,year_end,month_end,day_end):
        start_date=datetime(year=year_start,month=month_start,day=day_start)
        end_date=datetime(year=year_end,month=month_end,day=day_end)
        df=yf.download(tickers=ticker,start=start_date,end=end_date,interval="1d")
        price=df['Close']
        df_mean=price.mean(numeric_only=True)
        df_min=price.min(numeric_only=True)
        df_max=price.max(numeric_only=True)
        return [df_mean,df_min,df_max]
    def show_price(self,ticker,year_start,month_start,day_start,year_end,month_end,day_end):
        plt.clf()
        start_date = datetime(year=year_start, month=month_start, day=day_start)
        end_date = datetime(year=year_end, month=month_end, day=day_end)
        df = yf.download(tickers=ticker, start=start_date, end=end_date, interval="1d")
        price=df['Close']
        time=df.index
        plt.plot(time,price,color="Black",linewidth=4,marker="o",label=ticker)
        plt.title(f"{ticker} Price",color="Black",fontsize=20)
        plt.xlabel("Time",color="Black",fontsize=18)
        plt.ylabel("Price $",color="Black",fontsize=18)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        return plt
    def show_info_about_stock(self,ticker):
        stock = yf.Ticker(ticker)
        info = stock.info
        sector = info.get('sector', 'N/A')
        pe = info.get('trailingPE', 'N/A')
        forward_pe = info.get('forwardPE', 'N/A')
        industry_pe = info.get('industryTrailingPE', 'N/A')
        beta = info.get('beta', 'N/A')
        return [sector, pe, forward_pe, industry_pe, beta]
    def compare_stockmarket(self,ticker1,ticker2,ticker3,year_start,month_start,day_start,year_end,month_end,day_end):
        plt.clf()
        start_date = datetime(year=year_start, month=month_start, day=day_start)
        end_date = datetime(year=year_end, month=month_end, day=day_end)
        df = yf.download(tickers=ticker1, start=start_date, end=end_date, interval="1d")['Close']
        df2=yf.download(tickers=ticker2,start=start_date,end=end_date,interval="1d")['Close']
        df3=yf.download(tickers=ticker3,start=start_date,end=end_date,interval="1d")['Close']
        time1=df.index
        time2=df2.index
        time3=df3.index
        plt.plot(time1, df, color="Black", linewidth=4, marker="s",label=ticker1)
        plt.plot(time2, df2, color="Blue", linewidth=4, marker="o",label=ticker2)
        plt.plot(time3, df3, color="Purple", linewidth=4, marker="^",label=ticker3)
        plt.xlabel("Time",color="Black",fontsize=18)
        plt.ylabel("Price $",color="Black",fontsize=18)
        plt.grid(True)
        plt.legend(fontsize=12)
        plt.tight_layout()
        return plt
