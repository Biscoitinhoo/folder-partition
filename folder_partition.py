import os
import os.path
import shutil
import argparse

def main():
    # TODO: change folder argument as positional, not optional.
    parser = argparse.ArgumentParser(description="Split your data into 'training' and 'validation' folders. By default, it will take 80% of all your data and put into the 'training' folder and the remaining into the 'validation' folder.")

    parser.add_argument('-f','--folder', help="Path to the dataset folder (containing the directories with the data).", required=True)
    parser.add_argument('-q','--quantity', help="Quantity of the data of all dataset folders to be inserted into 'training' folder. [Default: 80%% of the data.]")
    parser.add_argument('-p','--percentage', help="Use percentage? Instead of '80' items, for example, it will be 80%% of the items.")

    args = vars(parser.parse_args())

    folder = str(args['folder'])
    quantity = int(args['quantity'])
    percentage = str(args['percentage'])

    dataset = os.path.join(folder)
    copy_files_to_folders(dataset, quantity, percentage)


def copy_files_to_folders(folder, quantity, percentage):
    print('Loading...')
    
    validation_path = folder + '/validation'
    training_path = folder + '/training'

    # original directories (without validation and training)
    original_directories = []    

    directories = os.listdir(folder)
    for _dir in directories:
        original_directories.append(_dir)

    validation_files = []
    training_files = []

    create_training_and_validation_dir(folder)
    
    for dir in original_directories:
        # cd to training/validation folder
        os.chdir(validation_path)
        # create original folders
        os.makedirs(dir, exist_ok=True)

    for dir in original_directories:
        # cd to training/validation folder
        os.chdir(training_path)
        # create original folders
        os.makedirs(dir, exist_ok=True)
    

    # change to boolean, using string just for test :p
    if percentage == 'None':
        divide_data(original_directories, quantity, folder, validation_path, validation_path, training_path)
        divide_data(original_directories, quantity, folder, training_path, validation_path, training_path)
    else:
        divide_data_by_percentage()

    print('Done.')


def divide_data_by_percentage():
    return


def divide_data(original_directories, quantity, folder, destination, validation_folder, training_folder):
    for dir in original_directories:
        # cd to training/validation folder
        os.chdir(destination)
        # create original folders
        os.makedirs(dir, exist_ok=True)
        # cd to created folder
        os.chdir(dir)

        absolute_path = folder + '/' + dir
        current_dir = os.path.abspath(os.getcwd())

        total_files = len(os.listdir(absolute_path))

        total_validation_files = total_files - quantity
        total_training_files = total_files - total_validation_files

        transferred_files = 1
        for f in os.listdir(absolute_path):
            file = absolute_path + '/' + f
            if transferred_files <= total_training_files:
                # training_folder + '/' + dir
                shutil.copy(file, training_folder + '/' + dir)
                transferred_files += 1
            else:
                shutil.copy(file, validation_folder + '/' + dir)
            

def create_training_and_validation_dir(directory):
    os.makedirs(directory + '/training', exist_ok=True)
    os.makedirs(directory + '/validation', exist_ok=True)


def usage():
    print('')
    print("Insert 60% of the data of the specified folder into 'training' folder and 40% into 'validation' folder.")
    print('     python3 folder-partition.py -f /home/biscoitinho/mnist_dataset -q 60 -pe')
    print('')
    print("Insert 800 of the data of the specified folder into 'training' folder and the rest into the 'validation' folder.")
    print('     python3 folder-partition.py --folder /home/biscoitinho/mnist_dataset --quantity 800')


if __name__ == '__main__':
    main()