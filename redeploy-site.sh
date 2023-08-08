#!/usr/bin/bash
echo "Killing server"

systemctl stop myportfolio.service

echo "Server Killed."
echo "---------------------------------------------"

sleep 5

# echo "navigating to project directory"

# cd gitgators-lauren-wasay/

# echo "Done navigating to project directory."
# echo "---------------------------------------------"

echo "running git fetch"

git fetch && git reset origin/main --hard

echo "Ran git fetch."
echo "---------------------------------------------"

echo "Activating virtual env"

source myenv/bin/activate

echo "Activated virtual env"
echo "---------------------------------------------"

echo "Installing dependencies."

pip install click==8.0.1
pip install cryptography==37.0.2
pip install Flask==2.0.1
pip install itsdangerous==2.0.1
pip install Jinja2==3.0.1
pip install MarkupSafe==2.0.1
pip install peewee==3.14.10
pip install pycparser==2.21
pip install PyMySQL==1.0.2
pip install python-dotenv==0.17.1
pip install Werkzeug==2.0.1

echo "Dependencies Installed."
echo "---------------------------------------------"

echo "Restarting myportfolio service"
systemctl start myportfolio.service
systemctl enable myportfolio.service
echo "myportfolio service restarted."
echo "---------------------------------------------"
