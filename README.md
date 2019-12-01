# Entry-Management-System


Entry Management software (GUI application) with email and sms facility. The software starts with the entry of the visitor email address which will be furthur used as a key to identify the visitor along with the email entry there are two buttons one for CheckIn and one for CheckOut

# If CheckIn is pressed : 
1. A form to fill the details appear in the frontend with a submit button whereas at the back end, once the user enters the information in the form, the backend should store all of the information with time stamp of the entry i.e checkin time. After clicking the Submit Button an email and an SMS should be triggered to the host informing him of the details of the visitor

# If CheckOut is pressed :
1. After validating the key the Checkout time if filled in the database and this should trigger an email to the guest with the complete form which should include:
# Details Required: 
1. Name
2. Phone No
3. Check-in time
4. Checkout time
5. Host name
6. Address visited.

# Installation
Use the package manager pip3 to install dependencies.

pip3 install -r requirements.txt
You'll need to update your database details in settings.py -

DATABASES = {<br />
    'default': {<br />
        'ENGINE': 'django.db.backends.postgresql_psycopg2',<br />
        'NAME': 'db_name',<br />
        'USER': 'username',<br />
        'PASSWORD': 'password',<br />
        'HOST': 'localhost',<br />
        'PORT': '',<br />
    }<br />
}<br />
Then you'll have to update the email host user and password in settings.py -<br />

EMAIL_HOST_USER = 'email_id@host.com'<br />
EMAIL_HOST_PASSWORD = 'your password'<br />
And finally, update the twilio SID and token in settings.py so that sms function works properly -<br />

TWILIO_ACCOUNT_SID = 'your sid'<br />
TWILIO_AUTH_TOKEN = 'your token'<br />
