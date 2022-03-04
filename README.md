# Github_Profile_Analyzer

This is a project that is going to help you understand more about your github activity. This project is not completed and this read me file takes to you to the latest development.

# Dependencies

[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
django = "*"


[dev-packages]

[requires]
python_version = "3.9"

# How to run
first go to the GotProApp folder and open the views.py
after that replace the github username in to your choice in the get_user function
then go to the terminal and run python manage.py runserver
last in your brower write the following url after the host/
    profiledetails/expand  displays all the Jsonresponce content in the browser
    profiledetails/profile  filters the content into email, following, followers, bio
    profiledetails/intro  renders a template to fill your github account to remove the manuall insertion of your githubuser . not complete
