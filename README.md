## Development

* clone repo
* create venv
```
mkvirtualenv personal_site
```
* install dependencies

```
pip install -r requirements.txt
```

```
brew install mysql
```

* Create DB and user permissions
```sql
CREATE DATABASE 'personal_site';
CREATE USER 'user_name'@'localhost' IDENTIFIED BY 'db_password';
GRANT ALL ON personal_site.* TO 'user_name'@'localhost';
```
* Runserver
