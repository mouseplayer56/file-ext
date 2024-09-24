import os

dev_bool = False  # DEFAULT: bool(False). Change to bool(True) if you want to skip input processes.
global_exit_key = str("!exit")  # the keyword to leave the program's user input functions, if dev is False. Useful for weird file extensions.
disallowed_extensions = [".bmp"]  # if dev is True/running regular ceid(), you'll have to add file extensions in here manually. if not, this program will let you add them.
allowed_extensions = [".txt"]  # this is the extension
default_path = os.path.join(os.path.dirname(__file__))  # __file__ can be modified by encapsulating os.path.dirname(__file__) in os.path.join( with another file path as the directory.
# alternatively, if modifying the above is complex, you can simply move the actual python file in a super-directory/same directory as the files you want to modify


def get_file_path(is_dev, file_path_og, exit_key):  # gets the file path to be modified by the user.
    file_path, file_input = file_path_og, None
    while not is_dev and file_input != exit_key:
        file_input = input(f"'{os.path.dirname(__file__)}'\nEnter path of folder in this directory; type {exit_key} to use the above directory only.\n")
        if file_input != exit_key:
            try:
                file_path = os.path.join(file_path, file_input)
                print(file_path)
            except:
                file_path = file_path_og
                print(Exception)
            finally:
                return file_path
    if is_dev:
        return file_path_og


def get_ext_list(is_dev, ext_list, exit_key):  # gets the list of extensions you want to have modified
    user_pop_app, user_extensions_input = None, None
    while not is_dev and user_pop_app != exit_key:
        user_pop_app = str(input(f"Type {exit_key} to verify changes & modify files\nWould you like to POP or APPEND unwanted extensions?\n").lower())
        user_extensions_input = None
        if user_pop_app == exit_key:
            try:
                len(ext_list)
                return ext_list
            except:
                raise Exception
            finally:
                pass
        while user_pop_app in ["pop", "append"] and user_extensions_input != exit_key:
            user_extensions_input = str(input(f"{ext_list}\nType {exit_key} to stop.\nEnter Restricted File Extensions, beginning with '.' .\n"))
            if user_extensions_input != exit_key:
                if user_pop_app == "pop":
                    ext_list.remove(user_extensions_input)
                elif user_pop_app == "append":
                    ext_list.append(user_extensions_input)
    if is_dev:
        return ext_list


def get_ext_change(is_dev, ext_change_list, exit_key):
    user_pop_app, user_extensions_input = None, None
    while not is_dev and user_pop_app != exit_key:
        user_pop_app = str(input(f"Type {exit_key} to verify changes & modify files\nWould you like to POP or APPEND wanted extensions?\n").lower())
        user_extensions_input = None
        if user_pop_app == exit_key:
            try:
                len(ext_change_list)
                return ext_change_list
            except:
                raise Exception
            finally:
                pass
        while user_pop_app in ["pop", "append"] and user_extensions_input != exit_key:
            user_extensions_input = str(input(f"{ext_change_list}\nType {exit_key} to stop.\nEnter Desired File Extensions, beginning with '.' .\n"))
            if user_extensions_input != exit_key:
                if user_pop_app == "pop":
                    ext_change_list.remove(user_extensions_input)
                elif user_pop_app == "append":
                    ext_change_list.append(user_extensions_input)
    if is_dev:
        return ext_change_list


def ceid_ask(is_dev_bool, file_path, unwanted_extensions_list, wanted_extensions_list, exit_key):  # stands for "change extension in directory - ask (for end-user)".
    full_path = get_file_path(is_dev_bool, file_path, exit_key)
    unwanted_extensions_list = get_ext_list(is_dev_bool, unwanted_extensions_list, exit_key)
    wanted_extensions_list = get_ext_change(is_dev_bool, wanted_extensions_list, exit_key)

    for file in os.listdir(full_path):
        print(file)
        counter = 0
        for ext in unwanted_extensions_list:
            if file.endswith(ext):
                os.rename(
                    os.path.join(full_path, file),
                    os.path.join(full_path, (os.path.splitext(str(file))[0] + str(wanted_extensions_list[counter])))
                )
                print(f"CHANGED -> {(os.path.splitext(str(file))[0] + str(wanted_extensions_list[counter]))}")
            if counter == len(wanted_extensions_list):
                pass
            else:
                counter += 1


def ceid(use_file_path_bool, unwanted_extensions_list, wanted_extensions_list, file_path, get_print):  # stands for "change extension in directory".
    # use_file_path_bool (UFPB) has 2 states:
    # if True, UFPB will require the FULL PATH of the file you want to modify
    # if False, UFPB will only require the name of the sub-directory that you want to modify, starting from the file location.

    if use_file_path_bool:  # if True
        try:
            full_path = os.path.dirname(file_path)
        except:
            raise f"ERROR: function 'ceid()' requires file_path parameter to be filled!\n{Exception}"
        finally:
            pass
    elif not use_file_path_bool:  # if False
        try:
            full_path = os.path.join(os.path.dirname(__file__), str(file_path))
        except:
            raise f"ERROR: function 'ceid()' requires file_path parameter to be filled!\n{Exception}"
        finally:
            pass

    for file in os.listdir(full_path):
        if get_print:
            print(file)
        counter = 0
        for ext in unwanted_extensions_list:
            if counter == int(len(wanted_extensions_list)) - 1:  # just in case unwanted > wanted.
                pass
            else:
                counter += 1
            if file.endswith(ext):
                print(counter, wanted_extensions_list)
                os.rename(
                    os.path.join(full_path, file),
                    os.path.join(full_path, (os.path.splitext(str(file))[0] + str(wanted_extensions_list[counter])))
                )
                if get_print:
                    print(f"CHANGED -> {(os.path.splitext(str(file))[0] + str(wanted_extensions_list[counter]))}")


# ceid_ask(dev_bool, default_path, disallowed_extensions, allowed_extensions, global_exit_key)

# ceid(False, disallowed_extensions, allowed_extensions, default_path, True)
