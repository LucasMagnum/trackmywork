# Track my work
Trackmywork is an application to help us keep track of our tasks in a simple way using the command line.

One of the good habits of productivity is to keep track of every task we do and this application will help us to do it :)

When I was creating the readme for my `personal` project called `trackmywork`, I planned to spend 2 hours on it. This is how I kept track of my task:

    $ trackmywork start -m "Creating track my work readme" -p "trackmywork" -c "personal" -t 2h
    You successfully started the task #01 - "Creating track my work readme"

When I am done, I will update my task :)

    $ trackmywork finish 1
    You successfully finished the task 1

or

    $ trackmywork finish
    You successfully finished the last task 1


## Quick start


### First install it

  $ pip install trackmywork


### Start a task
When we start a new task, we could use the `start` command, this task will be started and the application will keep track of the time it took to finish it.

    $ trackmywork start -m "Starting my task" -p "trackmywork" -c "personal" -t 2h
    You successfully started the task 1 - "Starting my task"

    # Adding links to a task
    $ trackmywork start -m "Task with links" -l "http://google.com" -t 2h
    You successfully started the task 2

### Edit a task
We could `edit` the task message, links or time after we create the task:

    $ trackmywork edit 2 -m "Changing the task message" -t 3h -l ""
    You edited the 2 changed message, time and links.


### Finish a task
We should save when we `finish` the task, that way is possible to keep track of the time it took between the `start` and `finish`.

    $ trackmywork finish
    You successfully finished the last task 2

    $ trackmywork finish 2
    You successfully finished the task 2


### Register a task
We may forget to start a task, but want to `register` it anyway.

    $ trackmywork register -m "Just saving this task" -t 2h -p "test" -c "personal"
    You successfully registered the task 3

### Remove a task
We might want to `remove` a task.

    $ trackmywork remove 3
    Do you want to remove the 3 task? [yn]

    You successfully removed the task 3

### Options

    The required parameters are:

        -t (time)
        -m (activity message)

    Optional parameters are:
        -p (project)
        -c (category)
        -l (links)


## Configurations

All configurations are stored in environment variables, we could change the behavior of the tracker using these configurations.

On my work computer, I have some default parameters to make it easier to track my tasks:

    export TRACKMYWORK_DEFAULT_CATEGORY="work"
    export TRACKMYWORK_DEFAULT_PROJECT="myproject"

    export TRACKMYWORK_DEFAULT_STORAGE="textfile"
    export TRACKMYWORK_STORAGE_PATH="/home/lucasmagnum/mywork.txt"

So, we could set up a default category, project or storage path.
By default, the textfile storage is used and it will be saved on "~/trackmywork.txt".
When no `category` is given, it will use the `TRACKMYWORK_DEFAULT_CATEGORY` if it exists, the same for `project`.

# Storage backends

Our storage backends should implement the `show` and `clear` interface.


#### Show tasks
We might want to see the task detail or the last tasks:

    $ trackmywork show #01
      <storage backend response>


    $ trackmywork show --tail 10
      <storage backend response>


#### Clear tasks
We could clear all the tasks we have stored.

    $ trackmywork clear tasks
    Are you sure about this? [yn]



## Textfile

### Configurations

    TRACKMYWORK_DEFAULT_STORAGE="textfile"
    TRACKMYWORK_STORAGE_PATH="/home/lucasmagnum/mywork.txt"


### Interface

Our data is stored in columns, following this template:

    id; task message; category; project; hours; links; started_at; finished_at


#### Show tasks

    $ trackmywork show 1
    id; task message; category; project; hours; links; started_at; finished_at
    1; "Start my task", "personal", "trackmywork", "2h", "", "2018-01-01 19:10:01", "2018-01-01 19:15:00"

    $ trackmywork show --tail
    id; task message; category; project; hours; links; started_at; finished_at
    2; "Changing the task message", "personal", "trackmywork", "3h", "", "2018-01-01 19:20:00", "2018-01-01 19:35:00"
    1; "Start my task", "personal", "trackmywork", "2h", "", "2018-01-01 19:10:01", "2018-01-01 19:15:00"

    $ trackmywork show --tail --limit 1
    id; task message; category; project; hours; links; started_at; finished_at
    2; "Changing the task message", "personal", "trackmywork", "3h", "", "2018-01-01 19:20:00", "2018-01-01 19:35:00"
