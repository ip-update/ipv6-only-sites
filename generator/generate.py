#!/usr/bin/env python
# -*- coding: utf-8 -*-

from glob import iglob
from os.path import isfile, join


def handlesitefile(file):
    print(file)


def walksites(jsonpath):
    for f in iglob(join(jsonpath, '*.json')):
        if isfile(f):
            handlesitefile(f)


if __name__ == '__main__':
    walksites('./sites/')
