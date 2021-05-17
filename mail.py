from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.application import MIMEApplication
import os
import pandas as pd

account = "danny871005"


def sender(reciever , gamil ):

    content = MIMEMultipart()                                               #建立MIMEMultipart物件
    content["subject"] = "反思二"                                            #郵件標題
    content["from"] = account
    content["to"] = gamil
    content.attach(MIMEText("反思二的回饋，有任何問題都在回信跟我說"))                                        

    file = MIMEApplication(open('C:/Users/user/Desktop/反思二/'+reciever ,'rb').read())
    file.add_header('Content-Disposition', 'attachment', filename=reciever)
    content.attach(file)


    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:           # 設定SMTP伺服器
        try:
            smtp.ehlo()                                                     # 驗證SMTP伺服器
            smtp.starttls()                                                 # 建立加密傳輸
            smtp.login("danny871005@gmail.com", "pcgjnbsuqhfyhwtn")         # 登入寄件者gmail
            smtp.send_message(content)                                      # 寄送郵件
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)



if __name__ == '__main__':
    
    path = 'C:/Users/user/Desktop/反思二'
    filelist = os.listdir(path)
    mail = pd.read_csv("student_mail.csv")

    for file in filelist:
        temp = file.split("_")
        name = temp[3][0:3]
        reciever = mail.loc[mail['name']==name]
        #print(name)
        
        a = str(reciever['mail']).split("Name")
        b = a[0].split(" ")
        c = b[-1]

        print(str(file),c)
        sender(str(file),c)
