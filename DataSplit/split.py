import os
import random
import shutil

def create_test_folder(source_dir, test_dir, percentage=0.15):
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    
    # Iterate through each subfolder in the source directory
    for subdir in os.listdir(source_dir):
        subdir_path = os.path.join(source_dir, subdir)
        
        if os.path.isdir(subdir_path):
            # Create corresponding subfolder in the test directory
            test_subdir_path = os.path.join(test_dir, subdir)
            if not os.path.exists(test_subdir_path):
                os.makedirs(test_subdir_path)
            
            # List all files in the current subfolder
            files = [f for f in os.listdir(subdir_path) if os.path.isfile(os.path.join(subdir_path, f))]
            
            # Randomly select 15% of the files
            num_files_to_move = int(len(files) * percentage)
            files_to_move = random.sample(files, num_files_to_move)
            
            # Move the selected files to the test subfolder
            for file in files_to_move:
                source_file_path = os.path.join(subdir_path, file)
                dest_file_path = os.path.join(test_subdir_path, file)
                shutil.move(source_file_path, dest_file_path)

if __name__ == "__main__":
    source_directory = "/realwaste-main/RealWaste"
    test_directory = os.path.join(source_directory, "realwaste-test")
    
    create_test_folder(source_directory, test_directory)
