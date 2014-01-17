##Usage

Welcome to coffeebeans

This SocialSchools CMS Site has been generated using the Social Schools CMS Template: https://bitbucket.org/changer/socialschools-cms-template

Most information how to setup and use can be found there. 

If you read this, you will probably start contributing to an existing solution. follow the following procedure to get up and running:

### Setup environment

```
psql -c "CREATE DATABASE coffeebeans"
mkvirtualenv coffeebeans
git clone ssh://git@bitbucket.org/changer/coffeebeans.git
cd coffeebeans
setvirtualenvproject
add2virtualenv .
echo "export DATABASE_URL=postgres://localhost/coffeebeans" >> $VIRTUAL_ENV/bin/postactivate
echo "export DJANGO_SETTINGS_MODULE=coffeebeans.settings.local" >> $VIRTUAL_ENV/bin/postactivate
echo "unset DATABASE_URL" >> $VIRTUAL_ENV/bin/postdeactivate
echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/postdeactivate
workon coffeebeans
pip install -r requirements.txt
python manage.py validate
python manage.py syncdb --all --noinput 
python manage.py migrate --fake
python manage.py createsuperuser
```

