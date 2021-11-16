# Try it

```bash
git clone https://github.com/lahodny/log-app.git
cd log-app
docker-compose build
docker-compose run web python manage.py migrate
docker-compose run web python manage.py loaddata mydata.json
docker-compose up
```
Then open http://127.0.0.1:8000