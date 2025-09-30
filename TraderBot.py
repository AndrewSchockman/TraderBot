import yfinance as yf
import matplotlib.pyplot as plt

sp500 = yf.Ticker("^GSPC")
sp500 = sp500.history(period="max")
sp500.plot.line(y="Close", use_index=True)
plt.show()