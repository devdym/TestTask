import pytest
from TopTen import TopTen
logfile = 'access.log'

def test_top_ten_ip():
    res = ['66.249.73.135', '46.105.14.53', '130.237.218.86', '75.97.9.59', '50.16.19.13', '209.85.238.199', '68.180.224.225', '100.43.83.137', '208.115.111.72', '198.46.149.143']
    topten = TopTen()
    topten.setfilename(logfile)
    topten.top_ten_ip()

    assert topten.getlist() == res
