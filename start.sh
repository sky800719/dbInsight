#python manage.py crontab remove
ps -ef | grep "manage.py" | grep -v grep | awk '{print $2}' | xargs kill -9

> nohup.out 

nohup python manage.py runserver sqlaudit:8000 &
#python manage.py crontab add

tail -f nohup.out
