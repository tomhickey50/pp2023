import os

class Config:
	SECRET_KEY = '5b07e16c302697a4' #set to env var
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' #set to env var
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')