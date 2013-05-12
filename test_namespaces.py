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
    def test_nsp_modules(self):
        "for later Modules outside base"
        import venlib.modules
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

