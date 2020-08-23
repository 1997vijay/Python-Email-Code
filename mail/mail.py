import config
import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
 
# Create DataFrame
df = pd.DataFrame(data)

#defining the html format
html = """\
<html>
  <body>
  <h1 style="color:red;size:20px">Hello {},</h1>
    <p style="color:green">
    Doing some testing on mail.\n\n\n\n\n\n
    </p>
    <p style="color:green">*************************************</p>
    \n\n\n\n\n
    <table style="color:teal;size:60px">
<tr>
    <th>{}</th>
    <th>{}</th>
    <th>Status</th>
  </tr>
  <tr>
    <td>Some</td>
  </tr>
  </table>
  </body>
</html>
""".format("Mamta",df.columns[0],df.columns[1])


part2 = MIMEText(html, "html")   #converting it into html

def send_mail(message):
    try:
        server=smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIl_ADDRESS,config.PASSWORD)
        server.sendmail(config.EMAIl_ADDRESS,config.RECIVER_EMAIL_ADDRESS,message.as_string())
        server.quit()
    except:
        print("Failed!!")

message = MIMEMultipart("alternative")
subg="Test"
message["Subject"] = "{}".format(subg)   #Subject        
message.attach(part2)   #body part
send_mail(message) #calling the function