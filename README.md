# Track my work
[![CircleCI](https://circleci.com/gh/LucasMagnum/trackmywork/tree/master.svg?style=svg)](https://circleci.com/gh/LucasMagnum/trackmywork/tree/master)

Trackmywork is an tool to help us to keep track of our tasks in a simple way using the command line.

One of the good habits of productivity is to keep track of every task we do and this tool will help us to do it :)

When I was creating the readme for my `personal` project called `trackmywork`, I planned to spend 2 hours on it. This is how I kept track of my task:

    $ trackmywork start -m "Creating track my work readme" -p "trackmywork" -c "personal" -t 2h
    The task 1 - "Creating track my work readme" was started with success.

When I was done, I finished my task :)

    $ trackmywork finish 1
    The task 1 was finished with success.

or

    $ trackmywork finish
    The last task 1 was finished with success.


At the end of the day, I could see how many tasks I accomplished and the tasks I was still waiting
to finish.

    $ trackmywork show
    id; message; category; project; hours; links; started_at; finished_at
    1; "Creating track my work readme", "personal", "trackmywork", "2h", "", "2018-01-01 19:10:01", "2018-01-01 19:15:00"
    2; "Updating the track my work docs", "personal", "trackmywork", "1h", "", "2018-01-01 20:00:01", "2018-01-01 20:30:00"
    3; "Creating new examples of tasks", "personal", "trackmywork", "1h", "", "2018-01-01 21:00:01", ""

    $ trackmywork show --wip
    id; message; category; project; hours; links; started_at; finished_at
    3; "Creating new examples of tasks", "personal", "trackmywork", "1h", "", "2018-01-01 21:00:01", ""


## Quick start


### First install it

  $ pip install trackmywork


### Start a task
When we start a new task, we could use the `start` command, this task will be started and the application will keep track of the time it took to finish it.

    $ trackmywork start -m "Starting my task" -p "trackmywork" -c "personal" -t 2h
    The task 1 - "Starting my task" was started with success.

    # Adding links to a task
    $ trackmywork start -m "Task with links" -l "http://google.com" -t 2h
    The task 2 - "Task with links" was started with success.

### Edit a task
We could `edit` the task message, links or time after we create the task:

    $ trackmywork edit 2 -m "Changing the task message" -t 3h -l ""
    The task 2 was edited with success. Fields changed: [message, time, links]


### Finish a task
We should save when we `finish` the task, that way is possible to keep track of the time it took between the `start` and `finish`.

    $ trackmywork start -m "Task to finish" -p "trackmywork" -c "personal" -t 2h
    The task 3 - "Task to finish" was started with success.

    $ trackmywork finish
    The last task 3 was finished with success.

    $ trackmywork finish 2
    The task 2 was finished with success.

    $ trackmywork finish 2
    The task 2 is already finished.


### Register a task
We may forget to start a task, but want to `register` it anyway.

    $ trackmywork register -m "Just saving this task" -t 2h -p "test" -c "personal"
    The task 4- "Just saving this task" was registered with success.

### Remove a task
We might want to `remove` a task.

    $ trackmywork remove 3
    Do you want to remove the 3 task? [yn]

    The task 3 was removed with success.

### Options

    The required parameters are:

        -t (time)
        -m (activity message)

    Optional parameters are:
        -p (project)
        -c (category)
        -l (links)


#### Show tasks

    $ trackmywork show 1
    id; message; category; project; hours; links; started_at; finished_at
    1; "Start my task", "personal", "trackmywork", "2h", "", "2018-01-01 19:10:01", "2018-01-01 19:15:00"

    $ trackmywork show --tail
    id; message; category; project; hours; links; started_at; finished_at
    2; "Changing the task message", "personal", "trackmywork", "3h", "", "2018-01-01 19:20:00", "2018-01-01 19:35:00"
    1; "Start my task", "personal", "trackmywork", "2h", "", "2018-01-01 19:10:01", "2018-01-01 19:15:00"

    $ trackmywork show --tail --limit 1
    id; message; category; project; hours; links; started_at; finished_at
    2; "Changing the task message", "personal", "trackmywork", "3h", "", "2018-01-01 19:20:00", "2018-01-01 19:35:00"


#### Clear tasks
We could clear all the tasks we have stored.

    $ trackmywork clear
    Are you sure about this? [yn]
    All tasked were deleted successfully.


## Configurations

All configurations are stored in environment variables, we could change the behavior of the tracker using these configurations.

On my work computer, I have some default parameters to make it easier to track my tasks:

    export TRACKMYWORK_DEFAULT_CATEGORY="work"
    export TRACKMYWORK_DEFAULT_PROJECT="myproject"

    export TRACKMYWORK_DEFAULT_STORAGE="textfile"

So, we could set up a default category, project or storage path.
When no `category` is given, it will use the `TRACKMYWORK_DEFAULT_CATEGORY` if it exists, the same for `project`.

# Storage backends

## Textfile
By default, the textfile storage is used and it will be saved on "/home/user/trackmywork.txt".

### Configurations

    TRACKMYWORK_DEFAULT_STORAGE="textfile"
    TRACKMYWORK_STORAGE_PATH="/home/username/mywork.txt"


### Interface

Our data is stored in columns, following this template:

    id; message; time; category; project; links; started_at; finished_at


