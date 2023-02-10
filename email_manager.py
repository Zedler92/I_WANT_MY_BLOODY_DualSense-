import smtplib
import ssl


def send_email(price, link):
    global server
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "zedler92@gmail.com"
    password = "yuznmgegfrdolbed"
    message = f"""
    Subject: The price of the DualSense is low!
    \n\n    
    The price for your DualSense is {price}. Link : \n{link}"""
    receiver_email = "zedler92@gmail.com"
    # Create a secure SSL context
    context = ssl.create_default_context()
    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()