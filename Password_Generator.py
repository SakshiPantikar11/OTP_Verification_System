import random
import smtplib
from email.message import EmailMessage
import re

# Function to validate the email address
def validate_email(email):
    # Check if the email ends with @gmail.com
    if re.fullmatch(r"[a-zA-Z0-9._%+-]+@gmail\.com", email):
        return True
    return False

# Function to generate a 6-digit OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Function to send OTP to the user's email
def send_otp(email, otp):
    try:

        sender_email = "spofficial2018@gmail.com"  # Sender's email address
        sender_password = "pnji vsll nsqc jzle"  # App password (update to your actual app password)

        # Create the email message
        msg = EmailMessage()
        msg.set_content(f"Your OTP is: {otp}")
        msg["Subject"] = "OTP Verification"
        msg["From"] = sender_email
        msg["To"] = email

        # Send the email via Gmail SMTP server
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)

        print("OTP sent successfully.")
    except Exception as e:
        print(f"Failed to send OTP. Error: {e}")


# Function to verify the OTP
def verify_otp(generated_otp, retries=3):
    for attempt in range(retries):
        entered_otp = input("Enter the OTP sent to your email: ")
        if entered_otp == generated_otp:
            print("Access granted!")
            return True
        else:
            print(f"Incorrect OTP. {retries - attempt - 1} attempt(s) remaining.")

    print("Access denied. Too many failed attempts.")
    return False


# Main function
def main():
    print("Welcome to the OTP Verification System!")
    email = input("Enter your email address: ")

    # Validate email
    if not validate_email(email):
        print("Invalid email address. Only @gmail.com emails are allowed.")
        return

    otp = generate_otp()
    send_otp(email, otp)

    if verify_otp(otp):
        print("Verification successful. Access granted!")
    else:
        print("Verification failed. Please try again later.")


if __name__ == "__main__":
    main()
