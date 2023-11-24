import os
import shutil
import sys

MODLIST_DIRECTORY = "modlist.html"
STEAM_USERNAME = "username"
STEAMCMD_DIRECTORY = "/root/Steam/steamcmd.sh"
WORKSHOP_DIRECTORY = "/root/Steam/steamapps/workshop/content/107410/"
SERVER_DIRECTORY = "/root/Steam/steamapps/common/Arma 3 Server/"


def iterate_through_html(directory: str):
    mod_ids = []
    with open(directory, "r") as f:
        data = f.read()
        mods = data.split('<tr data-type="ModContainer">')
        for i in mods[1:]:
            splits = i.split('href=')[1].split(" ")[0].split("=")
            mod_ids.append(splits[1].rstrip('"') + "\n")

    with open("modlist.txt", "w") as f:
        f.writelines(mod_ids)


def setup_download_commands(username: str):
    with open("commands.txt", "w") as f:
        f.write(f"login {username}")

    with open("modlist.txt") as f:
        with open("commands.txt", "a") as d:
            data = f.readlines()
            for i in data:
                if i == "0\n":
                    i = i.strip("\n")
                    continue
                d.write(f"\nworkshop_download_item 107410 {int(i)}\n")

            d.write("quit")


def download_mods(directory: str):
    os.system(f"{directory} +runscript commands.txt")


def lowercase_all_mods(directory: str):
    if sys.platform == "linux":
        current_dir = os.getcwd()
        print("Proceeding to lowercase all mods. May take a while.")
        os.system((f"cd {directory}" + "&& find . -depth -exec rename 's/(.*)\/([^\/]*)/$1\/\L$2/' {} \;"))
        os.chdir(current_dir)

def symlink_all_mods(workshop_directory: str, server_directory: str):
    for file in os.listdir(workshop_directory):
        try:
            os.symlink(f"{workshop_directory}{file}", f"{server_directory}@{file}")
        except FileExistsError:
            pass


def generate_mod_string():
    container = ""
    with open("modlist.txt", "r") as f:
        data = f.readlines()
        for i in data:
            temp = i.rstrip('\n')
            container += f"@{temp};"
    with open("mod_string.txt", "w") as f:
        f.write(container)


def delete_mods(workshop_directory: str, server_directory: str):

    for d in os.listdir(workshop_directory):
        print(f"Removing {workshop_directory}{d}")
        try:
            shutil.rmtree(f"{workshop_directory}{d}")
        except FileNotFoundError:
            continue
        
    for d in os.listdir(server_directory):
        if os.path.islink(d) and not(i == d):
            print(f"Removing {server_directory}{d}")
            os.remove(f"{server_directory}{d}")
        else:
            continue


def main():
    while True:
        menu = str(input("""================================================================================
        What would you like to do?
        1. Run all modlist setup methods (2-7).
        2. Return mod IDs as .txt
        3. Setup download commands.
        4. Download mods.
        5. Lowercase all mods.
        6. Symlink all mods.
        7. Generate mod string.
        8. Delete all mods.
        9. Exit.\n"""))
        if menu == "1":
            iterate_through_html(MODLIST_DIRECTORY)
            setup_download_commands(STEAM_USERNAME)
            print("Proceeding to download mods.")
            download_mods(STEAMCMD_DIRECTORY)
            download_mods(STEAMCMD_DIRECTORY)
            lowercase_all_mods(WORKSHOP_DIRECTORY)
            symlink_all_mods(WORKSHOP_DIRECTORY, SERVER_DIRECTORY)
            generate_mod_string()
            print("Mod string saved to mod_string.txt")
        elif menu == "2":
            iterate_through_html(MODLIST_DIRECTORY)
        elif menu == "3":
            setup_download_commands(STEAM_USERNAME)
        elif menu == "4":
            download_mods(STEAMCMD_DIRECTORY)
        elif menu == "5":
            lowercase_all_mods(WORKSHOP_DIRECTORY)
        elif menu == "6":
            symlink_all_mods(WORKSHOP_DIRECTORY, SERVER_DIRECTORY)
        elif menu == "7":
            generate_mod_string()
        elif menu == "8":
            delete_mods(WORKSHOP_DIRECTORY, SERVER_DIRECTORY)
        elif menu == "9":
            sys.exit()
        else:
            print("Invalid input.")
        print("Operation completed successfully.")


if __name__ == "__main__":
    main()
