# 3. Suppose we have an access.log web server.
# Write a function that receives file name and returns ten IP addresses from which there were most requests
# Lib https://pypi.org/project/IPy/ could help u working with IPs
#     Write a tests using unittest/pytest.

import pandas as pd
from IPy import IP

logfile = 'access.log'


class TopTen:
    def __init__(self):
        self.filename = ''
        self.res = []

    def getlist(self):
        return self.res

    def setfilename(self, lfile):
        print("--", self.filename)
        self.filename = lfile
        print(self.filename)

    def top_ten_ip(self):
        print(self.filename)
        data = pd.read_csv('access.log', sep=" ", header=None)
        self.res = data[0].value_counts()
        self.res = self.res.reset_index(inplace=False)
        self.res = self.res['index'][:10].to_list()
        for ip in self.res:
            print(IP(ip).strNormal())


def main():
    topten = TopTen()
    topten.setfilename(logfile)
    topten.top_ten_ip()
    print(topten.getlist())


if __name__ == "__main__":
    main()
