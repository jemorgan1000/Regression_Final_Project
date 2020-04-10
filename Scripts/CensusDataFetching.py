"""
This file fetches the census data for each Georgia County, removes useless columns, and formats it.
"""


import requests
import pandas as pd
import json
import os.path as osp
import os


def get_data(address):
	"""
	"""
	response = requests.get(address)
	print(response.text)
	formattedresponse = json.loads(response.text)
	with open('response_text.json','w') as dout:
		dout.write(json.dumps(response))
	return formattedresponse

def dump_data(address):
	response = requests.get(address)
	print(address)
	with open('response_text.json','w') as dout:
		dout.write(json.dumps(response.text))

def create_df(resp, var_dict):
	"""
	"""
	flip_var_dict = {i:j for j,i in var_dict.keys()}
	header = resp[0]
	for i,v in enumerate(header):
		if v in flip_var_dict.keys():
			header[i] = v
	df =  pd.DataFrame.from_records(resp[1:],columns=header)
	return df 

def main(args):
	"""
	args[1] key for the use
	"""
	KEY = args[1]
	variables = {"WHITE_POP":"DP05_0037PE",
				"BLACK_POP":"DP05_0038PE",
				"HISPANIC_POP":"DP05_0070PE",
				"ASIAN_POP":"DP05_0044PE",
				"TOTAL_POP":"DP05_0033E",
				"HOUSING_UNITS":"DP05_0086E",
				"POP_UNDER_5":"DP05_0005E",
				"POP_5_9":"DP05_0006E",
				"POP_10_14":"DP05_0007E",
				"POP_15_19":"DP05_0008E",
				"POP_20_24":"DP05_0009E",
				"POP_25_34":"DP05_0010E",
				"POP_35_44":"DP05_0011E",
				"POP_45_54":"DP05_0012E",
				"POP_55_59":"DP05_0013E",
				"POP_60_65":"DP05_0014E",
				"POP_65_74":"DP05_0015E",
				"POP_75_84":"DP05_0016E",
				"POP_85_P":"DP05_0017E",
				"POVERTY_PERCENT":"DP03_0128E",
				"INC_U_10":"DP03_0076PE",
				"INC_10_15":"DP03_0077PE",
				"INC_15_25":"DP03_0078PE",
				"INC_25_34":"DP03_0079PE",
				"INC_34_49":"DP03_0080PE",
				"INC_50_75":"DP03_0081PE",
				"INC_75_100":"DP03_0081PE",
				"INC_100_150":"DP03_0083PE",
				"INC_150_200":"DP03_0084PE",
				"INC_200_G":"DP03_0085PE",
				"SCHOOL_9":"DP02_0059PE",
				"SCHOOL_9_12_ND":"DP02_0060PE", # no diploma
				"SCHOOL_9_12":"DP02_0061PE",
				"SCHOOL_SOME_COLLEGE":"DP02_0062PE",
				"SCHOOL_ASSOC":"DP02_0063PE",
				"SCHOOL_BACH":"DP02_0064PE",
				"SCHOOL_GRAD":"DP02_0065PE",
				"HEALTH_INSUR":"DP03_0095PE"}
	dems = list(variables.values())
	dems = ','.join(dems)
	base = f"https://api.census.gov/data/2018/acs/acs5/profile?get=NAME,{dems}&for=county:*&in=state:*&key={KEY}"
	din = dump_data(base)

if __name__ == '__main__':
	import sys
	main(sys.argv)
