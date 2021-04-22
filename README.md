# SQLAlchemy

Learning notes about SQLAlchemy

## SQLAlchemy core



### Create engine with the connection string

```python
from sqlalchemy import create_engine

# create an engine for sqllte
engine = create_engine('sqlite:///college.db', echo = True)

```
for other db, this is how the connect string would be like
dialect[+driver]://user:password@host/dbname
```
for example for mysql it would look like this:
mysql+pymysql://<username>:<password>@<host>/<dbname>
```   
Engine object has connect method (for more methods: [here](https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_connecting_to_database.htm)

### Create Table
You can use the MetaData object which holds the information of tables to create tables. Refer to example.
In sqlalchemy, you can use some methods to mimic what a query would do. 


### Execute expression
Example
```python
ins = ins.values(id=1, name="Bob", lastname="Smith")
# create connection
conn = engine.connect()
# we can use the expression or string query to execute
conn.execute(ins)

result = conn.execute("select * from students")
result.fetchall()
```

### Textual SQL
Use `text` method to format query
```python
from sqlalchemy import text

s = text("select students.name, students.lastname from students where students.name between :x and :y")
conn.execute(s, x = 'A', y = 'L').fetchall()

```

You can also do something like this:
```python
from sqlalchemy.sql import select
s = select([text("students.name, students.lastname from students")]).where(text("students.name between :x and :y"))
conn.execute(s, x = 'A', y = 'L').fetchall()

```
