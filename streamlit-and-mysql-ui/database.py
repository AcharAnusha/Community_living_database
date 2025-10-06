import mysql.connector
from datetime import date
from dotenv import load_dotenv
import os
load_dotenv()
mygate = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="community_living"
)

c = mygate.cursor()


def view_all_tickets():
    c.execute('SELECT * from ticket')
    data = c.fetchall()
    return data


def get_flat_block(rid):
    c.execute('SELECT flat, block from resident WHERE rid="{}"'.format(rid))
    data = c.fetchall()
    if data:
        return data[0]
    else:
        return False


def db_create_ticket(rid, complaint):
    c.execute("SELECT tid FROM ticket ORDER BY tid DESC LIMIT 1")
    result = c.fetchone()

    last_tid = result[0]  # e.g., 'T100'
    last_number = int(last_tid[1:])  # Remove 'T' and convert to int
    new_tid = f"T{last_number + 1}"

    if not get_flat_block(rid):
        return False

    flat, block = get_flat_block(rid)
    query = 'INSERT INTO ticket(tid, rid, flat, block, is_resolved, complaint, response, date_generated) VALUES ("{}","{}","{}","{}","{}","{}","{}","{}")'.format(
        new_tid, rid, flat, block, 0, complaint, None, date.today())
    c.execute(query)
    mygate.commit()
    return new_tid


def db_get_ticket(tid):
    c.execute('SELECT * from ticket WHERE tid="{}"'.format(tid))
    data = c.fetchall()
    return data


def db_update_ticket(tid, new_ticket_status, new_ticket_response):

    # print(new_ticket_response, new_ticket_status, tid)

    try:
        query = 'UPDATE ticket set is_resolved="{}", response="{}" WHERE tid="{}";'.format(
            new_ticket_status, new_ticket_response, tid)
        # print(query)
        c.execute(query)
        mygate.commit()
        return True
    except:
        return False


def db_delete_ticket(tid):
    try:
        c.execute('DELETE FROM ticket WHERE tid="{}"'.format(tid))
        mygate.commit()
        return True
    except:
        return False


def db_any_query(q):
    c.execute(q)
    data = c.fetchall()
    mygate.commit()
    return data
