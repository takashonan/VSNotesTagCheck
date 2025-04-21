import os
import sys

def check_vsnote_header(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Skip empty files
    if not lines:
        return True
    
    # Remove invisible characters from each line for comparison
    stripped_lines = [line.encode('utf-8').decode('utf-8-sig').strip() for line in lines]
    
    # Find the positions of '---' and '#'
    dash_positions = [i for i, line in enumerate(stripped_lines) if line == '---']
    hash_position = next((i for i, line in enumerate(stripped_lines) if line.startswith('#')), len(stripped_lines))
    
    # Check if there are exactly two '---' before the first '#'
    if len([pos for pos in dash_positions if pos < hash_position]) != 2:
        return False
    
    # Get the positions of the two '---' before the first '#'
    first_dash, second_dash = [pos for pos in dash_positions if pos < hash_position][:2]
    
    # Check if there is exactly one 'tags:' between the two '---'
    tags_count = sum(1 for line in stripped_lines[first_dash+1:second_dash] if 'tags:' in line)
    
    if tags_count != 1:
        return False
    
    # Get the position of 'tags:'
    tags_position = next(i for i, line in enumerate(stripped_lines[first_dash+1:second_dash]) if 'tags:' in line) + first_dash + 1
    
    # Check if there are lines starting with '- ' between 'tags:' and the second '---'
    dash_lines = [lines[i] for i in range(tags_position+1, second_dash) if stripped_lines[i].startswith('- ')]
    
    if not dash_lines:
        return False
    
    # Check if all dash lines have the same indentation
    indentations = [len(line) - len(line.lstrip()) for line in dash_lines]
    
    if len(set(indentations)) != 1:
        return False
    
    # Check if any line has no visible characters after '- '
    for i in range(tags_position+1, second_dash):
        stripped_line = stripped_lines[i]
        if stripped_line == '-':
            return False
    
    return True

def main(folder_path):
    # List to store files that do not follow the rule
    invalid_files = []

    # Iterate over all files in the folder
    for file_name in os.listdir(folder_path):
        # Skip files and folders that start with '.'
        if file_name.startswith('.'):
            continue
        
        file_path = os.path.join(folder_path, file_name)
        
        # Check if it is a file
        if os.path.isfile(file_path):
            # Check if the file follows the rule
            if not check_vsnote_header(file_path):
                invalid_files.append(file_name)

    # Print the invalid files
    print("Files that do not follow the rule:")
    for file_name in invalid_files:
        print(file_name)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python vsnotetagcheck.py <folder_path>")
    else:
        folder_path = sys.argv[1]
        main(folder_path)
