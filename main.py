from thread import Thread
import time
import mysql.connector


def check(thread_name, instance):
    while True:
        print(thread_name, instance)
        if instance["UseKeywords"] == 1:
            print("checking keywords...")
        interval = instance["IntervalMinutes"]
        time.sleep(interval)


my_db = mysql.connector.connect(
    host="db",
    port="3306",
    user="root",
    password="example",
    database="urlchecker"
)

cursor = my_db.cursor(dictionary=True)
cursor.execute("SELECT * FROM urls;")
rows = cursor.fetchall()

for row in rows:
    uid = row["urlid"]
    Thread(uid, "Thread_{}".format(uid), check, instance=row).start()
