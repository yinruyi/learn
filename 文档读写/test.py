#coding:utf-8
import sys
import os
#sys.path.append("../")

class pretreatment():
    """预处理"""
    def __init__(self):
        pass
    def read_txt(self,txtPath,coding = 'utf-8'):
        import codecs
        f = codecs.open(txtPath,'r',coding).readlines()
        dataset = []
        for line in f:
            line = line.replace("\r\n","")
            line = line.replace("\n","")
            dataset.append(line)
        return dataset

class DataAnalysis(pretreatment):
    pass

if __name__=='__main__':
    print sys.path
    abspath = os.getcwd()
    print abspath
    data = DataAnalysis().read_txt(abspath+'//test//test.txt')
    print data