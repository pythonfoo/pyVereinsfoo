#!/usr/bin/env python 
#-*- coding: utf-8 -*-

"""
Namespaces tests
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
        import venlib.base.mandatory
    
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





        
