cd project-chad-wojak
git fetch && git reset origin/main --hard
pip3 install --upgrade pip
pip3 install -r requirements.txt
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
systemctl start myportfolio
systemctl enable myportfolio
systemctl daemon-reload
systemctl restart myportfolio