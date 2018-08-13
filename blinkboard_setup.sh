pip install -r  requirements.txt
sudo apt-get install avahi-utils
sudo cp blinkt.service /etc/avahi/services/blinkt.service
crontab < blinkboard_crontab_file.cron
