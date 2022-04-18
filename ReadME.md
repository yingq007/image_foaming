INTRODUCTION
---------------
The images foaming project is to let users tag images from their experiment as foaming or not. 
The tagged images are stored in user's profile.
A quick view for this project showingcase can be found here: https://www.loom.com/share/5fde804a19ba48e7829c0e9b996c9ec5

REQUIREMENTS
---------------------
To run the code, Python must be installed (Python 3.8.9).
Flask web framework was used to build server and SQLAlchemy were used to store data. Below are requiements in requiements.txt that need to be installed before running the code:
Flask==2.0.1
Flask-SQLAlchemy==2.5.1
psycopg2-binary==2.8.6
SQLAlchemy==1.4.1
Flask-DebugToolbar==0.11.0
a virturl enviornment is also created 

RUNNING THE SCRIPT
---------------------
1. Create a virtual enviornment, in the terminal, run:
virtualenv env
source env/bin/activiate
2. Install this porject's dependencies from requirment.txt, in the terminal, run:
pip3 install-r requirements.txt
3. Create a PostgreSQL database for this project, in the terminal, run:
createdb foams
4. create tables in the database, in the terminal run:
python3 -i model.py
db.create_all()
5. Seed the Database:
python3 seed_database.py
6. Start the Server:
Run server.py 
open http://localhost:5000 in your browser

