import pandas as pd
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load DataFrame
try:
    df = pd.read_excel("Task.xlsx")
    print(df)
except FileNotFoundError:
    print("Error: 'Task.xlsx' not found.")
    exit()

# Get today's date
today = datetime.datetime.now()
today_month = today.month
today_day = today.day

# Iterate through rows in DataFrame
for index, row in df.iterrows():
    try:
        due_date = pd.to_datetime(row['DueDate'])  # Assuming the due date is in 'DueDate' column
        task_name = row['TaskName']  # Assuming 'TaskName' column has the task's name
        email = row['Email']         # Assuming 'Email' column has the recipient's email

        if due_date.month == today_month and due_date.day == today_day:
            print(f"Today is the due date for: {task_name}!")
            
            # Send Email
            def send_email(receiver_email, task_name):
                sender_email = "jublinerjk@gmail.com"
                password = "otpt pgwc dhui sfwq"  # Use environment variables for security
                
                message = MIMEMultipart()
                message["From"] = sender_email
                message["To"] = receiver_email
                message["Subject"] = "Task Reminder!"
                
                body = (
                    f"Hi,\n\nThis is a reminder to complete the task: {task_name}.\n\n"
                    f"Have a great day!\n\nBest Regards,\nYour Python Script"
                )
                message.attach(MIMEText(body, "plain"))

                try:
                    with smtplib.SMTP("smtp.gmail.com", 587) as server:
                        server.starttls()
                        server.login(sender_email, password)
                        server.sendmail(sender_email, receiver_email, message.as_string())
                    print(f"Task reminder sent successfully to {receiver_email}!")
                except smtplib.SMTPException as e:
                    print(f"Error sending email to {receiver_email}: {e}")

            send_email(email, task_name)
    except Exception as e:
        print(f"Error processing row {index}: {e}")
