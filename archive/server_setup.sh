#!/usr/bin/env bash

set -e

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/perspectivefood/recommender_api.git'

PROJECT_BASE_PATH='/usr/local/apps'
VIRTUALENV_BASE_PATH='/usr/local/virtualenvs'

# Set Ubuntu Language
locale-gen en_GB.UTF-8

# Install Python, SQLite and pip
echo "Installing dependencies..."
apt-get update
apt-get install -y python3-dev python3-venv sqlite python-pip supervisor nginx git

mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH/recommender-api

mkdir -p $VIRTUALENV_BASE_PATH
python3 -m venv $VIRTUALENV_BASE_PATH/recommender_api

$VIRTUALENV_BASE_PATH/recommender_api/bin/pip install -r $PROJECT_BASE_PATH/recommender-api/requirements.txt

# Run migrations
cd $PROJECT_BASE_PATH/recommender-api/src

# Setup Supervisor to run our uwsgi process.
cp $PROJECT_BASE_PATH/recommender-api/deploy/supervisor_profiles_api.conf /etc/supervisor/conf.d/recommender_api.conf
supervisorctl reread
supervisorctl update
supervisorctl restart recommender_api

# Setup nginx to make our application accessible.
cp $PROJECT_BASE_PATH/recommender-api/deploy/nginx_recommender_api.conf /etc/nginx/sites-available/recommender_api.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/recommender_api.conf /etc/nginx/sites-enabled/recommender_api.conf
systemctl restart nginx.service

echo "DONE! :)"
