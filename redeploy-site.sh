#!/usr/bin/bash
tmux kill-session
cd project-chad-wojak/
git fetch && git reset origin/main --hard
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt
tmux new-session -d -s flask
tmux send-keys -t flask 'source python3-virtualenv/bin/activate' C-m
tmux send-keys -t flask 'export FLASK_ENV=development' C-m
tmux send-keys -t flask 'flask run --host=0.0.0.0' C-m
~                                                                    
