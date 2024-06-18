import smtplib
from email.message import EmailMessage
from enum import Enum
from Vehicle import Vehicle

class EmailCredentials(Enum):
    EMAIL_HOST = 'vrsksmtp4.veriskdom.com'
    EMAIL_PORT = 25
    EMAIL_SENDER ='i44374@verisk.com'


vehicle = 'BMW - T BB C456 - 4'
parked_time = '50 minutes'


def send_receipt_email(function):

    def send_email(*args):
        vehicle_instance = function(*args)
        if not isinstance(vehicle_instance, Vehicle):
            return vehicle_instance

        valid_option = False
        while not valid_option:
            user_option = input('Do you want to send email of this receipt ?? (Y/N) : ').lower()
            if user_option == 'y':
                try:
                    message = f'''
                            <!DOCTYPE html>
                            <html lang="en">
                            <body class="container">
                                <p class="vehicle">Vehicle: {vehicle_instance.brand.brand + ' - '  +vehicle_instance.get_reg_no() + ' - '+ (vehicle_instance.vehicle_type).title()}</p>
                                <p class="time">Park Time: {vehicle_instance.park_time.get_total_park_time()}</p>
                                <p>Paid : Rs {vehicle_instance.get_price_incurred()}</p>
                                <p class="footer"><b>Thank you for using our parking service.</b></p>
                            </body>
                            </html>
                            '''
                    send_email_to_recepient(subject='Parking Receipt', email_message=message, recepient='rikeshmahat.96@gmail.com')


                except Exception as e:
                    print(e)

                valid_option = True

            elif user_option == 'n':
                print('Email cancelled.')
                valid_option = True
            else:
                print('please choose one \'Y\' or \'N\'')

    return send_email


def send_email_to_recepient(subject, email_message, recepient=None):
    message = EmailMessage()
    message['From'] = EmailCredentials.EMAIL_SENDER.value
    message['To'] = recepient
    message['Subject'] = subject

    message.set_content(email_message, subtype='html')

    with smtplib.SMTP(EmailCredentials.EMAIL_HOST.value, int(EmailCredentials.EMAIL_PORT.value)) as server:
        server.starttls()
        try:
            server.send_message(message)
            print('Email sent successfully.')
        except Exception as e:
            print('Failed to send email')
            print(e)




