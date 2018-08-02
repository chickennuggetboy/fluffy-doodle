import smtplib
server = smtplib.SMTP('smtp.wellington.com', 587)

#Next, log in to the server
server.login("youremailusername", "password")

#Send mail
msg = "
Hello!" # The /n separates the message from the headers
server.sendmail("alex.kim@consultantemail.com", "thomas.smith@wellington.com", msg)
