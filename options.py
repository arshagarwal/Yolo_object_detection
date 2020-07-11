#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 03:41:20 2020

@author: arsh
"""
import argparse

class options:
    def __init__(self,):
        parser=argparse.ArgumentParser()
        parser.add_argument("data_path",help='path of the directory that contains the dataset ')
        self.parser= parser.parse_args()
    def __call__(self):
      return self.parser 
