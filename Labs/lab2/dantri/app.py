from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

#  download dan tri full page
webpage = urlopen("http://dantri.com.vn")
data = webpage.read()
        # print(data)
html_content = data.decode("utf8")
        # print(html_content)



#  analyze region of interest
    #  create beautifulsoup
soup = BeautifulSoup(html_content, "html.parser")
#  prettify: make the code easier to see
# print(soup.prettify())

ul = soup.find("ul", "ul1 ulnew")
# print(ul.prettify())
li_list = ul.find_all("li")
# li_list is a list type
# for li in li_list:
#     print(li.prettify())
#     print("*" *20)

# li = li_list[0]

news_list = []
for li in li_list:
    h4 = li.h4     #find h4
    a = h4.a       #find a
    # a = li.h4.a
    news = {
        "title": a.string,
        "link": "http://dantri.com.vn" +  a["href"]
    }
    news_list.append(news)
    # print(news)
print(news_list)

# print(a.string)    # lay phan string doan cuoi the
# print("http://dantri.com.vn/" + a["href"])

pyexcel.save_as(records = news_list, dest_file_name = "dantri.xlsx")

#  extract data
