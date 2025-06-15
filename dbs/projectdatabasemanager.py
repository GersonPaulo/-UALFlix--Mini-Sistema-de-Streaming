import psycopg2
import psycopg2.extras
import requests
from tools.edits import EditorTxt
host = "localhost"
database = "usuarios"
username = "postgres"
pwd = "101213K"
port_id = "5432"

edtxt = EditorTxt()


class ProjectDatabaseManager:
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
            a = edtxt.negrito_bright_green(f"{' ' * 30}Connected to the database :{database}! ✅  ")
            for table in tables:
                local = edtxt.negrito_bright_magenta(f"{' ' * 30}Table --------------- {table[0]}")
        except Exception as error:
            local = edtxt.charging_bar()
            edtxt.negrito_bright_yellow(f"{' ' * 30}  Failed to connect to the database {database}!  ❌ ")
            edtxt.negrito_red(error)
        finally:
            if self.cur is not None:
                self.cur.close()
            if self.conn is not None:
                self.conn.close()

    def inicializar_database(self):
        try:
            self.conn = psycopg2.connect(host=host, dbname =database, user=username, password=pwd, port=port_id )
            self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            create_script = ''' CREATE TABLE IF NOT EXISTS videos (
                                    video_id INTEGER PRIMARY KEY DEFAULT nextval('video_id_seq2'),
                                    tittle     VARCHAR(255) NOT NULL,
                                    video_url  VARCHAR(255) NOT NULL,
                                    views      int NOT NULL)'''
            self.cur.execute(create_script)
            self.conn.commit()
            print(" Created table videos into the database!✅ ")
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
            insert_script = ''' INSERT INTO videos (title, video_url) VALUES (%s, %s)'''
            insert_values = (a, b)

            edtxt.negrito_green(f"valores inseridos na tabela videos ")
            self.cur.execute(insert_script, insert_values)
            self.conn.commit()
        except Exception as error:
            print(error)
        finally:
            if self.cur is not None:
               self.cur.close()
            if self.conn is not None:
                self.conn.close()

    def insert_title(self, a=str):
        try:
            self.conn = psycopg2.connect(host=host, dbname=database, user=username, password=pwd, port=port_id)
            self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            insert_script = ''' INSERT INTO videos (title) VALUES (%s)'''
            insert_values = (a,)

            edtxt.negrito_green(f"titles inseridos na tabela videos ")
            self.cur.execute(insert_script, insert_values)
            self.conn.commit()
        except Exception as error:
            print(error)
        finally:
            if self.cur is not None:
               self.cur.close()
            if self.conn is not None:

                self.conn.close()
    def insert_video_url(self, a=str):
        try:
            self.conn = psycopg2.connect(host=host, dbname=database, user=username, password=pwd, port=port_id)
            self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            insert_script = ''' INSERT INTO videos (video_url) VALUES (%s)'''
            insert_values = (a,)

            edtxt.negrito_green(f"video_url inserido na tabela videos ")
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
            self.cur.execute('SELECT * FROM videos')

            video_fetch_data = self.cur.fetchall()
            if len(video_fetch_data) > 0:
                return video_fetch_data
            elif len(video_fetch_data) <= 0:
                return False

            self.conn.commit()
        except Exception as error:
            print(error)
        finally:
            if self.cur is not None:
               self.cur.close()
            if self.conn is not None:
                self.conn.close()

    def update_video_info(self, a=str, b=int):
        try:
            self.conn = psycopg2.connect(host=host, dbname=database, user=username, password=pwd, port=port_id)
            self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            update_script = ''' UPDATE videos SET vurl = %s WHERE video_id = %s'''
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
            delete_script = ''' DELETE FROM videos WHERE video_id = %s'''
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

def menu():
    while True:
        print("\nMenu:")
        print("1. Testar conexão com o banco de dados")
        print("2. Inicializar banco de dados")
        print("3. Inserir dados de teste na tabela")
        print("4. Mostrar todos os dados")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            call = ProjectDatabaseManager().test_db_connection()
        elif escolha == "2":
            call2 = ProjectDatabaseManager().inicializar_database()
        elif escolha == "3":
            call3 = ProjectDatabaseManager().insert_title("test_title")
            call33 =ProjectDatabaseManager().insert_video_url("test_url")

        elif escolha == "4":
            call4 = ProjectDatabaseManager().show_all_data()
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
