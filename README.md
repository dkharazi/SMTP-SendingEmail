## Overview

Frequently, we'll have the names and email addresses of some people that need to receive an automated message. In order to send them this message, we need all of the contact information for the recipients, the body and subject that will be sent, and any headers that are required. For simplicity’s sake you can store the contact details in a file rather than a database. You can also store the template of the message you wish to send in a file. The smtplib module of Python is basically all you need to send simple emails, without any subject line or such additional information. But for any actual emails, you do need a subject line and additional information — maybe even pictures and attachments. 

## Requirements

1. The code was written in Python 2.7, so make sure you run the code with the same Python distribution.
2. Include the text files in the same directory as the Python script.
3. Run the python file using the command line, while including the "contacts.csv" file as the first argument and the "body.txt" file as the second argument.
4. Change the "body.txt" file to your preferred email body, and include your preferred contacts in the "contacts.csv" file.
5. Ensure that you follow the typical formatting rules when making adjustments to the "body.txt" and "contacts.csv" files.
6. Insert your sender email and password into the lines that have been marked for you in the code.
7. Either ensure that the sender email is from gmail, or modify the SMTP host on line 48.
