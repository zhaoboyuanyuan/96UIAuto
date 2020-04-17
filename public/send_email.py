import smtplib
from email.mime.text import MIMEText            #MIMRText()定义邮件正文
from email.mime.multipart import MIMEMultipart  #MIMEMulipart模块构造带附件
import os
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase

from public import mailText


class send_email():

    #邮件内容为text
    def getText(self):
        #邮件发送内容
        text = mailText.mailText()
        return MIMEText(text, 'plain', 'utf-8')




    #发送一般默认内容为text和添加附件
    def send(self):
        # 发送邮箱服务器
        # smtpserver = 'smtp.qq.com'
        smtpserver = 'smtp.163.com'

        # 发送邮箱用户/密码(登录邮箱操作)
        # user = "guchengcai@163.com"
        # password = "wulian123"

        user = "15951644332@163.com"
        password = "zhaoboyuan54321"

        # user = "1309817607@qq.com "
        # password = "fesnswauckbnjjgc"
        # password = "wmlqmrikrkkwfjfd"


        # 发送邮箱
        sender = user

        # 接收邮箱
        receiver = ["1309817607@qq.com"]
        #注意点：163邮箱会554 DT SMP错误，这时候你只要在发邮件的时候抄送上自己，就再也不会报这个错误了！
        receiver.append("15951644332@163.com")  #自己邮箱
        # receiver.append("yi.liu@wuliangroup.com") #刘毅
        # receiver.append("ren.zhong@wuliangroup.com")  #钟任
        # receiver.append("furong.wang@wuliangroup.com")

        # 发送主题
        subject = '96号文容器自动化测试报告'

        msgRoot = MIMEMultipart()
        # 邮件正文是MIMEText:
        msgRoot.attach(self.getText())
        #发送附件
        msgRoot.attach(self.fuJian())

        msgRoot['Subject'] = subject
        msgRoot['From'] = user
        msgRoot['To'] = ",".join(receiver)
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(user, password)
        smtp.sendmail(sender, receiver, msgRoot.as_string())
        smtp.quit()
        print('邮件发送成功!')

    #添加附件
    def fuJian(self):
        file_new = "D:\\code\\96UIAutoC\\result\\result.html"
        # 添加附件就是加上一个MIMEBase，从本地读取一个html邮件:
        with open(file_new, 'rb') as f:
            # 设置附件的MIME和文件名，这里是png类型:
            mime = MIMEBase('file', 'html', filename='result.html')
            # 加上必要的头信息:
            mime.add_header('Content-Disposition', 'attachment', filename='result.html')
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            # 把附件的内容读进来:
            mime.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(mime)
            # 添加到MIMEMultipart:
            return mime


    #邮件内容为html时
    def getHtml(self):
        file_new = "D:\\code\\96UIAutoC\\result\\result.html"
        f = open(file_new, 'rb')
        mail_body = f.read()
        f.close()
        html = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        return html
#
# if __name__ == '__main__':
#     send_email().send()


