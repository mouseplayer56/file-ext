# file-ext
## Input the directory of a folder (with the files you want to modify), the extensions you want to replace, and the extensions to replace them with.
Intended for large-scale re-mapping of extensions. Also contains the ability to re-map certain extensions to specific ones, explained further below.

![git_cap](https://github.com/user-attachments/assets/d0866261-bbda-43eb-8c64-7dc7bfbe9742)

Comes with test folder & 3 files in .txt, that you can convert to .bmp to see the image.

**BEGINNER'S NOTE:** If you don't know Python and want to use this, simple open the file-sorter.py file in notepad, and remove both of the "#" symbol and space from the line beginning "ceid_ask(".

![image](https://github.com/user-attachments/assets/14ea9c16-14bb-4436-bb31-9f5403bb1946)

![image](https://github.com/user-attachments/assets/b20154fd-f583-403f-a170-b0885c660d75)

As well, you'll ideally want to keep the file-sorter.py file in either a directory above or at the same directory as the files you want to modify.

**FOR SPECIFIC RE-MAPPING:** you just need the extensions from the two wanted/unwanted lists to be in the same index. If you have more unwanted extensions than wanted extension, the last extension in the wanted list will be used - i.e., it's a global/generic extension for selected files. If you have more wanted extensions than unwanted, the index used will be the same index as the length of unwanted variables.

**_Requires Python 3.12 or later_**
