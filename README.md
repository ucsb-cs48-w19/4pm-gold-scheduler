# Project Gold Scheduler
[GS](https://protected-depths-20813.herokuapp.com)
## Project summary
Gold Scheduler helps UCSB students plan their upcomming quarter by making easier for them to visualize multiple potential schedules. It uses a calandar-like view with multiple windows, each window is a schedule. The user can select the classes available for the quarter selected and filter out classes just like in GOLD. From there they can drag the class into the calandar, have its lecture and section times displayed, any potential conflicts are highlighted and can be easily resolved.  

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
Select the classes from the class box, add them to the weekly calendar with the click of a button and have all class info and potential conflicts displayed on the page.


## Known Problems
1. Leaving page does not save calendar
2. Adding the same class again will result in a conflict
3. Cannot remove classes from calendar once added
4. Text for classes close on calendar might have text overlapping each other
5. Class info text is not relative to screen size. Changing browser window size will put text outside block

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D
