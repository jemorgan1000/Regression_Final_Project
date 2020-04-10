
import json
import pandas as pd 
from os import getcwd
import os.path as osp


def build_df(resp_path,lookup_path):
	with open(resp_path) as din:
		resp = json.load(din)
	df = pd.DataFrame.from_records(resp[1:],columns=resp[0])
	lu_df = pd.read_csv(lookup_path,names=['READABLE','CENSUS'])
	decoder = {tup[2]:tup[1] for tup in lu_df.itertuples()}
	df.rename(columns=decoder,inplace=True)
	return df


def main():
	chdir = getcwd()
	wd = osp.dirname(chdir)
	data_path = osp.join(wd,'Data')
	df = build_df(osp.join(data_path,'response.json'), osp.join(data_path,'census_lookups_table.csv'))
	df.to_csv('County_Dems_Processed.csv')


if __name__ == '__main__':
	main()