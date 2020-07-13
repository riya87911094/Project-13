import sqlite3

db = sqlite3.connect('Registration')
rs = db.cursor()

#rs.execute('''create table Register1(name varchar(50),email varchar(100),phone varchar(10),passwd varchar(10))''')
#db.commit()  

rs.execute('''insert into Register1 values('logana','@gmail.com','4567898765','logana1234#')''')
db.commit()


rs.execute('select * from Register1')
for i in rs:
    print(i)