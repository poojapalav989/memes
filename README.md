
## How To Setup On Linux
1. Clone This Project 
2. Go to Project Directory 
3. Create a Virtual Environment `virtualenv env`
4. Activate Virtual Environment `source env/bin/activate`
5. Install Requirements Package `pip3 install -r requirements.txt` and pip3 install requests
6. Migrate Database `python3 manage.py migrate`
7. Create Super User `python3 manage.py createsuperuser`
8. Finally Run The Project `python3 manage.py runserver`