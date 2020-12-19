from modeBTree import *

insertar = createDatabase('db1')
print(insertar)
insertar1 = createDatabase('db1')
print(insertar1)
insertar2 = createDatabase('db4')
print(insertar2)
insert = createDatabase('db5')
print(insert)
ingresar = createDatabase(0)
print(ingresar)
alter = alterDatabase('db5', 'db1')
print(alter)
alter1 = alterDatabase('db5', 'db2')
print(alter1)
drop = dropDatabase('db4')
print(drop)
imp = showDatabases()
print(imp)


