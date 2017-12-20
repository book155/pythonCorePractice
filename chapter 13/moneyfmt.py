class MoneyFmt(object):
    'finish a,no finish bcd'
    TestValue = 0
    def __init__(self,value=0.0):
        self.value=float(value)
    def update(self,value=None):
        print 'before modify:' + str(self.value)
        self.value = value
        print 'after modify:' + str(self.value)
        return self.value
    def dollarize(self,value):
        arrayStr = str(value)
        if (arrayStr[0] == '-'):
            result = '-' + '$' + arrayStr[1:]
        else :
            result = '$' + arrayStr
        return result
    def __nonzero__(self):
        if self.value != 0:
            return True
    def __dirClass__(self):
            return dir(MoneyFmt)