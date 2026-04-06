import smtplib
from email.mime.text import MIMEText

sender_email = "abiloronalyn21@gmail.com"
password = "ztus dlhq gtsi nwhg"

def send_email(player, score, hints, time_taken):

    subject = "Escape Room Game Result"

    body = f"""
Hello {player},

Here are your Escape Room results:

Puzzles solved: {score}
Hints used: {hints}
Time taken: {round(time_taken,2)} seconds

Better performance means:
More puzzles solved
Fewer hints used
Less time taken

Thanks for playing!
"""

    message = MIMEText(body)

    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = sender_email

    try:

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login(sender_email, password)

        server.sendmail(sender_email, sender_email, message.as_string())

        server.quit()

        print("Email sent successfully")

    except:

        print("Email failed")