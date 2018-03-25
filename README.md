**Активация venv**

source venv/bin/activate

**Обновление requirements.txt**

pip freeze > requirements.txt


**For staging run the following command:**

$ heroku config:_set APP_SETTINGS=config.StagingConfig_ --remote stage
For production:

$ heroku config:_set APP_SETTINGS=config.ProductionConfig_ --remote pro