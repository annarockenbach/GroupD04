import smtplib
from email.mime.text import MIMEText

sender_email = "your_email@gmail.com"
password = "your_app_password"


def send_email(player, score, hints, time_taken, winner):

    subject = "Escape Room Game Results"

    body = f"""
Hello {player},

Here are your Escape Room results:

Score: {score}
Hints used: {hints}
Time taken: {round(time_taken,2)} seconds

Winner: {winner}

Ranking criteria:
1. Highest score
2. Fewest hints used
3. Fastest completion time

Thank you for playing!
"""

    message = MIMEText(body)

    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = sender_email

    try:

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login(sender_email, password)

        server.sendmail(
            sender_email,
            sender_email,
            message.as_string()
        )

        server.quit()

        print("Email sent successfully")

    except:

        print("Email sending failed")
