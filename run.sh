#!/bin/bash
export MANDRILL_KEY=$3
export PERSONAL_SITE_DB_KEY=$2
exec /home/ubuntu/.virtualenvs/personal_site/bin/gunicorn --pythonpath '/home/ubuntu/personal_site' personal_site.wsgi
