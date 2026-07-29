import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "helloaysha178@gmail.com"
    password = "fywd gywy lpgb zewz"

    receiver = "aysha.fazal001@stud.fh-dortmund.de"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)