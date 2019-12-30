#Importing the required libraries
import mysql
import mysql.connector
from mysql.connector import Error
import faker
from faker import Faker
from faker import Factory


# Object creations
fk = Faker()
#fpassword = Factory.create()





#Here we are creating the autodata entry









#Database connection
# Change your database settings herer :-
#  - host       : will you localhost or 127.0.0.0:port
#  - port       : for mysql deafult port will be 3306, but incase
#  - user       : database user, default is root
#  - password   : You database password
#  - auth_pluing: This is only python 3.x versions

no_enterData      = 2000
database_host     = 'localhost'
database_port     =  3308
database_name     = 'youdatabasename'
database_user     = 'root'
database_password = 'yourdatabasepassword'
python3authplugin = 'mysql_native_password'  # This is for mysql and python 3.x version only, if other database you do have and there is python2 then just comment it.

# this is will create connection establishment with database
conn = mysql.connector.connect(
    host        = database_host,
    port        = database_port,
    database    = database_name,
    user        = database_user,
    password    = database_password,
    auth_plugin = 'mysql_native_password' ## comment it if you are using python2 and database other than mysql.
    )

# creating connection object
crsr = conn.cursor()

# Query

#query = "SELECT * FROM users"
insertQuery = "INSERT INTO employee(name, age, sex, designation, address) VAlUES(%s, %s, %s, %s, %s)"
#Executing  query

#Initiating the data entry here
# The no will iterate that amount of data

for i in range(no_enterData):
    val = (
            fk.profile()['name'],
            str(fk.profile()['birthdate']),
            fk.profile()['sex'],
            fk.profile()['job'],
            fk.profile()['address']
        )
    crsr.execute(insertQuery, val)
    print("{0} {1} {2} {3} {4}".format(
        val[0],
        val[1],
        val[2],
        val[3],
        val[4]
    ))
# Fetching the result
# result  = crsr.fetchall()

## Ultra saving the data
conn.commit()
