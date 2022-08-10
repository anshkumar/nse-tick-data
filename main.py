from intraday import Intra_Day
import csv
from datetime import datetime

ID = Intra_Day('NIFTY 50')
dataPoints = ID.nifty_intraDay()
today = datetime.today()

with open(datetime.strftime(datetime(today.year, today.month, today.day), '%Y-%m-%d')+'.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(dataPoints)
