## Folder partition
Split your dataset into training and validation folders through terminal, without code implementation.

![Alt text](folder-partition-example.png?raw=true)

### Installation
You can download folder_partition by cloning the Git repository:    

    git clone https://github.com/Biscoitinhoo/folder-partition/
    
### Usage
To see the help section, use:

    python3 folder_partition.py -h
                       
### Arguments:
    
    -f      Path to the dataset. (positional)
    -q      Quantity of data to be inserted into training folder. The difference will be inserted into validation. (optional)
    -p      Percentage to be inserted into training/validation folder (max 100). (optional)
    -q      Quantity of data to be inserted into training folder. The rest will be inserted into validation. (optional)
    -p      Use quantity as percentage. Instead of 80 items (quantity), for example, it will be 80% of all your data inside each folder. (optional)
    
### Examples
All examples take in consideration 1000 data into each folder.

Split data in default mode (80% of the data into training folder, 20% into validation)

    python3 folder-partition.py -f /home/biscoitinho/dogs-and-cats
    Output: 800 files into training, 200 into validation  
 

Split data with specific quantity.  

    python3 folder-partition.py -f /home/biscoitinho/dogs-and-cats -q 600
    Output: 600 files into training, 400 into validation.
    
    
Split data using percentage

    python3 folder-partition.py -f /home/biscoitinho/dogs-and-cats -p 50
    python3 folder-partition.py -f /home/biscoitinho/dogs-and-cats -q 50 -p
    Output: 500 files into training, 500 into validation.
