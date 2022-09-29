import csv
from os import walk
import os
import glob

from os.path import isfile, join

class csv_reader:
    def __init__(self):
        return
    def csv_openfile(self, path, filename):
        self.path = path
        self.filename = filename
        with open((path+filename), 'r', newline='') as csvfile:
            inlines = csv.reader(csvfile, delimiter='', quotechar='"')
            # for line in inlines:
        return

    # csv file을 해당 폴더에서 모두 읽어와서 filelist에 저장하고 list를 리턴한다.
    def csv_listfiles(self, path): # folder를 읽어서 csv 파일 리스트를 리턴한다.
        filelist = []
        self.path = path
        filelist = glob.glob(path + './*.csv')
        return filelist
    def csv2xls(self):
        return
    def csv_select(self):
        return
    def csv_writfile(self):
        return