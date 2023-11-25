import os
import sys
import sqlite3 as sdb


def start_connction():
    if not os.path.isfile(os.getcwd() + "/contact.db"):
        con = sdb.connect("contact.db")
        cur = con.cursor()
        cur.execute(""" CREATE TABLE contact(c_id integer primary key autoincrement,
                        c_name Text,c_family Text,c_phone Text,c_email Text,c_telegramId Text
                        )   """)
        con.commit()
        con.close()


def get_id():
    con = sdb.connect("contact.db")
    cur = con.cursor()
    data_set = ''
    try:
        data_set = cur.execute(f"""SELECT MAX(c_id) FROM contact """)
        datas = data_set.fetchone()
        return datas[0]
    except:
        return

    finally:
        con.commit()
        con.close()


def insert_new_contact(c_name, c_family, c_phone, c_email, c_telegramId):
    con = sdb.connect("contact.db")
    cur = con.cursor()
    data_set = cur.execute(f""" INSERT INTO contact(c_name,c_family,c_phone,c_email,c_telegramId)
                                                VALUES( '{c_name}',
                                                        '{c_family}',
                                                        '{c_phone}',
                                                        '{c_email}',
                                                        '{c_telegramId}'    ) """)
    con.commit()
    con.close()


def select_all_database(family, phone):
    con = sdb.connect("contact.db")
    cur = con.cursor()
    data_set = ''
    try:
        if len(family) != 0:
            data_set = cur.execute(f""" SELECT * FROM contact WHERE c_family LIKE '%{family}%' """)
        elif len(phone) != 0:
            data_set = cur.execute(f""" SELECT * FROM contact WHERE c_phone LIKE '%{phone}%'  """)
        datas = data_set.fetchall()
        con.commit()
        con.close()
        return datas
    except:
        return


def select_person_bye_id(contact_id):
    con = sdb.connect("contact.db")
    cur = con.cursor()
    data_set = ''
    try:
        data_set = cur.execute(f"""SELECT * FROM contact WHERE c_id={contact_id}""")
        datas = data_set.fetchone()
        return datas
    except:
        return

    finally:
        con.commit()
        con.close()


def update_contact(c_id, c_name, c_family, c_phone, c_email, c_telegramId):
    con = sdb.connect("contact.db")
    cur = con.cursor()
    data_set = cur.execute(
        f""" UPDATE  contact SET c_name= '{c_name}' , c_family='{c_family}',  c_phone='{c_phone}',  c_email='{c_email}', c_telegramId='{c_telegramId}'  WHERE c_id = {c_id}   """)
    con.commit()
    con.close()


def delete_contact(c_id):
    con = sdb.connect("contact.db")
    cur = con.cursor()
    data_set = cur.execute(
        f""" DELETE FROM  contact WHERE  c_id = {c_id}   """)
    con.commit()
    con.close()

if __name__ == "__main__":
    pass
