import unittest
from tipymail.sender import TipyMailSender
from credentials import credentials


class TestTipyMailSender(unittest.TestCase):
    def test_send_email(self):
        # Set up your test email addresses and credentials here
        sender_email = credentials["sender_email"]
        sender_password = credentials["app_password"]
        recipient_email = credentials["recipient"]
        subject = "Test Subject"
        body = "Test Body"

        sender = TipyMailSender(sender_email, sender_password)
        sender.send_email(recipient_email, subject, body)

        # Add assertions as needed
        # For example, check if the email was sent successfully


if __name__ == '__main__':
    unittest.main()
