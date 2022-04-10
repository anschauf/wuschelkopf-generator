import os


rootdir = 'assets/'

ending = '_Zeichenfläche 1.png'


def main():
    print("Test")

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith(ending):
                new_file = file.replace(ending, '.png')
                os.rename(os.path.join(subdir, file), os.path.join(subdir, new_file))


main()