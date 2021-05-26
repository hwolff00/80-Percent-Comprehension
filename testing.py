#!/usr/local/bin/python
# -*- coding: latin-1 -*-

import re

key = "([\d\w +-.''"",?!\(\)]*){[\w/]*}([\d\w +-.''"",?!\(\)]*)"
phrase = '" to use or have (something) as clothing {bc} to have (a shirt, pants, etc.) over part of your body"'

str_lst = re.findall(key, phrase)

if str_lst == []:
    print(phrase)
else:
    str = ''
    for i, x in str_lst:
        str += i
        str += x

    print(str)
