import smtplib
from email.message import EmailMessage

print("Email Sender Script")

sender_email = input("Enter email: ")
password=input("Enter your email password or app password: ")
receiver_email = input("Enter reciever email: ")

subject = input("Enter Subject: ")
message = input("Enter message: ")

email = EmailMessage()
email["From"]=sender_email
email["To"]=receiver_email
email["Subject"]=subject

email.set_content(message)

try:
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login(sender_email,password)
        smtp.send_message(email)
        
    print("\nEmail sent successfully!")

except Exception as e:
    print("Error sending email:", e)


