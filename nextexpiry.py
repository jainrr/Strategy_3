import requests,json
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta, TH

#def nextThu_and_lastThu_expiry_date ():

todayte = datetime.today()

cmon = todayte.month
if_month_next=(todayte + relativedelta(weekday=TH(1))).month
next_thursday_expiry=todayte + relativedelta(weekday=TH(2))

if (if_month_next!=cmon):
	month_last_thu_expiry= todayte + relativedelta(weekday=TH(5))
	if (month_last_thu_expiry.month!=if_month_next):
		month_last_thu_expiry= todayte + relativedelta(weekday=TH(4))
else:
	for i in range(1, 7):
		t = todayte + relativedelta(weekday=TH(i))
		if t.month != cmon:
			# since t is exceeded we need last one  which we can get by subtracting -2 since it is already a Thursday.
			t = t + relativedelta(weekday=TH(-2))
			month_last_thu_expiry=t
			break
str_month_last_thu_expiry=str(int(month_last_thu_expiry.strftime("%d")))+month_last_thu_expiry.strftime("%b").upper()+month_last_thu_expiry.strftime("%Y")
str_next_thursday_expiry=str(int(next_thursday_expiry.strftime("%d")))+next_thursday_expiry.strftime("%b").upper()+next_thursday_expiry.strftime("%Y")
print("================================================================================")

todayte = datetime.today()
cmon = todayte.month

for i in range(1, 6):
	t = todayte + relativedelta(weekday=TH(i))
	if t.month != cmon:
		# since t is exceeded we need last one  which we can get by subtracting -2 since it is already a Thursday.
		t = t + relativedelta(weekday=TH(-2))
		break
import datetime
thu = t.strftime("%yX%m%d").replace('X0','X').replace('X','')
thu1= t.strftime("%y%b").upper()
a = datetime.datetime.strptime(str_next_thursday_expiry,'%d%b%Y').strftime('%y')
b = datetime.datetime.strptime(str_next_thursday_expiry,'%d%b%Y').strftime('%m')
d = int(b)
if d<10:
	b= b[1]
c = datetime.datetime.strptime(str_next_thursday_expiry,'%d%b%Y').strftime('%d')
new_expirydate= a + b + c
if str_next_thursday_expiry == str_month_last_thu_expiry:
		ed = thu1
else:
	try:
		new_expirydate = a + b + c
		ed = new_expirydate
		inst = pd.read_csv("https://api.kite.trade/instruments")
		inst = inst.set_index(['tradingsymbol'])
		bnround = 14000
		strangle_CE = 0
		name = "NIFTY"+ed+ str(bnround+strangle_CE)+"CE"
		lot_size = inst.loc[name]['lot_size']
	except KeyError:
		c = str(int(c) - 1)
		new_expirydate = a + b + c
		ed = new_expirydate

with open("data/expiry.json", "w") as f:
	data = {"expirydate":ed}
	json.dump(data, f)
bnround = 14000
strangle_CE = 0
print("Zerodha Format Expiry Date = " + ed)
print("Compare with Zerodha Format = NIFTY"+ed+ str(bnround+strangle_CE)+"CE")
print("================================================================================")
print("Zerodha Format Expiry Date = " + thu1)
print("================================================================================")
print("Next Expiry Date = " + str_next_thursday_expiry)
print("================================================================================")
print("Month End Expiry Date = " + str_month_last_thu_expiry)
print("================================================================================")
