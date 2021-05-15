import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

'''class LoggableList(list, Loggable):
    def append(self, x):
        list.append(self, x)
        self.log(x)
        '''
class LoggableList(list, Loggable):
    def append(self, x):
        super(LoggableList, self).append(x)
        self.log(x)
        


