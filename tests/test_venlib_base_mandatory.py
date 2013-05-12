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
sys.path.append(os.getcwd())

import pytest
import uuid

class TestMandatory():
    def test_mdy_Address_isinstance_DataObj(self):
        import venlib
        from venlib.base.mandatory.address import Address

        if not isinstance(Address, venlib.base.venbase.DataObj):
            print "-------- Dependency Fail --------"

    def test_mdy_Addresse(self):
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

        if not type(adr.weburl) == str:
            print "-------- Type Error --------"
        adr.weburl = "http://www.chaosdorf.de"
        
        if not type(adr.position) == str:
            print "-------- Type Error --------"
        adr.position = "General"
        
        # mdyID is the Mandator ID as an UUID
        # or define a table with Adress and Mandator UUID's
        if not type(adr.mdyID) == uuid.UUID:
            print "-------- Type Error --------"
        mdyid = adr.mdyID
        # TODO: do not know if this works
        # just for test if only getter is set
        with pytest.raises(AttributeError):
            adr.mdyID = uuid.uuid4()

    def test_mdy_phone(self):
        from venlib.base.mandatory.address import Phone
        phone = Phone()
        
        # TODO: Phone Typologic in an Helper to fill here
        if not type(phone.number) == str:
            print "-------- Type Error --------"
        phone.number = "0171-12345678"
 
        if not type(phone.typ) == int:
            print "-------- Type Error --------"
        phone.typ = 1

        if not type(phone.phoneID) == uuid.uuid:
            print "-------- Type Error --------"
        phoneid = phone.phoneID
        # TODO: do not know if this works
        with pytest.raises(AttributeError):
            phone.phoneID = uuid.uuid4()

        notes.adrID = uuid.uuid4()
        if not type(notes.adrID) == uuid.uuid:
            print "-------- Type Error --------"

    def test_mdy_email(self):
        from venlib.base.mandatory.address import EMail
        email = EMail()
        
        # TODO: EMail Typologic in an Helper to fill here
        if not type(email.email_address) == str:
            print "-------- Type Error --------"
        email.email_address = "test@master.de"
 
        if not type(email.typ) == int:
            print "-------- Type Error --------"
        email.typ = 1

        if not type(email.emailID) == uuid.uuid:
            print "-------- Type Error --------"
        emailid = email.emailID
        # TODO: do not know if this works
        with pytest.raises(AttributeError):
            email.emailID = uuid.uuid4()
        
        notes.adrID = uuid.uuid4()
        if not type(notes.adrID) == uuid.uuid:
            print "-------- Type Error --------"

    def test_mdy_notes(self):
        from venlib.base.mandatory.address import Notes
        notes = Notes()
        
        if not type(notes.shorttxt) == str:
            print "-------- Type Error --------"
        notes.shorttxt = "some note shorts"

        if not type(notes.longtxt) == str:
            print "-------- Type Error --------"
        notes.longtxt = "some note Long text"

        if not type(notes.typ) == int:
            print "-------- Type Error --------"
        notes.typ = 1

        if not type(notes.noteID) == uuid.uuid:
            print "-------- Type Error --------"
        noteid = notes.noteID
        # TODO: do not know if this works
        with pytest.raises(AttributeError):
            notes.noteID = uuid.uuid4()
        
        notes.adrID = uuid.uuid4()
        if not type(notes.adrID) == uuid.uuid:
            print "-------- Type Error --------"

