#!/usr/bin/env python 
#-*- coding: utf-8 -*-

"""
First Mandatory tests
"""

__author__ = "oerb"
__copyright__ = "GPL 2013"
__license__ = "GPL" 



import sys
import os

# Add the ptdraft folder path to the sys.path list
#sys.path.append('/home/bison/Dokumente/Projekte/Coding/shared/pythonfoo_github/pyVereinsfoo/')
sys.path.append(os.getcwd())

import pytest


class TestMandatory():
    def test_mdy_Address_isinstance_DataObj(self):
        import venlib
        from venlib.base.mandatory.address import Address

        if not isinstance(Address, venlib.base.venbase.DataObj):
            print "-------- Dependency Fail --------"

    def test_mdy_Addresse_hasProps(self):
        from venlib.base.mandatory.address import Address

        adr = Address()
        
        if not type(adr.name) == "str":
            print "-------- Type Error --------"
        adr.name = "Schmidt"
        
        if not type(adr.first_name) == str:
            print "-------- Type Error --------"
        adr.first_name = "Otto"
        
        if not type(adr.companyname) == str:
            print "-------- Type Error --------"
        adr.companyname = "fastcars ltd"
        
        if not type(adr.priv_streat) == str:
            print "-------- Type Error --------"
        adr.priv_streat = "Woodway"
        
        if not type(adr.priv_house_nr) == str:
            print "-------- Type Error --------"
        adr.priv_house_nr = "10 a"
        
        # TODO: This test has to be extendet to countrycode Object
        if not type(adr.priv_countrycode) == str:
            print "-------- Type Error --------"
        adr.priv_countrycode = "40721"

        if not type(adr.bus_streat) == str:
            print "-------- Type Error --------"
        adr.bus_streat = "Woodway"
        
        if not type(adr.bus_house_nr) == str:
            print "-------- Type Error --------"
        adr.bus_house_nr = "10 a"
        
        # TODO: This test has to be extendet to countrycode Object
        if not type(adr.bus_countrycode) == str:
            print "-------- Type Error --------"
        adr.bus_countrycode = "40721"

        # TODO: This test has to be extendet to countrycode Object
        if not type(adr.postbox_countrycode) == str:
            print "-------- Type Error --------"
        adr.priv_countrycode = "40721"

        # TODO: How did postoffice Addresses work world wide
        if not type(adr.postbox_address) == str:
            print "-------- Type Error --------"
        adr.priv_countrycode = "Postoffice ...."
