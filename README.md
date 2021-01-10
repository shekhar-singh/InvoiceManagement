# InvoiceManagement
Assignment

Customer can upload a PDF file, track a document’s digitization status and if document is digitized return mock data.
Staff member can manually add digitized structure and can mark a document as “digitized”

This project uses django.

Clone this repository using this command:-

  `git clone https://github.com/shekhar-singh/InvoiceManagement.git`
  
# Getting up and running.
 Get inside the InvoiceManagement using this command.
 
 `cd InvoiceManagement` 

This steps below will get you up and running with a local development environment. We assume you have the following installed:

  - pip
  - virtualenv

First make sure to create and activate a virtialenv, then open a terminal at the project root and install the requirements for local development.

    $ pip install -r requirements.txt

Create .env file in the root project directry and set these values

SECRET_KEY='SOME KEY'
AWS_ACCESS_KEY_ID='SOME KEY'
AWS_SECRET_ACCESS_KEY='SOME KEY'
AWS_STORAGE_BUCKET_NAME='SOME KEY'
AWS_S3_REGION_NAME='SOME KEY'

	$ python manage.py makemigrations
	$ python manage.py migrate
	$ python manage.py runserver

Test the endpoint using postman 
Find the sample request and response from the sample_request_responce.txt in the root directory