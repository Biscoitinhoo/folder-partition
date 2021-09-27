import os
import os.path
import shutil
import argparse

def main():
    # TODO: change folder argument as positional, not optional.
    parser = argparse.ArgumentParser(description="Split your data into 'training' and 'validation' folders. By default, it will take 80% of all your data and put into the 'training' folder and the remaining into the 'validation' folder.")
    argument = parser.add_mutually_exclusive_group()

    parser.add_argument('-f','--folder', help="Path to the dataset folder (containing the directories with the data).", required=True)
    argument.add_argument('-q','--quantity', help="Quantity of data to be inserted into training folder. The difference will be inserted into validation [Default: 80%% into training].", required=False)
    argument.add_argument('-p','--percentage', help="Percentage to be inserted into training/validation folder (max 100).", required=False)

    args = vars(parser.parse_args())

    folder = str(args['folder'])
    quantity = args['quantity']
    percentage = args['percentage']

    dataset = os.path.join(folder)
    copy_files_to_folders(dataset, quantity, percentage)


def copy_files_to_folders(folder, quantity, percentage):
    print('Loading...')
    
    validation_path = folder + '/validation'
    training_path = folder + '/training'

    # original directories to be copied
    original_directories = []    

    directories = os.listdir(folder)
    for _dir in directories:
        original_directories.append(_dir)

    create_training_and_validation_dir(folder)
    
    # create original folders inside validation/training folders
    for dir in original_directories:
        os.chdir(validation_path)
        os.makedirs(dir, exist_ok=True)

        os.chdir(training_path)
        os.makedirs(dir, exist_ok=True)

    # TODO: create only one method, they do basically the same thing. also fix these parameters.
    if quantity:
        divide_data_by_quantity(original_directories, int(quantity), folder, validation_path, validation_path, training_path)
    if percentage:
        divide_data_by_percentage(original_directories, int(percentage), folder, training_path, validation_path, training_path)
    if not quantity and not percentage:
        divide_data_default_mode(original_directories, validation_path, folder, training_path, validation_path)

    print('Done.')


def divide_data_default_mode(original_directories, destination, folder, training_folder, validation_folder):

    for dir in original_directories:
        files_inserted_into_training = 0
        files_inserted_into_validation = 0

        # cd to training/validation folder
        os.chdir(destination)
        # cd to created folder
        os.chdir(dir)

        absolute_path = folder + '/' + dir
        total_files = len(os.listdir(absolute_path))

        total_training_files = int(0.8 * total_files)

        transferred_files = 1
        for f in os.listdir(absolute_path):
            file = absolute_path + '/' + f

            if transferred_files <= total_training_files:
                shutil.copy(file, training_folder + '/' + dir)
                files_inserted_into_training += 1

                transferred_files += 1
            else:
                shutil.copy(file, validation_folder + '/' + dir)
                files_inserted_into_validation += 1

        print_copied_files(files_inserted_into_training, files_inserted_into_validation, total_files, dir)


def divide_data_by_percentage(original_directories, percentage, folder, destination, validation_folder, training_folder):
    for dir in original_directories:
        files_inserted_into_training = 0
        files_inserted_into_validation = 0

        os.chdir(destination)
        os.chdir(dir)

        absolute_path = folder + '/' + dir
        total_files = len(os.listdir(absolute_path))

        total_training_files = int((percentage * total_files) / 100)

        transferred_files = 1
        for f in os.listdir(absolute_path):
            file = absolute_path + '/' + f

            if transferred_files <= total_training_files:
                shutil.copy(file, training_folder + '/' + dir)
                files_inserted_into_training += 1

                transferred_files += 1
            else:
                shutil.copy(file, validation_folder + '/' + dir)
                files_inserted_into_validation += 1

        print_copied_files(files_inserted_into_training, files_inserted_into_validation, total_files, dir)


def divide_data_by_quantity(original_directories, quantity, folder, destination, validation_folder, training_folder):
    for dir in original_directories:
        files_inserted_into_training = 0
        files_inserted_into_validation = 0

        os.chdir(destination)
        os.chdir(dir)

        absolute_path = folder + '/' + dir

        total_files = len(os.listdir(absolute_path))

        total_validation_files = total_files - int(quantity)
        total_training_files = total_files - total_validation_files

        transferred_files = 1
        for f in os.listdir(absolute_path):
            file = absolute_path + '/' + f
            
            if transferred_files <= total_training_files:
                shutil.copy(file, training_folder + '/' + dir)
                files_inserted_into_training += 1

                transferred_files += 1
            else:
                shutil.copy(file, validation_folder + '/' + dir)
                files_inserted_into_validation += 1

        print_copied_files(files_inserted_into_training, files_inserted_into_validation, total_files, dir)
    

def create_training_and_validation_dir(directory):
    os.makedirs(directory + '/training', exist_ok=True)
    os.makedirs(directory + '/validation', exist_ok=True)


def print_copied_files(training, validation, total_files, directory):
    print('Directory ' + directory + ', ' + str(total_files) + ' files. ' + str(training) + ' files into training, ' + str(validation) + ' files into validation.')


if __name__ == '__main__':
    main()