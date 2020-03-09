# Flask Python Applications 
Examples of Flask web applications

This folder contains a python Flask web application that I designed for a final project of my web security class
The application was based around the OWASP Top 10 vulnerability cross site scripting, and was meant to repersent
a recent incident here in Canada. The main application was built using python and the Flask library and the sites
around it built using bootscrap as there was a limited time frame with this project so creating a large number
of sites from scratch would have taken up too much time.

Testing the application is very easy, just start the python application and navigate to the localhost on the port
given by Flask. Than logging in using admin@admin.com and admin as the creds, you will be shown a dashbored designed
to repersent a credit site, if you go to the navigation bar and increment the bankingone.html to bankingtwo.html
you will see that you were redirected to another users page without having to log in as that user.

As a security student, I can think of a few ways around this but the most obvious, would be to attached some sort
of authentication to the site that would require you to log in again in attempting to access another record, this way
you could ensure that only the user that was meant to access that record could.