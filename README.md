# Flask Starter Template

### This is a starter template for Flask projects.
##### It includes the following features:
 + Role based authentication with __Flask-Login__ which can be edited on ```rbac.py```
 + MySQL database connection with __mysqlclient__
 + ORM support with __Flask-SQLAlchemy__
 + .env file support with __python-dotenv__
 + Powerful template engine __Jinja2__
 + Database migration support with __Flask-Migrate__

##### Pre-requisites:
 + Python 3.6 or above
 + MySQL 5.7 or above
 + IDE of your choice

##### To use this template:
1. Clone this repository using git clone <repo_url>
2. Unzip the folder and open it in your favorite IDE like PyCharm, VSCode, etc.
3. Open the terminal and create a virtual environment using ```python -m venv venv```
4. Run ```pip install -r requirements.txt``` to install all the dependencies.
5. Create a .env file and add the following variables:
    + ```SECRET_KEY``` - A secret key for your application.
    + ```SQLALCHEMY_DATABASE_URI``` - The URI for your MySQL database.
        + Example: ```mysql://<username>:<password>@localhost:3306/<db_name>```
    + ```SQLALCHEMY_TRACK_MODIFICATIONS``` - Set it to ```False```.
6. 
