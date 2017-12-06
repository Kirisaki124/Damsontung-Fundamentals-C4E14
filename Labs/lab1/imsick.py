from gmail import GMail, Message
from random import *

content1 = '''<p style="text-align: center;"><strong>1đơn xin nghỉ học</strong></p>
<p style="text-align: center;">l&yacute; do l&agrave; :{{sickness}}</p>'''
content2 = '''<p style="text-align: center;"><strong>2đơn xin nghỉ học</strong></p>
<p style="text-align: center;">l&yacute; do l&agrave; :{{sickness}}</p>'''
content3 = '''<p style="text-align: center;"><strong>3đơn xin nghỉ học</strong></p>
<p style="text-align: center;">l&yacute; do l&agrave; :{{sickness}}</p>'''
content_template = [content1, content2, content3]
contents_template = content_template[randint(0,len(content_template)-1)]
# contents = choice(content)
reason1 = ''' em là thánh'''
reason2 = ''' em thích '''
reason3 = ''' em muốn'''
sicknesses = [reason1, reason2, reason3]
sickness = choice(sicknesses)

contents = contents_template.replace("{{sickness}}", sickness)



gmail = GMail("c4e14test@gmail.com","kirari124")
msg = Message("GOD",to = "c4e14test@gmail.com",html = contents)
gmail.send(msg)
