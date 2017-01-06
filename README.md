# admin-interface
Prerequisites - 1.) Python 2.7 or later
                2.) Django 1.10 or latest
                3.) MySQL
Install django in ubuntu using pip:  pip install django
Install MYSQL in ubuntu : sudo apt-get install mysql-server(set root password when it prompts)
                          Check mysql service is running or not by issuing: service mysql status
                          To start service issue: service mysql start
DB Creation:
  -> Login to mysql : mysql -u root -p (press enter.It will ask for root password that we set when installing mysql)
  -> Create a db with name admin_interface.command to create : create database admin_interface;
  
Running application:
  -> Move to admin_interface folder and issue python manage.py runserver to start the application to run.Now application will run in localhost with port 8000
  -> Sometimes when we run python manage.py runserver it will give warnings saying changes in models were observed run migrations to save the changes to db.Run the migrations so that the models(tables) will get created in db.Command: python manage.py migrate
  -> Open 127.0.0.1:8000 in browser 
  
  
  

