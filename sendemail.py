# Import modules
import smtplib
import csv
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Sender email
SENDER_ADDRESS = 'my_address@example.com'
PASSWORD = 'mypassword'

# Reads in text for an email body
def read_template(filename):
    with open(filename, 'r', encoding = 'utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)
    
# Reads in contacts for an email
def get_contacts(filename):
    names = []
    emails = []
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            names.append(row[0])
            emails.append(row[1])
    return names, emails

if __name__ == '__main__':
    # Reads in file name used for body
    if len(sys.argv) == 2:
        contacts = sys.argv[1]
        body = sys.argv[2]
    else:
        sys.exit("A file name is required for the program.")
    
    # Reads in files used for contacts and body
    names, emails = get_contacts(contacts)
    message = read_template(body)
    
    # Connect to the mail server
    server = smtplib.SMTP(host = 'smtp.gmail.com', port = 587)
    server.starttls()
    server.login(SENDER_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        # Create a message
        msg = MIMEMultipart() 

        # Add the name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Setup the parameters of the message
        msg['From'] = SENDER_ADDRESS
        msg['To'] = email
        msg['Subject'] = "Input a test subject."
        
        # Add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        # Send the message via the server set up earlier.
        s.send_message(msg)
        del msg
        
    # Terminate the SMTP session and close the connection
    server.quit()
