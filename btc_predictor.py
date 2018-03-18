import pandas
import matplotlib.pyplot as plt

# train_btc.csv
dataset = pandas.read_csv('/media/nvidia/JetsonSSD-250/sandbox/dev/bitcoin-price-api/train_btc.csv', usecols=[1], engine='python', skipfooter=3)
plt.plot(dataset)
plt.show()
