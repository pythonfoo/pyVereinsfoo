#!/usr/bin/env python 
#-*- coding: utf-8 -*-
""" Some Description to enter"""
__author__ = "oerb"
__copyright__ = "GPL 2013"
__license__ = "GPL" 

""" Here I beginn to demonstrate the test Libery for 
Testdriven Development. The First at all is to define 
what Namespaceing is to use in this Project. So we 
must test the Framestructure. """

import pytest

class TestNamespaces():
    def test_venlib(self):
        import venlib
    def test_nsp_base(self):
        import venlib.base
    def test_nsp_base_venbase(self):
        "All classes hast to be child of Venbase not object!!!!"
        from venlib.base.venbase import Venbase
    def test_nsp_modules(self):
        "for later Modules outside base"
        import venlib.modules
    def test_nsp_mandatory(self):
        "it has to be Mandatory, here also are Adresses etc"
        import venlib.mandatory
    def test_nsp_bookkeeping(self):
        "bookkeeping"
        import venlib.base.bookkeeping
    def test_nsp_hbci(self):
        "hbci online banking"
        import venlib.base.hbci
    def test_nsp_docs(self):
        "Document view, print else"
        import venlib.base.docs
    def test_nsp_web(self):
        "Web-Gui"
        import venlib.base.web
    def test_nsp_qtgui(self):
        "Qt-Gui"
        import venlib.base.qtgui
    def test_nsp_datev(self):
        "datev interface"
        import venlib.base.datev
    def test_nsp_dbif(self):
        "databases Interface / Interfaces"
        import venlib.base.dbif
    def test_nsp_dbif_sqlite(self):
        "database Interface sqlite"
        import venlib.base.dbif.sqlite
    def test_nsp_dbif_mysql(self):
        "database Interface sqlite"
        import venlib.base.dbif.mysql
    def test_nsp_ldap(self):
        "LDAP Interface"
        import venlib.base.ldap

class TestMandatory():
    def test_mdy_Address_isinstance_venbase(self):
        import venlib
        from venlib.base.mandatory.address import Address

        if not isinstance(Address, venlib.base.venbase.Venbase):
            print "Adresse has to be child of venlib.base.venbase.Venbase"

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

        
