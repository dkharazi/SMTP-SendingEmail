## Overview

Frequently, we'll have the names and email addresses of some people that need to receive an automated message. In order to send them this message, we need all of the contact information for the recipients, the body and subject that will be sent, and any headers that are required. For simplicity’s sake you can store the contact details in a file rather than a database. You can also store the template of the message you wish to send in a file. The smtplib module of Python is basically all you need to send simple emails, without any subject line or such additional information. But for any actual emails, you do need a subject line and additional information — maybe even pictures and attachments. 

## Requirements

1. Include the text files in the same directory as the python file.
2. Run the python file using the command line, while including the "body.txt" file as the first argument and the "contacts.csv" file as the second argument.
