import csv
from exchanges.coindesk import CoinDesk


train_data = CoinDesk.get_historical_data_as_dict(start='2013-09-01', end='2017-12-31')
with open('train_btc.csv','wb') as csv_file1:
    writer = csv.writer(csv_file1)
    for key, value in train_data.items():
          writer.writerow([key,value])

print('training data done')

test_data = CoinDesk.get_historical_data_as_dict(start='2018-02-01', end='2018-03-12')

with open('test_btc.csv','wb') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in test_data.items():
          writer.writerow([key,value])

print('end of program')


