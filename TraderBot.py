import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

sp500 = yf.Ticker("^GSPC")
sp500 = sp500.history(period="max")
del sp500["Dividends"]
del sp500["Stock Splits"]
sp500["Tomorrow"] = sp500["Close"].shift(-1)
sp500["Target"] = (sp500["Tomorrow"] > sp500["Close"]).astype(int)
sp500 = sp500.loc["1990-1-1":].copy()

#First param increases accuracy, second minimizes overtraining at cost of accuracy, random seed
model = RandomForestClassifier(n_estimators=100, min_samples_split=100, random_state=1)

#Training and test sets
train = sp500.iloc[:-100]
test = sp500.iloc[-100]

predictors = ["Close", "Volume", "Open", "High", "Low"]
print(sp500)