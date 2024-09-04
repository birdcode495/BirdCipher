import psycopg2

conexion1 = psycopg2.connect(host = 'b5882sxpx70asjk9ktop-postgresql.services.clever-cloud.com', port = 50013, 
	user = 'uuwo4nvlyzn61jj5sqtu', dbname = 'b5882sxpx70asjk9ktop', password = 'oi7xGqSj3Gcd9tcfzYegl86GwXz1yC')

cursor1 = conexion1.cursor()

u = 'Carlos'

psql1 = 'select * from players where username = (%s)'
hj = (u,)

cursor1.execute(psql1, hj)
er = cursor1.fetchall()

print(er)

conexion1.commit()
conexion1.close()

