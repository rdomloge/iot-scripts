import smtplib

def send(recipient, sender, subject, msg): 
    print('Sending email from '+sender+' to '+recipient+', regarding "'+subject+'": '+msg);
    try:

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("rdomloge@gmail.com", "ubyuqblsziamjuey")

        server.sendmail(sender, recipient, 'Subject: '+subject+'\n\n'+msg)
        server.quit()
    except IOError:
        print('Looks like the network may be down');
    except:
        print('Failed to send email');
