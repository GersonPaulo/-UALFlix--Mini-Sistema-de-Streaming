import psycopg2
import psycopg2.extras


from tools import EditorTxt
host = "localhost"
database = "usuarios"
username = "postgres"
pwd = "101213K"
port_id = "5432"

edtxt = EditorTxt()
class DatabaseManager:
    def __init__(self):
        # to avoid errors if db not start
        self.conn = None
        self.cur = None

    def test_db_connection(self):
        try:
            self.conn = psycopg2.connect(host=host, dbname=database, user=username, password=pwd, port=port_id)
            self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            # Query to get all table names in the public schema
            self.cur.execute(""" SELECT table_name FROM information_schema.tables
                                 WHERE table_schema = 'public' AND table_type = 'BASE TABLE';""")
            tables = self.cur.fetchall()
            local = edtxt.charging_bar()
            a = edtxt.negrito_bright_green(f"{' ' * 30}Connected to the database! ✅  ")
            for table in tables:
                local = edtxt.negrito_bright_magenta(f"{' ' * 30}Table --------------- {table[0]}")
        except Exception as error:
            edtxt.negrito_bright_red("❌ Failed to connect:")
            print(error)
        finally:
            if self.cur is not None:
                self.cur.close()
            if self.conn is not None:
                self.conn.close()

    def inicializar_database(self):
        try:
            self.conn = psycopg2.connect(host=host, dbname =database, user=username, password=pwd, port=port_id )
            self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            create_script = ''' CREATE TABLE IF NOT EXISTS users (
                                    user_id   INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                                    email     VARCHAR(255) NOT NULL,
                                    password  VARCHAR(255) NOT NULL) '''
            self.cur.execute(create_script)
            self.conn.commit()
            print("✅ Connected to the database!")
        except Exception as error:
            print("❌ Failed to connect:", error)
        finally:
            if self.cur is not None:
                self.cur.close()
            if self.conn is not None:
                self.conn.close()

    def insert_into_table(self, a=str, b=str):
        try:
            self.conn = psycopg2.connect(host=host, dbname=database, user=username, password=pwd, port=port_id)
            self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            insert_script = ''' INSERT INTO users (email, password) VALUES (%s, %s)'''
            insert_values = (a, b)

            edtxt.negrito_green('valores inseridos na base de dados')
            self.cur.execute(insert_script, insert_values)
            self.conn.commit()
        except Exception as error:
            print(error)
        finally:
            if self.cur is not None:
               self.cur.close()
            if self.conn is not None:
                self.conn.close()

    def show_all_data(self):
        try:
            self.conn = psycopg2.connect(host=host, dbname=database, user=username, password=pwd, port=port_id)
            self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            self.cur.execute('SELECT * FROM USERS')

            user_fetch_data = self.cur.fetchall()
            if len(user_fetch_data) > 0:
                return user_fetch_data
            elif len(user_fetch_data) <= 0:
                return False

            self.conn.commit()
        except Exception as error:
            print(error)
        finally:
            if self.cur is not None:
               self.cur.close()
            if self.conn is not None:
                self.conn.close()

    def update_user_email(self, a=str, b=int):
        try:
            self.conn = psycopg2.connect(host=host, dbname=database, user=username, password=pwd, port=port_id)
            self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            update_script = ''' UPDATE users SET email = %s WHERE user_id = %s'''
            update_values = (a, b)

            self.cur.execute(update_script, update_values)
            self.conn.commit()
        except Exception as error:
            print(error)
        finally:
            if self.cur is not None:
                self.cur.close()
            if self.conn is not None:
                self.conn.close()


        pass


    def delete_from_table(self, a):
        try:
            self.conn = psycopg2.connect(host=host, dbname=database, user=username, password=pwd, port=port_id)
            self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            delete_script = ''' DELETE FROM users WHERE user_id = %s'''
            delete_values = (int(a),)

            self.cur.execute(delete_script, delete_values)
            self.conn.commit()
        except Exception as error:
            print(error)
        finally:
            if self.cur is not None:
                self.cur.close()
            if self.conn is not None:
                self.conn.close()



