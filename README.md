# intive-python-test

Challenge for backend developers

Using the tools (language, framework, etc.) of your preference:
Expose a REST API with a single endpoint. This endpoint should receive a user_id field by
POST Http method. The endpoint should expect that field on the request body and should not
accept parameters on URL.
Using the user_id you should obtain a user from randomuser.me API. The URL to obtain that
user information is of the form: https://randomuser.me/api/?ud=<user_id>
Your endpoint should return the following information about the user that you get from
randomuser.me: Lastname, Firstname, E-Mail, Picture, Address. The Address should have two
components: Number and Street the first one and City - State the second one.
The response from your endpoint should look like:
user: {
lastname: "LastName",
firstname: "FiestName",
image: "http://image.url"
Address: {
street: "123 false street",
city: "City - State"
}
}
}
We expect to receive your code in a git repository with a README with all the necessary
information to up your API and test it.

--------------------------------------------------------------------------------------------------------
In order to run this project you will have to install:

- python
- postman
- pipenv (which is the Python equivalent of npm, more information here https://docs.pipenv.org/en/latest/install/)
- tornado, requests, json (python modules that have to be reinstalled inside pipenv using 'pipenv install + modulename')

After setting the environment and cloning the project run the app using the command 'pipenv run python app.py' inside the project
folder, and test the post request in postman sending a post request to the url http://localhost:46546 with the key 'user_id' and any value
of your preference. You will receive a json with the user information as shown in the picture below. 
