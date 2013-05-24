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

def tobe_str(prop):
    "to be or not to be String"
    if not type(prop) == "str":
        print "-------- Type Error --------"
    prop = "This ist just a simple and short Text"
    with pytest.raises(TypeError):
        prop = 1
    with pytest.raises(TypeError):
        prop = 2.2345

def tobe_int(prop):
    "to be or not to be int"
    if not type(prop) == "int":
        print "-------- Type Error --------"
    with pytest.raises(TypeError):
        prop = "This ist just a simple and short Text"
    prop = 1
    with pytest.raises(TypeError):
        prop = 2.2345


class TestMandatory():
    def test_mdy_Address_isinstance_DataObj(self):
        import venlib
        from venlib.base.mandatory.address import Address

        if not isinstance(Address, venlib.base.venbase.DataObj):
            print "-------- Dependency Fail --------"

    def test_mdy_Addresse(self):
        from venlib.base.mandatory.address import Address

        adr = Address()
        
        tobe_str(adr.name)
        tobe_str(adr.first_name)
        tobe_str(adr.companyname)
        tobe_str(adr.priv_streat)
        tobe_str(adr.priv_house_nr)
        
        # TODO: This test has to be extendet to countrycode Object
        tobe_str(adr.priv_countrycode)
        tobe_str(adr.priv_country)
        tobe_str(adr.bus_streat)
        tobe_str(adr.bus_house_nr)
       
        # TODO: This test has to be extendet to countrycode Object
        tobe_str(adr.bus_countrycode)
        tobe_str(adr.bus_country)

        # TODO: This test has to be extendet to countrycode Object
        tobe_str(adr.postbox_countrycode)

        # TODO: How did postoffice Addresses work world wide
        tobe_str(adr.postbox_address)
        tobe_str(adr.weburl)
        tobe_str(adr.position)
        
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
        
        tobe_str(phone.number)
        # TODO: Phone Typologic in an Helper to fill here
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
        tobe_str(email.email_address)
        tobe_int(email.typ) 

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
        
        tobe_str(notes.shorttxt)
        tobe_str(notes.longtxt)
        tobe_int(notes.typ)

        if not type(notes.noteID) == uuid.uuid:
            print "-------- Type Error --------"
        noteid = notes.noteID
        # TODO: do not know if this works
        with pytest.raises(AttributeError):
            notes.noteID = uuid.uuid4()
        
        notes.adrID = uuid.uuid4()
        if not type(notes.adrID) == uuid.uuid:
            print "-------- Type Error --------"

