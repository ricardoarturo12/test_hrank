#!/bin/python3

import math
import os
import random
import re
import sys
import requests


def run(min_value, max_value):
    url = "https://jsonmock.hackerrank.com/api/medical_records"

    total_pages = requests.get(url).json()['total_pages']
    quantity = 0

    for page in range(1, total_pages+1):
        r = requests.get(url, params={'page': page}).json()
        data_page = r['data']

        for data in data_page:

            if int(data["vitals"]["bloodPressureDiastole"]) >= min_value and int(data["vitals"]["bloodPressureDiastole"]) <= max_value:

                quantity+=1

    return quantity


if __name__ == '__main__':
    min_value = int(input("valor1 : "))
    max_value = int(input("valor2 : "))

    values = run(min_value, max_value)

    print(values)