# Strategy_3

Code to automatically calculate next weekly Expiry date (not current week) and monthly expiry date.

Change Line Number 12  TH(2) to TH(1) to get current week expiry date...


# import file and library
import nextexpiry
import json

# load expirydate.json file and assign to variable
f            = open("data/expiry.json","r")
expiry  = json.load(f)
expirydate = expiry["expirydate"]

# how to use
long_ce = "NIFTY"+str(expirydate)+str(14000)+"CE"
