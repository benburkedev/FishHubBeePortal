#
# chargebee1.py
# Purpose: 
#
# Environment
#	     
# Inputs: various tables from Chargebeen and hubspot
# Output(s): TBA
#
#
# Use the pandas and numpy libraries for data and numeric processing
#
import pandas as pd
import numpy as np
import chargebee
import json
import os


# the main two dataframes are:

# Pipedrive Organisations and Chargebee companies are wildly out of sync. Produced this map df to provide inter-relationships

global BeePipeCompanyNameMapdf # the map.. is not the territory

# list of fields to use for Customer record (based on Chargebee Customer extract
global lstCustomer 

lstCustomer = ['Email','Billing_Address_Email','First_Name','Last_Name','Company','Billing_Address_First_Name','Billing_Address_Last_Name','domain','FishEyeD','Billing_Address_Line1','Billing_Address_Line2', \
'Billing_Address_City','Billing_Address_State','Billing_Address_Zip']

lstDeals = ['First_Name','Last_Name','Email','Phone','Organization']

# This script attempts to access a directory pointed to by environment variable GDrivePath - can be over-ridden by swapping in the following hard coded path
# GDrivePath = '/mnt/c/users/ben/Google Drive/HSLoader'
#GDrivePath = os.environ.get('HSLOADERPATH')

#if GDrivePath is None:
	#print("Environment not setup")
	#exit(1);


#print("Reading company names map")

chargebee.configure("test_wKIlCtk29ynbkoQkcmkDcdRXSXYz1gb40","fishburners-sydney-test")

entries = chargebee.Customer.list({
	"Customer_Portal_Status[is]" : "Active"
	})

for entry in entries:
	customer = entry.customer
	card = entry.card
	print (customer)


