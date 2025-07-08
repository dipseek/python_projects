import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Your email credentials
sender_email = "dipseek2005@gmail.com"
receiver_email = "khushishekhawat2104@gmail.com"
password = "ojjo xayn ihxf ctri"  # Use App Password, NOT your Gmail login

# Email subject and body
subject = "Test Email from Python"
body = "Hello,\n\nThis is a test email sent using Python!"

# Create a MIME object
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Attach the email body
message.attach(MIMEText(body, "plain"))

# Send email via Gmail's SMTP server
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Secure the connection
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()
    print("✅ Email sent successfully!")
except Exception as e:
    print(f"❌ Error: {e}")