# CerenWebsite

## Build With
  * Python Django
  * HTML,CSS,js,Bootstrap
 
 
## How to Run

Download and Install Python required version.

  Before the following steps make sure you have git installed on your system
  you can clone using git
  
      git clone https://github.com/jithinjose0/CerenWebsite.git

Read about virtualenv in Python. Create a virtual environment for your project.

      pip install virtualenv
      
      virtualenv virtualenv_name
Activate the environment in cmd.

    virtualenv_name\scripts\activate

Run the command in console pip install -r requirements.txt go to that directory and run the above command. 
This command will install the necessary packages required to run the project.

    pip install -r requirements.txt
    
Go the the directory where manage.py file is present. Run following commands in the cmd

    python manage.py makemigrations
    
    
    python manage.py migrate
    
    
    python manage.py runserver
    
See your project is running on your local host 

    http://127.0.0.1:8080
