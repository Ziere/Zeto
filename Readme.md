#Zeto technical interview

## Requirement:
    1 Create a class called Customer which contains the parameters name, email_address, phone_number, and a flag vip_customer.
    2 Define” REST resources and methods to expose and control Customer Model.
    3 Create a form to capture Name, Phone Number, and Email Address.
    4 Validate the fields to ensure that the following rules are met (only BE validation is sufficient):
            a. name: Must be [a-z, A-Z, max 40 chars]
            b. phone_number: [0-9, max 12 digits]
            c. email_address: Must be a valid email format
    5 Submit and validate form over AJAX using REST service created in previous step.
    6 When the information is successfully saved to the Customer records entered so far via rest.
    7 Page should display a count of the occurrences of the customer’s email address in the database.
    8 Use long-polling and two-way data binding in angular to poll for new customers (added from a different tab).
    9 Create a button for each listed user to set or unset the vip_customer flag, via AJAX.
    10 Add a property address to the Customers model.
    11 Create data migrations to add the address field to the model and initialize Customer.address to be Customer.name + '- No address provided'.
    12 Provide UNIT tests for automated testing


## Steps done
    - Create a virtualenv
    - Install django, rest and resourses in a clean Python 2.7 virtualenv
    - Create the model Customer
    - Create the Rest Api for the Customer model
    - Visualization of customers list
    - Use a long polling and 2 way data binding in the customers list

## TODO List
    - Form with Ajax and validation
    - Create the button in the Customers lists to check or uncheck the Vip Status
    - Add the property address to the model
    - Do a data migration
    - Do UNIT tests


## How to check the project
    - Clone it
    - Make the source of the virtualenv
    - Run python manage.py runserver

    - API via browser 'localhost:8000/customer/'
    - Check the user list using Angular 'localhost:8000/customerList/'