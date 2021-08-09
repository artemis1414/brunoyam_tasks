import sqlite3

class Base:

    def __init__(self, name_db):
        self.db = name_db
        self.con = sqlite3.connect(self.db)
        self.cur = self.con.cursor()

    def commited(func):
        def decorator(*args, **kwargs):
            func(*args, **kwargs)
            args[0].con.commit()

        return decorator
    @commited
    def create(self, name_table, **kwargs):
        list_columns = []
        if 'FOREIGN' in kwargs:
            self.cur.execute("PRAGMA foreign_keys = 1")
            for value in kwargs['FOREIGN']:
                kwargs[value] = ''
            del kwargs['FOREIGN']
        for key, value in kwargs.items():
            list_columns.append(' '.join([key, value]))
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {name_table} ({', '.join(list_columns)})")

    def select(self, table, fields, where=None):
        if not where:
            request = self.cur.execute(f"SELECT {', '.join(fields)} FROM {', '.join(table)}")
        else:
            request = self.cur.execute(f"SELECT {', '.join(fields)} FROM {', '.join(table)} WHERE {where}")
        return request.fetchall()

    @commited
    def insert(self, table, *args):
        self.cur.executemany(f"INSERT INTO {table} VALUES ({' ,'.join(['?' for _ in range(len(args[0]))])})", list(args))

    def close(self):
        self.con.close()



