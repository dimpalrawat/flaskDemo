import os


user = os.environ.get('MYSQL_USER')
password = os.environ.get('MYSQL_PASSWORD')
db = os.environ.get('MYSQL_DATABASE')
host = os.environ.get('db_endpoint_HOST')

print(user)
print(password)
print(db)
print(host)


CONNECTION_STRING = "mysql+pymysql://"+user+":"+password+"@"+host+"/"+db