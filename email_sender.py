import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from completion_tools import OpenAITools
from dotenv import load_dotenv

load_dotenv()

tools = OpenAITools()


# Define the SMTP server and port
smtp_server = os.environ["SMTP_SERVER"]  # Replace with your Hostinger SMTP server
smtp_port = os.environ["SMTP_PORT"]  # Use 465 for SSL, 587 for TLS

# Sender and recipient details
sender_email = os.environ["EMAIL_ADDRESS"]  # Replace with your Hostinger email
password = os.environ["EMAIL_PASSWORD"]  # Replace with your email password




def send_email(content, receiver_email, apikey):
    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = '[Demo GPT order bot] - Order Confirmation'
    tools.set_api_key(apikey)
    # Email body
    messages = content.copy()
    messages.append(
    {'role':'system', 'content':'create a html summary of the previous product order. Itemize the price for each item'},    
    )
    #The fields should be 1) pizza, price 2) list of toppings 3) list of drinks, include size include price  4) list of sides include size include price, 5)total price '},    

    body = tools.get_completion_from_messages(messages, temperature=0)
    print(body)

    message.attach(MIMEText(body, 'html'))

    # Send the email using the 'with' statement
    try:
        if not receiver_email: raise ValueError
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, password)
            server.send_message(message)
        print('Email sent successfully')
    except ValueError:
        return "Failed to send confirmation, Check your Email"
    except Exception as e:
        return f'Failed to send email: {e}'
       

    return "Confirmation Sent"
