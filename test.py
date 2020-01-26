#!/usr/bin/python3

import dart_fss as dart
import sys

if len(sys.argv) < 2:
    print("Run it with API key.")
    exit()

crp_cd='005930' # Samsung Electronics
start_dt='20180101'

api_key=sys.argv[1]
dart.dart_set_api_key(api_key=api_key)
crp_list = dart.get_crp_list()
print(crp_list)
basic_info = crp_list.find_by_crp_cd(crp_cd)
print(basic_info)
financial_reports = basic_info.get_financial_statement(start_dt)
print(financial_reports)
