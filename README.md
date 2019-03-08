Travis-CI status on Master Branch:  [![Build Status](https://travis-ci.org/ucsb-cs48-w19/4pm-gold-scheduler.svg?branch=master)](https://travis-ci.org/ucsb-cs48-w19/4pm-gold-scheduler)
# Project Gold Scheduler
[Link to Gold Scheduler](https://protected-depths-20813.herokuapp.com)
## Project summary
Gold Scheduler helps UCSB students plan their upcomming quarter by making easier for them to visualize multiple potential schedules. User can use dropdown bottom to choose the classes and sections directly. Also, they can select the classes available for the quarter selected and delete class just like in GOLD. The calendar will show them the conflict of classes, so they can manage the scheduler by themselves easily.

### One-sentence description of the project
A webapp for UCSB students to help them plan their fututre quarter schedules

### Additional information about the project
The user can make their multiple schedules on one page. Easy for them to register class and plan their class process. 

### Prerequisites
1. pip
2. python3 
3. flask 
4. postgreSQL
5. gunicorn (for Heroku deployment)

## Installation
1. Fork the repo
2. Install [pip](https://pip.pypa.io/en/latest/installing/)
3. Install PostgreSQL on your machine: [Mac](https://postgresapp.com/) | [Windows](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads#windows)
4. Install virtual environment:  `$ pip install virtualenv`
5. Under your project file: `$ virtualenv venv`
6. Active virtualenv: `$ source venv/bin/activate`
7. Install requirements from requirements.txt: `$ pip install -r requirements.txt`
8. Database setup:
    *  You need a heroku accont. Then, you need to create a project on heroku. Under the project, add-on Heroku Postages.
    * Under your Heroku Postages, you need to go to setting->view credentials... Copy Hero CLI
    * Open your terminal, paste the your Heroku CLI. Now you should connect to your database.
    * Open the routes.py, replace {os.environ['DATABASE_URL']} to your database info. [Reference](https://devcenter.heroku.com/articles/jawsdb#using-jawsdb-with-python-django) 
    * In your python console: 
	    * `>>>from routes import db` 
	    * `>>>db.create_all()`
	    *  Now, you have your data table created in database.
    * Back to the terminal:
	    * Select your table: `$ select * from Public.”yourTableName”`
	    * Download the class data(csv file) is from data file on github.
	    * Import the data: `$ \copy Public."yourTableName” FROM 'path of the csv file' DELIMITER ',' csv HEADER;`
9. To start the app:
    * `$ export FLASK_APP=routes.py`
    * `$ flask run`
10. If you want scrap data by yourself, here is a link for a scraper which is written  by UCSB-rooms goup. It is written in python, which is esaier to follow than our java-version. [Link](https://github.com/ucsb-cs48-w19/6pm-ucsb-rooms/blob/master/scraper.py)  


## Functionality
1. User open the link above.
2. Read the page of introduction, and click the link to get start.
3. Use dropdown boxes to find the class they need.
4. Click add class to add class to the schedule
5. Delete or continue add classes. The calendar may show them the note if the confliction happens.
6. Use "Plus" bottom to add more schedules.

## Known Problems

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D


## License
If you haven't already, add a file called LICENSE.txt with the text of the appropriate license. We recommend using the MIT license: https://choosealicense.com/licenses/mit/

The Value Exchange: users are happy with the result

