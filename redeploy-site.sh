echo "Killing all tmux sessions..."
tmux kill-ses -t flask-portfolio
echo "Fetching newest changes..."
git fetch && git reset origin/main --hard
echo "Python venv stuff"
source python3-virtualenv/bin/activate
pip install -r requirements.txt
echo "tmux..."
tmux new-session -d -s flask-portfolio 'flask run --host=0.0.0.0'
echo "deactivating python shell"
deactivate
echo "Finished!" 
