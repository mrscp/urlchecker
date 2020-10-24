from thread import Thread
import time
import mysql.connector
import requests
from html2text import html2text
import re
from datetime import datetime


args = dict(
    host="db",
    port="3306",
    user="root",
    password="example",
    database="urlchecker"
)


def check(thread_name, instance):
    while True:
        exists_keywords = False

        try:
            html_content = requests.get(instance["urladdress"])
            is_active = html_content.status_code == 200
        except requests.exceptions.ConnectionError:
            is_active = False
            html_content = None

        if is_active:
            html_content = html2text(html_content.text)

            if instance["UseKeywords"] == 1:
                if instance["Keywords"] is not None:
                    keywords = instance["Keywords"].split(",")
                    pattern = ["({})".format(x) for x in keywords]
                    pattern = r"|".join(pattern)
                    exists = re.search(pattern, html_content)
                    if exists:
                        exists_keywords = True
            else:
                exists_keywords = True

        result = is_active * exists_keywords

        con = mysql.connector.connect(**args)
        cur = con.cursor(dictionary=True)
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

        cur.execute("SELECT * FROM urls WHERE urlid='{0}'".format(instance["urlid"]))
        instance = cur.fetchone()

        cur.execute(
            """
            INSERT INTO urlcheckhistory (urlid, CheckTime, CheckResult)
            VALUES ('{2}', '{0}', b'{1}')
            """.format(dt_string, result, instance["urlid"])
        )
        print(
            "..........................................................",
            thread_name, instance, "\n",
            "Time '{0}', Result '{1}')".format(dt_string, result, instance["urlid"]), "\n",
            "Record id", cur.lastrowid
        )
        cur.execute(
            """
            UPDATE urls 
            SET LastCheckTime = '{0}',  IsActive = b'{1}'
            WHERE urlid = '{2}'""".format(dt_string, result, instance["urlid"])
        )
        con.commit()
        con.close()
        cur.close()

        interval = instance["IntervalMinutes"]
        time.sleep(interval)


main_connection = mysql.connector.connect(**args)
cursor = main_connection.cursor(dictionary=True)
cursor.execute("SELECT * FROM urls")
rows = cursor.fetchall()
main_connection.close()
cursor.close()

for row in rows:
    uid = row["urlid"]
    Thread(uid, "Thread_{}".format(uid), check, instance=row).start()

