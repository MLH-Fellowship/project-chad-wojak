cd project-chad-wojak
git fetch && git reset origin/main --hard
pip3 install --upgrade pip
pip3 install -r requirements.txt
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
tmux new-session -d -s detached
tmux send-keys 'flask run --host=0.0.0.0' C-m