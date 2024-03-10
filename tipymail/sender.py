from email.message import EmailMessage
import smtplib
import ssl
import markdown

class TipyMailSender:
    def __init__(self, sender_email, sender_password):
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_email, subject, body, is_markdown=False):
        em = EmailMessage()
        em["From"] = self.sender_email
        em["To"] = recipient_email
        em["Subject"] = subject

        if is_markdown:
            html_body = markdown.markdown(body)
            em.add_alternative(html_body, subtype="html")
        else:
            em.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.sender_email, self.sender_password)
            smtp.send_message(em)
