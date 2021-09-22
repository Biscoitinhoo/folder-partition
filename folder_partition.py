import os
import os.path
import shutil
import argparse

def main():
    parser = argparse.ArgumentParser(description='Description of your program')

    parser.add_argument('-f','--folder', help="Path to the dataset folder (containing the directories with the data).", required=True)
    parser.add_argument('-q','--quantity', help="Quantity of the data of all dataset folders to be inserted into 'training' folder. [Default: 80%% of the data.]")
    parser.add_argument('-p','--percentage', help="Use percentage? Instead of '80' items, for example, it will be 80%% of the items.")

    args = vars(parser.parse_args())

    folder = str(args['folder'])  
    quantity = str(args['quantity'])
    percentage = str(args['percentage'])

    # # TODO: try/catch
    dataset = os.path.join(folder)
    copy_files_to_folders(dataset, quantity, percentage)


def copy_files_to_folders(folder, quantity, percentage):
    # TODO: progress bar
    print('Loading...')
    
    validation = folder + '/validation'
    training = folder + '/training'

    # original directories (without validation and training)
    original_directories = []

    directories = os.listdir(folder)
    for _dir in directories:
        original_directories.append(_dir)

    for dir in original_directories:
        absolute_path = folder + '/' + dir
        total_files = len(os.listdir(absolute_path))

        for file in os.listdir(absolute_path):
            print("Folder '" + dir + "', file: " + file)
            
        print("Total files in '" + dir + "' folder: " + str(total_files))

    create_training_and_validation_dir(folder)

    split_files_into_folders(original_directories, validation, folder)
    split_files_into_folders(original_directories, training, folder)

    print('Done.')


def divide_data_by_percentage(quantity):
    print('percentage')


def divide_data(quantity):
    print('without percentage')


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


def usage():
    print("""Split your data into 'training' and 'validation' folders. By default, it will take 80% of all your data and put into the 'training' folder and the remaining into the 'validation' folder.""")
    print('You can change the quantity/percentage using the arguments.')
    print('')

    print('positional arguments:')
    print("     -f, --folder              Path to the dataset folder (containing the directories with the data).")
    print('')
    print('optional arguments:')
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


if __name__ == '__main__':
    main()