from gmail import *
from datetime import *

content1 = '''<p style="text-align: center;"><strong>1đơn xin nghỉ học</strong></p>
<p style="text-align: center;">l&yacute; do l&agrave; :1asd</p>'''

now = datetime.now()
while True:
    if now.hour >= 18 and now.minute == 28 and now.second >= 1:
        gmail = GMail("c4e14test@gmail.com","kirari124")
        msg = Message("god",to = "c4e14test@gmail.com", html = content1 )
        gmail.send(msg)
        break
