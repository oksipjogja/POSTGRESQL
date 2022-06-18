import psycopg2 # PostgreSQL database adapter for Python programming Language
DB_HOST = "localhost"
DB_Name = "wahana"
DB_user = "wahana"
DB_pass = "umbara_77"

# menghubungkan postgreSQL dengan fungsi psycopg2 sebagai modul yang digunakan
connection = psycopg2.connect(dbname=DB_Name,user=DB_user,password=DB_pass,host=DB_HOST)
cursor = connection.cursor()  # object cursor yang biasa digunakan untuk mengeksekusi SELECT statement

# # # membuat tabel baru
# print("Query : -\nCreate Table department(dept_id BIGSERIAL NOT NULL PRIMARY KEY,dept_name VARCHAR(100) NOT NULL,vacancy BIGSERIAL NOT NULL);")
# cursor.execute("CREATE TABLE department(dept_id BIGSERIAL NOT NULL PRIMARY KEY,dept_name VARCHAR(100) NOT NULL,vacancy BIGSERIAL NOT NULL);")
# print("Tabel Berhasil Dibuat!!")

# # menambahkan data baru kedalam tabel
# print("\nInserting New Values in Table .. Query \nINSERT INTO employee(emp_name,emp_phone) VALUES('andi','081902212402')")
# cursor.execute("INSERT INTO employee(emp_name,emp_phone) VALUES('andi','081902212402')")
# print("Sukses Data Ditambahkan!!")

# # Mencari spesifik value dari database
# print("Displaying Specific Values from Table .....Query\nSELECT * FROM employee where emp_name='Donie';\nOUTPUT\n")
# cursor.execute("SELECT * FROM employee where emp_name='Donie';")
# output = cursor.fetchall()
# for item in output:
#     print(item)
# print("\n")

# # Melakukan Update tabel secara spesifik
# print("Updating Specific values in table ... Query ..\nUPDATE employee SET emp_name=")
# cursor.execute("UPDATE employee SET emp_name='Donie' WHERE emp_id='1';")
# print("\nUpdate Berhasil\nPrinting entire table with changes !!\n")
# cursor.execute("SELECT * FROM employee;")
# output = cursor.fetchall()
# for item in output:
#     print(item)
# print("\n")

# # Menghapus data dari tabel
# print("Deleting specific record from table .. Query ... \nDELETE FROM employee WHERE")
# cursor.execute("DELETE FROM employee WHERE emp_id=1;")
# print("Menghapus Data Berhasil!\n Printing table with changes !!\n")
# cursor.execute("SELECT * FROM employee;")
# output = cursor.fetchall()
# for item in output:
#     print(item)
# print("\n")

# # Menghapus semua data dari tabel
# cursor.execute("TRUNCATE TABLE employee;")
# print("Semua data dari Tabel telah terhapus !!")

# # Menghapus tabel dari database
# cursor.execute("DROP TABLE employee;")
# print("Tabel Berhasil Dihapus !!")

# # cursor.execute("SELECT * FROM wahana;")
# # output=cursor.fetchall()
# # for item in output:
#     # print(item)
connection.commit()
cursor.close()
connection.close()