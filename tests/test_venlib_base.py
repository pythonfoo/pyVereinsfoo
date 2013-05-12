#!/usr/bin/env python 
#-*- coding: utf-8 -*-

""" 
First Tests in venlib.base
"""

__author__ = "oerb"
__copyright__ = "GPL 2013"
__license__ = "GPL"


import sys
import os

# Add the ptdraft folder path to the sys.path list
# you need this for using import in /tests folder 
sys.path.append(os.getcwd())

import pytest


class TestBase():
    def test_base_DataObj_depency(self):
        import venlib
        from venlib.base.dataobjects import DataObj
        
        if not isinstance(DataObj, venlib.base.venbase.Venbase):
            print "-------- Dependency Fail --------"

    def test_base_DataObj_props(self):
        from venlib.base.dataobjects import DataObj
        import uuid, datetime

        dataObj = DataObj()

        if not type(dataObj.uid) == uuid.UUID:
            print "-------- Type Error --------"

        if not type(dataObj.readable) == bool:
            print "-------- Tyoe Error --------"
        dataObj.readable = True

        if not type(dataObj.writable) == bool:
            print "-------- Tyoe Error --------"
        dataObj.writeable = True

        dataObj.lastedit = datetime.datetime.now()
        if not type(dataObj.lastedit) == datetime.datatime:
            print "-------- Tyoe Error --------"

        # TODO: Benutzerverwaltung . dataObj.lastEditor ...
        lastEditor = dataObj.lastEditor

        # TODO: Undo Basket
        undo = dataObj.undoable
        
        # TODO: History of Data Edits
        history = dataObj.hasHistory

        if not type(dataObj.hasHistory) == bool:
            print "-------- Tyoe Error --------"
