# Gallery

My  personal gallery application that you display all my favourite photos for others to see. 12th-May-2019

### Prerequisites

What things you need to install the software and how to install them

```
sudo apt-get install python3.6.
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
pip install virtualenv
```

Then activate

```
source virtual/bin/activate
```

Install pip

```
sudo apt install python3-pip
```

```
pip install django==1.11
```

```
cd to the dir you cloned the repository
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

```
python3.6 manage.py pictures test
```

### Writing the test

The tests simple make our application crash free just incase it does.
Example:

```
def test_save_method(self):
        self.pius.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

```

### Passing the  tests

To make it pass we:

```
def save_editor(self):
        self.save()
```

## Deployment

In order to deploy the following files must be created assuming you have set heroku:

* Add a `procfile` in the project root.
* Add `requirement.txt` file with all the requirements in the project root;
* Add `Gunicorn` to `requirements.txt`;
* A `runtime.txt` to specify the correct Python version in the project root;
* Configure `whitenoise` to serve static files.


## Built With

* [Django](https://docs.djangoproject.com/en/2.2/) - The web framework used
* [Python3.6](https://docs.python.org/3/) - Dependency Language
* [Postgres](https://www.postgresql.org/docs/10/tutorial-inheritance.html) - Used to store data
* [Heroku](https://devcenter.heroku.com/categories/reference) - To deploy the application


## Authors

* **Oruko Pius** 


## License

This project is licensed under the MIT License - see the [license.md](license.md) file for details

## Acknowledgments

* Used LMS for the sole reference
* StackOverflow
