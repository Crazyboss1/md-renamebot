echo "Cloning Repository"
git clone https://github.com/CrazyBoss1/md-renamebot /app
cd /app
echo "installing requirements"
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
