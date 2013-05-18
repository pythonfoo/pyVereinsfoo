from numpy.f2py.auxfuncs import throw_error
import uuid
import datetime


class DataObj(object):
    def __init__(self):
        self._uid = uuid.uuid4()
        self._readable = False
        self._writeable = False
        self._lastedit = datetime.datetime.now()

    def uid(self):
        #if not type(dataObj.uid) == uuid.UUID:
        #    print "-------- Type Error --------"
        return self._uid

    def readable(self):
        #if not type(dataObj.readable) == bool:
        #    print "-------- Type Error --------"
        return self._readable

    @property
    def writable(self):
        return self._writeable

    @writable.setter
    def writable(self, value):
        #if not type(dataObj.writable) == bool:
        #    print "-------- Type Error --------"
        #dataObj.writeable = True
        if type(value) == bool:
            self._writeable = value
        else:
            raise Exception("Exception: Type miss match. Only BOOL allowed")

    @property
    def lastedit(self):
        return self._lastedit

    @lastedit.setter
    def lastedit(self, value):
        #dataObj.lastedit = datetime.datetime.now()
        #if not type(dataObj.lastedit) == datetime.datetime:
        #    print "-------- Type Error --------"
        #raise Exception("Exception: READ ONLY PROPERTY")
        print('read-only property!')
