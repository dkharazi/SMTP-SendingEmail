# Import modules
import smtplib
import csv
import sys
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set traceback
sys.tracebacklimit = 0

# Sender email
SENDER_ADDRESS = 'samplesender@example.com'
PASSWORD = 'pass!'

# Reads in text for an email body
def read_template(filename):
    with open(filename, 'r') as template_file:
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
    if len(sys.argv) == 3:
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
    try:
    	server.login(SENDER_ADDRESS, PASSWORD)
    except smtplib.SMTPAuthenticationError as e:
    	server.quit()
    	print("\nEither ensure your email and password are entered correctly, or change the security settings on your sender email.\n")
    	raise Exception(e)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        # Create a message
        msg = MIMEMultipart() 

        # Add the name to the message template
        message_mod = message.substitute(PERSON_NAME=name.title())

        # Setup the parameters of the message
        msg['From'] = SENDER_ADDRESS
        msg['To'] = email
        msg['Subject'] = "Input a test subject."
        
        # Add in the message body
        msg.attach(MIMEText(message_mod, 'plain'))
        
        # Send the message via the server set up earlier.
        text = msg.as_string()
        server.sendmail(SENDER_ADDRESS, email, text)
        del msg
        
    # Terminate the SMTP session and close the connection
    server.quit()
