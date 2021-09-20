import os
import os.path
import shutil
import optparse

def main():
    parser = optparse.OptionParser()

    # dataset path
    parser.add_option('-f', '--folder', dest='folder')        
    # quantity of data to be splitted into 'training' folder). 
    parser.add_option('-q', '--quantity', dest='quantity')
    # split data using probability? E.g: '-p 80' will mean '80% of the data'.
    parser.add_option('-p', '--percentage', dest='percentage')

    options, args = parser.parse_args()

    folder = options.folder
    quantity = options.quantity
    percentage = options.percentage

    if not options.folder:
        usage()
        exit()

    # TODO: try/catch
    dataset = os.path.join(str(folder))
    copy_files_to_folders(dataset)


def usage():
    print("""Split your data into 'training' and 'validation' folders. By default, it will take 80% of all your data and put into the 'training' folder and the remaining into the 'validation' folder.""")
    print('You can change the quantity/percentage using the arguments.')
    print('')

    print('Positional arguments:')
    print("     -f, --folder              Path to the dataset folder (containing the directories with the data).")
    print('')
    print('Optional arguments:')
    print("     -q, --quantity            Quantity of the data of all dataset folders to be inserted into 'training' folder. [Default: 80% of the data.]")
    print("     -p, --percentage          Use percentage? Instead of '80' items, it will be 80% of the items.")

    print('')

    print('Examples')

    print('')
    print("Insert 60% of the data of the specified folder into 'training' folder and 40% into 'validation' folder.")
    print('     python3 folder-partition.py -f /home/biscoitinho/mnist_dataset -q 60 -pe')
    print('')
    print("Insert 800 of the data of the specified folder into 'training' folder and the rest into the 'validation' folder.")
    print('     python3 folder-partition.py --folder /home/biscoitinho/mnist_dataset --quantity 800')


def copy_files_to_folders(path):
    validation = path + '/validation'
    training = path + '/training'

    # original directories (without validation and training)
    original_directories = []

    directories = os.listdir(path)
    for _dir in directories:
        original_directories.append(_dir)

    create_training_and_validation_dir(path)

    split_files_into_folders(original_directories, validation, path)
    split_files_into_folders(original_directories, training, path)

    print('Done.')


def split_files_into_folders(original_directories, new_path, path):
    for d in original_directories:
        # cd to training/validation folder
        os.chdir(new_path)
        # create original folders
        os.makedirs(d, exist_ok=True)
        # cd to created folder
        os.chdir(d)

        current_directory = os.path.abspath(os.getcwd())
        root_dir = path + '/' + d
        # copy files from root directory to the new one
        shutil.copytree(root_dir, current_directory, dirs_exist_ok=True)


def create_training_and_validation_dir(directory):
    os.makedirs(directory + '/training', exist_ok=True)
    os.makedirs(directory + '/validation', exist_ok=True)


if __name__ == '__main__':
    main()
