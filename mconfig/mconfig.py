import os
import platform

class config:
    VERSION = ""
    CONFILE = ""
    CONPATH = ""
    PLATFORM = ""

    def version(self):
        f = open(self.CONPATH,'r')
        self.VERSION = f.readline()
        f.close()
    
    def getconfile(self):
        self.CONFILE =  os.path.abspath(__file__)

    def getconpath(self):
        self.CONPATH = self.CONFILE.replace("mconfig.py",'ver.txt')

    def getplatform(self):
        self.PLATFORM = platform.system()
    def __init__(self):
        self.getconfile()
        self.getconpath()
        self.getplatform()
        self.version()
