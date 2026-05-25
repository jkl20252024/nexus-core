import smtplib
from email.mime.text import MIMEText


EMAIL = "technodroid40@gmail.com"
APP_PASSWORD = "wopx cysg tbbc sazk"


def send_email(to_email, subject, body):

    msg = MIMEText(body)

    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = to_email

    try:

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login(
            EMAIL,
            APP_PASSWORD
        )

        server.sendmail(
            EMAIL,
            to_email,
            msg.as_string()
        )

        server.quit()

        return {
            "success": True,
            "email": to_email
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }