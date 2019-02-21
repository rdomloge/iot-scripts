import smtplib

def send(recipient, sender, subject, msg): 
    print('Sending email from '+sender+' to '+recipient+', regarding "'+subject+'": '+msg);
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("rdomloge@gmail.com", "ubyuqblsziamjuey")

    server.sendmail(sender, recipient, 'Subject: '+subject+'\n\n'+msg)
    server.quit()
