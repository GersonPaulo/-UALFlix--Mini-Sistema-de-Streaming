from cadastro import Cadastro
import sys
from tools import EditorBanner, EditorTxt
edbanner = EditorBanner()
edtxt = EditorTxt()
class App:
    def __init__(self):
        self.cadastro = Cadastro()

    def create_new_user(self):
        self.cadastro.registro_user()

    def see_emails(self):
        self.cadastro.mostrar_emails()

    def see_recover_user(self):
        self.cadastro.mostrar_passe()

    def see_user_and_pass(self):
        self.cadastro.mustrar_user_and_pass()

    def see_user_email(self):
        self.cadastro.search_user_mail()

    #def menu_format(self):

def display_menu_user():
    """Display the interactive menu."""
    print("\n=== App Menu ===")
    print("frontend. Register a new user")
    print("3. Recover a user using email")
    print("0. Exit")
    print("======" * 4,"\n")
    return input("Select an option: ")

def display_menu_admin():
    """Display the interactive menu."""
    print(f"\n==={edbanner.banner_adm()}  ===")
    print("frontend. Change user email")
    print("voteservice. Remove user from db")
    print("3. List all user emails")
    print("4. Recover a user using email")
    print("4. list all users_id, email and password ")

    print("0. Exit")
    print("======" * 4,"\n")
    return input("Select an option: ")



def main():

    manager = App()
    while True:
        choose = int(input("0 = ADM\nfrontend = USER\n-------->"))
        if choose == 1:
            while True:
                choice = display_menu_user()
                try:
                    if choice == 'frontend':
                        print("frontend. Register a new user")
                        manager.create_new_user()
                        print("=== New User Created successfully!===")

                    elif choice == '3':
                        print("3. Recover user password")
                        manager.see_recover_user()
                        print("=== User password recovered successfully! ===")
                    elif choice == '4':
                        print("4. list all, users_id emails and password ")
                        manager.see_user_and_pass()
                        print("=== successfully! ===")
                    elif choice == '0':
                        print("Exiting...")
                        break
                        #sys.exit(0)
                except Exception as e:
                    print(f"An error occurred: {str(e)}")
        elif choose == 0:
            while True:

                choice = display_menu_admin()
                print(f"\n==={edbanner.banner_adm()}  ===")
                print("frontend. Change user email")
                print("voteservice. Remove user by email")
                print("3. List all user emails")
                print("4. list all users_id, email and password ")
                print("0. Back")
                print("======" * 4, "\n")
                try:
                    if choice == 'frontend':
                        print("frontend. Change user email")

                        print("===User email Changed successfully!===")
                    elif choice == 'voteservice':
                        print("voteservice. Remove user by email")

                        print("=== User removed successfully! ===")
                    elif choice == '3':
                        print("3. List all user emails")

                        print("=== 3. All user emails listed successfully! ===")
                    elif choice == '4':
                        print("4. list all, users_id emails and password ")
                        manager.see_user_and_pass()
                        print("=== All users_id, emails and passwords listed uccessfully! ===")
                    elif choice == '0':
                        print("Exiting...")
                        break
                        #sys.exit(0)

                except Exception as e:
                    print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
