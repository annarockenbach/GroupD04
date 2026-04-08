import smtplib
from email.mime.text import MIMEText

def send_email(receiver_email, player, score, hints, time_taken):
    smtp_server = 'smtp.gmail.com'
    port = 587

    sender_email = 'your_email@gmail.com'
    sender_password = 'your_app_password'

    subject = "Escape Room Game Result"

    body = f"""
Hello {player},

Here are your Escape Room results:

Puzzles solved: {score}
Hints used: {hints}
Time taken: {round(time_taken, 2)} seconds

Better performance means:
- More puzzles solved
- Fewer hints used
- Less time taken

Thanks for playing!
"""

    message = MIMEText(body, 'plain')
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        print("Email sent successfully!")

    except Exception as e:
        print("Error:", e)
