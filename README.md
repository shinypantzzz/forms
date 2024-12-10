# Startup
First, set up a virtual environment:
```
root> python -m venv env
```
Activate it. In powershell, for example, run:
```
root> ./env/Scripts/Activate
```
Install dependencies:
```
(env) root> pip install -r requirements.txt
```
Run server:
```
(env) root> python src/main.py
```
# Tests
Tests are in a form of json file `tests/tests.json`. Each test consists of data to be sent and expected response.

Test database `db.json` consists of three templates:
- LoginForm
- RegistrationForm
- OrderForm

To run tests, run:
```
(env) root> python tests/main.py
```
# Additional information
When there are more then one suitable template, template with largest number of fields is returned. If there are more then one such template (which means those templates have the exact same fields), any of them can be returned.
