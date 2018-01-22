echo "Kill Exists Python Process!!!"
ps -ef | grep "manage.py" | grep -v grep | awk '{print $2}' | xargs kill -9

echo "Start Python Server at Port 8000"
nohup python manage.py runserver sqlaudit:8000 &
python manage.py crontab add
