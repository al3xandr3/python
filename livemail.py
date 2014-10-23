import smtplib

# http://www.nixtutor.com/linux/send-mail-through-gmail-with-python/
# http://docs.python.org/2/library/email-examples.html

def mail(toaddrs, subj, msg, server, port, username, password):
    message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: <SUBJ>
<BODY>
"""

    # replace
    message = message.replace("<SUBJ>", subj)
    message = message.replace("<BODY>", msg)

    # The actual mail send
    server = smtplib.SMTP(server, port)
    server.starttls()
    server.login(username, password)
    server.sendmail(username, toaddrs, message)
    server.quit()


if __name__ == "__main__":
    
    if len(sys.argv) < 8:
        sys.exit("Use: python livemail.py 'username@live.com' 'subj' 'file.html' 'smtp.live.com' '587' 'username@live.com' '*******'")

    import sys
    # Open file
    fo = open(sys.argv[3], "rb")
    msg = fo.read()
    mail(sys.argv[1], sys.argv[2], msg, sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])

#> python livemail.py 'username@live.com' 'subj' 'file.html' 'smtp.live.com' '587' "username@live.com" "********"
