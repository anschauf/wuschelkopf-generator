import os


rootdir = 'assets/'

ending = '_Zeichenfläche 1.png'


def main():
    print("Test")

    count = 0

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith(ending):
                complete_old_file = os.path.join(subdir, file)
                new_file = os.path.join(subdir, file.replace(ending, '.png'))
                os.rename(complete_old_file, new_file)
                print(f'Replaced "{complete_old_file} with {new_file}"')
                count += 1
    print('################################')
    print(f'Total replacement: {count}')


# Run the main function
if __name__ == "__main__":
    main()