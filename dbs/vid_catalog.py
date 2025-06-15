from  projectdatabasemanager import ProjectDatabaseManager
from tools.edits import  EditorTxt, EditorBanner
import requests


db_manager = ProjectDatabaseManager()
edtxt= EditorTxt()
edbanner = EditorBanner()

flask_endpoints = ["http://127.0.0.1:7000/video_list", "http://192.168.1.74:7000/video_list"]

def fetch_video_list():
    for url in flask_endpoints:
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(e)
            continue
    return {}
videos = fetch_video_list()
vid_keys = list(videos.keys())
vid_values = list(videos.values())
class Catalogo :
    def __init__(self):
        self.title = str()
        self.url = str()
        self.video_dct = videos
        self.video_keys = list(videos.keys())
        self.video_values = list(videos.values())

        pass

    def test_db(self):
        local = db_manager.test_db_connection()
        pass

    #pede o email ao para o registro e verifica se o mail é valido
    def add_title(self):
        try:
            all_data = db_manager.show_all_data()
            db_titles = [videos['title'] for videos in all_data]
            for title in db_titles:
                for i in range(len(vid_keys)):
                    if vid_keys[i] == title:
                        edtxt.negrito_bright_yellow("Titulo já existente no catalogo")
                    elif vid_keys[i] != title:
                        edtxt.negrito_bright_green('=== Titulo valido! ===')
                        self.title = vid_keys[i]
                        return

        except Exception as error:
            edtxt.negrito_red(error)

    #pede a passe ao user e verifica tem no min 8 caracteres
    def add_passe(self):
        temp_var = str(input('insira a sua password min 8 digitos:>'))
        while (len(temp_var)) <= 7 :
            edtxt.negrito_red('=== password invalida minimo 8 digitos')
            temp_var = str(input('digite password:>'))
        if len(temp_var) >7:
            self.v_name = temp_var
            edtxt.negrito_green('password valida')
            return self.v_name

    def registro_user(self):
        u_mail = str(self.add_mail())
        u_passe = str(self.add_passe())
        db_manager.insert_into_table(u_mail, u_passe)

    def mostrar_emails(self):
        all_data = db_manager.show_all_data()
        i = 0
        print(f'{"---" * 5}')
        for user in all_data:
            i+=1
            print(f'user {i} email: {user["email"]}')
            edtxt.negrito_blue(f'user {i} email: {user["email"]}')
        print(f'{"---"*5}')

    def mostrar_passe(self):
        temp_var = str(input('digite o seu email:>'))
        all_data = db_manager.show_all_data()
        i=0
        edtxt.charging_bar()
        for user in all_data:
            i+=1
            if temp_var == user["email"]:
                print(f'User Existente\n{edtxt.negrito_bright_white("***<<Show Credentials>>***")}')
                print(f'{"-"*50}\nemail:{edtxt.negrito_blue(user["email"])}\npassword:{edtxt.negrito_blue(user["password"])}\n{"-"*50}')
                break
            else:
                edtxt.negrito_red(f'{i} {temp_var} ***<<No Credentials>>***')

    def mostrar_user_and_pass(self):
        all_data = db_manager.show_all_data()
        if len(all_data) > 0:
            for user in all_data:
                edtxt.negrito_green(f"user_id: {user['user_id']}")
                edtxt.negrito_bright_white(f" email: {user['email']}, password: {user['password']}")
            print(f'no total temos {len(all_data)} users na prataforma')
        else:
            print('user table empty')

    def search_user_mail(self):
        temp_var = str(input('digite o seu email:>'))
        all_data = db_manager.show_all_data()
        i = 0
        j = True
        for user in all_data:
            i += 1
            if temp_var == user["email"]:
                print(f'user Existente --- email: {user["email"]} match {temp_var}\n***<<Show Credentials>>***')
                print(f'{"---" * 5} \nemail:{user["email"]} \npassword:{user["password"]} \n{"---" * 5}')
                break

    def remove_user(self):
        temp_var = str(input('digite o user_id ------->'))
        all_data = db_manager.show_all_data()
        for user in all_data:
            if temp_var == user["user_id"]:
                apagar_user = db_manager.delete_from_table(user["user_id"])
                edtxt.negrito_bright_red(f'user {user["email"]} deleted !')
                break

    def update_user_email(self):
        try:
            temp_var = int(input('digite o video_id ----->'))
        except ValueError as error:
            edtxt.negrito_red(error)
            temp_var = int(input('digite novamente o user_id ----->'))
        all_data = db_manager.show_all_data()
        for video in all_data:
            if temp_var == video["video_id"]:
                a = self.add_mail()
                update_mail = db_manager.update_user_email( a, ["user_id"])
                edtxt.negrito_bright_white(f'Email: {a} actual')
                edtxt.negrito_bright_yellow('Email updated successfully')
                temp_var2 = True
        if temp_var == False:edtxt.negrito_red(f"---ERROR --- \nId inesistente {temp_var} ")


for key, value in videos.items():
    edtxt.negrito_bright_magenta(f"key: {key}, value: {value}")
for key in (vid_keys):
    edtxt.negrito_bright_cyan(key)
for value in (vid_values):
    edtxt.negrito_bright_blue(value)

print(Catalogo().add_title())
