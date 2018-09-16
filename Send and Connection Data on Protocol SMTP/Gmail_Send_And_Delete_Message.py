# =============================================================================
# Instrustions for gmail
# 1. Step = Unlock IMAP/POP in Settings gmail
# https://support.google.com/mail/answer/7126229?hl=ru&visit_id=636721368008336639-936248371&rd=2
# 2. Step = Create Password For App ( This setting is not available for accounts
# with 2-Step Verification enabled)
# https://support.google.com/accounts/answer/185833?hl=en
# =============================================================================
# https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python
# =============================================================================


import smtplib
import socket
import sys
import email
import imaplib
from email.parser import HeaderParser
import poplib

# =============================================================================
# SET EMAIL LOGIN REQUIREMENTS
# =============================================================================
GMAIL_USER = 'name@gmail.com'
GMAIL_APP_PASSWORD = 'password_app'
GMAIL_IMAP_SERVER = 'imap.gmail.com'
GMAIL_SMTP_PORT = 465
GMAIL_IMAP_PORT = 993

GMAIL_FOLDER_NAME = '"[Gmail]/Sent Mail"'

sent_from = GMAIL_USER
sent_to = 'name_sent@gmail.com'

# =============================================================================
# SET THE INFO ABOUT THE SAID EMAIL
# =============================================================================

def message_struct(sent_from, sent_to):
    msg = "\r\n".join([
      "From: {}",
      "To: {}",
      "Subject: Just a message",
      "dfghjkl",
      "Why, oh why"
      ]).format(sent_from, sent_to)
    return msg

# =============================================================================
# SEND EMAIL OR DIE TRYING!!!
# Details: http://www.samlogic.net/articles/smtp-commands-reference.htm
# =============================================================================
def connect_to_send(email_imap, port, email, password_app):
      connect = smtplib.SMTP_SSL(host=email_imap, port=port)
      connect.login(email, password_app)
      return connect

def connect_for_delete(email_imap, port, email, password_app):
    connect = imaplib.IMAP4_SSL(host=email_imap, port=port)
    connect.login(email, password_app)
    return connect

try:
    server_to_send = connect_to_send(GMAIL_IMAP_SERVER,
                     GMAIL_SMTP_PORT,
                     GMAIL_USER,
                     GMAIL_APP_PASSWORD)
    msg = message_struct(sent_from=sent_from, sent_to=sent_to)
    server_to_send.sendmail(sent_from, sent_to, msg)
    print('Message Sent!')
    #server_to_send.close()
except Exception as exception:
    print("Error: %s!\n\n" % exception)


try:
    server = connect_for_delete(GMAIL_IMAP_SERVER,
                     GMAIL_IMAP_PORT,
                     GMAIL_USER,
                     GMAIL_APP_PASSWORD)
    #server.sendmail(sent_from, sent_to, msg)
    # get list of mailboxes
    mailparser = HeaderParser()
    list = server.list();
    server.select(GMAIL_FOLDER_NAME)
    typ, data = server.search(None, 'ALL')
    uids = data[0].split()
    for num in uids:
        try:
            resp, data_second = server.fetch(num, '(RFC822)')
            data_decode = data_second[0][1].decode()
            msg = mailparser.parsestr(data_decode)
            print (msg['From'],'========',msg['Date'],'====',msg['Subject'])
            if msg['Subject'] == 'Just a message':
                server.store(num, '+FLAGS', '\\Deleted')
                print ('Deleted\n\n')
        except Exception as exception:

            print ("Error: %s!" % exception)
            print ('Id:', num)
    server.expunge()
    print('Count:',len(uids))

except Exception as exception:
    print("Error: %s!\n\n" % exception)

server.close()
