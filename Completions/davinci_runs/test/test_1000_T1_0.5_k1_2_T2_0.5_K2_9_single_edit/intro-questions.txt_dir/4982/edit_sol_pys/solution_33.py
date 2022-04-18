'''
Created on Feb 17, 2018

@author: mmp
'''

import os
import sys
import logging
import pandas as pd
from django.utils import timezone
from django.db import transaction
from constants import Constants
from utils.result import Results
from utils.software import Software
from utils.software import SoftwareManager
from utils.result import get_or_error
from utils.result import get_or_error_simple
from utils.result import get_or_create
from utils.result import get_or_create_simple
from utils.result import get_or_create_list
from utils.result import get_or_create_list_simple
from utils.result import get_or_none
from utils.result import get_or_none_simple
from utils.result import save_or_error
from utils.result import save_or_error_simple
from utils.result import delete_or_error
from utils.result import delete_or_error_simple
from utils.result import delete_or_none
from utils.result import delete_or_none_simple
from utils.result import update_or_error
from utils.result import update_or_error_simple
from utils.result import save_or_duplicate
from utils.result import save_or_duplicate_simple
from utils.result import get_or_none_simple
from utils.result import update_or_error
from utils.result import update_or_error_simple
from utils.result import save_or_error
from utils.result import save_or_error_simple
from utils.result import save_or_duplicate
from utils.result import save_or_duplicate_simple
from utils.result import get_or_none_simple
from utils.result import update_or_error
from utils.result import update_or_error_simple
from utils.result import save_or_error
from utils.result import save_or_error_simple
from utils.result import save_or_duplicate
from utils.result import save_or_duplicate_simple
from utils.result import get_or_none_simple
from utils.result import update_or_error
from utils.result import update_or_error_simple
from utils.result import save_or_error
from utils.result import save_or_error_simple
from utils.result import save_or_duplicate
from utils.result import save_or_duplicate_simple
from utils.result import get_or_none_simple
from utils.result import update_or_error
from utils.result import update_or_error_simple
from utils.result import save_or_error
from utils.result import save_or_error_simple
from utils.result import save_or_duplicate
from utils.result import save_or_duplicate_simple
from utils.result import get_or_none_simple
from utils.result import update_or_error
from utils.result import update_or_error_simple
from utils.result import save_or_error
from utils.result import save_or_error_simple
from utils.result import save_or_duplicate
from utils.result import save_or_duplicate_simple
from utils.result import get_or_none_simple
from utils.result import update_or_error
from utils.result import update_or_error_simple
from utils.result import save_or_error
from utils.result import save_or_error_simple
from utils.result import save_or_duplicate
from utils.result import save_or_duplicate_simple
from utils.result import get_or_none_simple
from utils.result import update_or_error
from utils.result import update_or_error_simple
from utils.result import save_or_error
from utils.result import save_or_error_simple
from utils.result import save_or_duplicate
from utils.result import save_or_duplicate_simple
from utils.result import get_or_none_simple
from utils.result import update_or_error
from utils.result import update_or_error_simple
from utils.result import save_or_error
from utils.result import save_or_error_simple
from utils.result import save_or_duplicate
from utils.result import save_or_duplicate_simple
from utils.result import get_or_none_simple
from utils.result import update_or_error
from utils.result import update_or_error_simple
from utils.result import save_or_error
from utils.result import save_or_error_simple
from utils.result import save_or_duplicate
from utils.result import save_or_duplicate_simple
from utils.result import get_or_none_simple
from utils.result import update_or_error
from utils.result import update_or_error_simple
from utils.result import save_or_error
from utils.result import save_or_error_simple
from utils.result import save_or_duplicate
from utils.result import save_or_duplicate_simple
from utils.result import get_or_none_simple
from utils.result import update_or_error
from utils.result import update_or_error_simple
from utils.result import save_or_error
from utils.result import save_or_error_simple
from utils.result import save_or_duplicate
from utils.result import save_or_duplicate_simple
from utils.result import get_or_none_simple
from utils.result import update_or_error
from utils.result import update_or_error_simple
from utils.result import save_or_error
from utils.result import save_or_error_simple
from utils.result import save_or_duplicate
from utils.result import save_or_duplicate_simple
from utils.result import get_or_none_simple
from utils.result import update_or_error
from utils.result import update_or_error_simple
from utils.result import save_or_error
from utils.result import save_or_error_simple
from utils.result import save_or_duplicate
from utils.result import save_or_duplicate_simple
from utils.result import get_or_none_simple
from utils.result import update_or_error
from utils.result import update_or_error_simple
from utils.result import save_or_error
from utils.result import save_or_error_simple
from utils.result import save_or_duplicate
from utils.result import save_or_duplicate_simple
from utils.result import get_or_none_simple
from utils.result import update_or_error
from utils.result import update_or_error_simple
from utils.result import save_or_error
from utils.result import save_or_error_simple
from utils.result import save_or_duplicate
from utils.result import save_or_duplicate_simple
from utils.result import get_or_none_simple
from utils.result import update_or_error
from utils.result import update_or_error_simple
from utils.result import save_or_error
from utils.result import save_or_error_simple
from utils.result import save_or_duplicate
from utils.result import save_or_duplicate_simple
from utils.result import get_or_none_simple
from utils.result import update_or_error
from


def main():
    shares = []
    for i in range(int(input())):
        temp = input().split()
        if temp[0] == "buy":
            shares.append(int(temp[1]) * int(temp[2]))
        elif temp[0] == "sell":
            shares.sort()
            for j in range(int(temp[1])):
                shares[j] = int(temp[2]) - shares[j]
        elif temp[0] == "split":
            temp2 = []
            for j in shares:
                temp2.append(j/int(temp[1]))
            shares = temp2
        elif temp[0] == "merge":
            temp2 = []
            for j in range(int(len(shares)/int(temp[1]))):
                temp2.append(sum(shares[j*int(temp[1]):(j+1)*int(temp[1])]))
            if len(shares)%int(temp[1]) != 0:
                temp2.append(sum(shares[int(len(shares)/int(temp[1]))*int(temp[1]):]))
            shares = temp2
        else:
            shares = [int(temp[1]) - i for i in shares]
    print(sum(shares)/len(shares))

main()
