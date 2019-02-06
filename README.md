# Project Gold Scheduler

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
5. gunicorn

## Installation
1. Install [pip](https://pip.pypa.io/en/latest/installing/)
2. Install virtual environment:  `$ pip install virtualenv`
3. Under your project file: `$ virtualenv venv`
4. Active virtualenv: `$ source venv/bin/activate`
5. Install Flask: `$ pip install Flask`
6. Install gunicorn: `$ pip install gunicorn`

## Functionality
Select the classes from the class box, drag and drop into generate box, click the generae button. All possible weekly schedules will be displayed on the calandar


## Known Problems
1. Time Conflict notes show wrong. 
2. Class shows on the wrong place of the schedule. 
3. Try to delete some classes, and see if the notes show right. 
4. Refresh the page.

## Contributing

TODO: Leave the steps below if you want others to contribute to your project.

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License

If you haven't already, add a file called `LICENSE.txt` with the text of the appropriate license.
We recommend using the MIT license: <https://choosealicense.com/licenses/mit/>

