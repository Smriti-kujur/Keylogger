import smtplib, ssl

def send_email(sender_email, password, message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "ishikujur11@gmail.com"
    password = "S0f9_M4u8@R0c7"
    receiver_email = "ishikujur11@gmail.com"

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        print(e) 
    finally:
        server.quit() 