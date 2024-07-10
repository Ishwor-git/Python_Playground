from PIL import Image
from sys import argv
import os
from datetime import datetime

option = argv[1]

try:
    img_source = argv[2]
    img_format = argv[3]
    save_dir = f"{datetime.now().strftime('%Y%m%d%H%M%S')}"

except:
    pass
if option == "--help" or option == "-h":
    print(
        """
--- Welcome to ImagCon ---
syntax: python3 [filename] -[options] [raw file / directory] [conversion format]

Example:python3 main.py -dir images/ png
Example: python3 main.py -f images/pokemon.jpg tif

OPTIONS:
--dir / -d  convert all image files in that directory to given format.
           NOTE: non image files like .txt, .csv etc might create error

--file / -f convert single given file to given format

--help / -h Show help options 

--syntax / -s Display syntax

Thanks for using our program
        """
    )
elif option == "--syntax" or option == "-s":
    print(
        "syntax: python3 [filename] -[options] [raw file / directory] [conversion format]"
    )
    print("type option '--help' or '-h' for more info.")

elif option == "--dir" or option == "-d":

    try:
        count = 1
        os.makedirs(save_dir)
        for file in os.listdir(img_source):

            try:
                img = Image.open(f"{img_source}{file}")
                split_name = os.path.splitext(file)
                save_filename = f"{split_name[0]}.{img_format}"

                try:
                    img.save(f"{save_dir}/{save_filename}", img_format)
                    print(
                        f"converted {file} to {save_filename}. No of conversion : {count}"
                    )
                    count += 1
                except:
                    print(f"Unsupported Image type .{img_format}")
                    break

            except:
                print(f"Unable to convert {file}")
                continue

    except:
        print("Error : Unable to run the program; Invalid Syntax")

elif option == "--file" or option == "-f":
    try:

        try:
            img = Image.open(img_source)
            save_filename = f"{save_dir}.{img_format}"

            try:
                img.save(f"{save_filename}", img_format)
            except:
                print(f"Unsupported Image type .{img_format}")

        except FileNotFoundError as err:
            print(err)

        except:
            print(f"unable to convert {img_source}")

    except:
        print("Error : Unable to run the program; Invalid Syntax")
else:
    print("Invalid Option type '--help' or '-h' for more info..")

print("Image conversion completed, terminating program...")
