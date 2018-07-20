#!/usr/bin/python

import sqlite3
from sqlite3 import Error

def sqlite_connect(sqlite_file):
    try:
        return  sqlite3.connect(sqlite_file)
    except Error as e:
        print(e)

    return None


def print_all_table_schemas(connection):
    print("Tables:")
    cursor = connection.cursor()
    results = cursor.execute("SELECT sql FROM sqlite_master WHERE type = 'table';")
    for name in results:
        print(name[0]) 
    print("")

def list_tables(connection):
    print("* All tables:")
    cursor = connection.cursor()
    results = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    for name in results:
        if name[0] != "sqlite_sequence":
            print("\t{}".format(name[0])) 
    
    print("\n")

def get_columns_name(cursor_description):
    return [x[0] for x in cursor_description]

def format_columns(columns):
    formated_columns = []
    for c in columns:
        formated_columns.append("{:20}".format(c))
    return " | ".join(formated_columns)

def print_columns_header_line(cursor):
    columns = get_columns_name(cursor.description)
    print(format_columns(columns))
    underline = ""
    for _ in range(0, len(columns) - 1):
        underline += "---------------------|-"
    underline += "---------------------"
    print(underline)


def print_table_records(connection, table_name):
    cursor = connection.cursor()
    sql = "SELECT * FROM {}".format(table_name)
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("* All records of \"{}\":\n".format(table_name))
        print_columns_header_line(cursor)
        for r in rows:
            print("%-20s | %20s" %(r[0], r[1]))
    except Error as e:
        print("* Print records of table \"{0}\", ERROR: \"{1}\"".format(table_name, e))
    print("\n")

def main():
    sqlite_file = "chats.db"
    connection = sqlite_connect(sqlite_file)
    list_tables(connection)
    print_table_records(connection, "abc")
    print_table_records(connection, "messages")
    print_table_records(connection, "conversations")
    print_table_records(connection, "conversations")
    print_table_records(connection, "pns_tokens")
    

if __name__ == '__main__':
    main()