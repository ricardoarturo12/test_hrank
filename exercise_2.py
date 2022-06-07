#!/bin/python3

import math
import os
import random
import re
import sys
import requests


#
# Complete the 'weatherStation' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING keyword as parameter.
#

def weatherStation(keyword):
    # Write your code here
    result_filter = ''
    result_all = ''

    #api connect
    r = requests.get("https://jsonmock.hackerrank.com/api/weather").json()

    total_pages = r['total_pages']

    filter_active = False

    x = range(1, total_pages+1)

    for page in x:
        r = requests.get("https://jsonmock.hackerrank.com/api/weather", params={'page':page}).json()

        data_page = r["data"]

        for data in data_page:

            if keyword in data["name"]:
                result_filter += data_process(data)
                result_all = ''
                filter_active = True

            if not filter_active:
                result_all += data_process(data)

    return result_all or result_filter


def data_process(data):
    return f'{data["name"]},{number_value(data["weather"])},{number_value(data["status"][0])},{number_value(data["status"][1])} \n'


def number_value(data):
    numbers = ''
    for word in data:
        if word.isdigit():
            numbers += f'{int(word)}'
    return numbers



if __name__ == '__main__':
    fptr = 'all'

    keyword = input()

    result = weatherStation(keyword)
    print('\n')
    print(result)
