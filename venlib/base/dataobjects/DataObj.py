import uuid
import datetime


class DataObj(object):
    def __init__(self):
        self._uid = uuid.uuid4()
        self._readable = False
        self._writeable = False
        self._lastedit = datetime.datetime.now()
        self._lastEditor = None
        self._history = []

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

    @property
    def lastEditor(self):
        return self._lastEditor

    @lastEditor.setter
    def lastEditor(self, value):
        print('read-only property!')

    @property
    def undoable(self):
        return self.hasHistory

    @undoable.setter
    def undoable(self, value):
        print('read-only property!')

    @property
    def hasHistory(self):
        return len(self._history)

    @hasHistory.setter
    def hasHistory(self, value):
        print('read-only property!')

