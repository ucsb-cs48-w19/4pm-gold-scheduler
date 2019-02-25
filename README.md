[![Build Status](https://travis-ci.org/ucsb-cs48-w19/4pm-gold-scheduler.svg?branch=K1n9sley-heroku)](https://travis-ci.org/ucsb-cs48-w19/4pm-gold-scheduler)
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

## Functionality
1. User open the link above.
2. Read the page of introduction, and click the link to get start.
3. Use dropdown boxes to find the class they need.
4. Click add class to add class to the schedule
5. Delete or continue add classes. The calendar may show them the note if the confliction happens.
6. Use "Plus" bottom to add more schedules.

## Known Problems
1. Add delete process
2. Add more than one schedule
3. Time conflict formate updating
4. schedule match time

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D


## License
If you haven't already, add a file called LICENSE.txt with the text of the appropriate license. We recommend using the MIT license: https://choosealicense.com/licenses/mit/

The Value Exchange: users are happy with the result

