from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

webpage = urlopen('http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn')
data = webpage.read()
html_content = date.decode("utf8")

soup = BeautifulSoup(html_content, "html.parser")

print(soup)
