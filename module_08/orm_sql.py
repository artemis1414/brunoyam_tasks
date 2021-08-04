import sqlite3


def connect(db):
    con = sqlite3.connect(db)
    return con


def foreign_keys_on(con):
    con.execute("PRAGMA foreign_keys = 1")


def cursor(con):
    return con.cursor()


def create_table(name_table, columns, con):
    columns_types = []

    for element in columns:
        if not columns_types:
            columns_types.append(f'{element} INTEGER PRIMARY KEY')
            continue
        if type(element) == int:
            columns_types.append(f'{element} int')
        elif type(element) == str:
            columns_types.append(f'{element} text')
    con.execute(f"CRATE TABLE IF NOT EXISTS {name_table} {tuple(columns_types)}")
    return


