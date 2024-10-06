import os  
  
def replace_string_in_file(file_path, old_string, new_string):  
    try:  
        with open(file_path, 'r', encoding='utf-8') as file:  
            file_data = file.read()  
  
        if old_string in file_data:  
            new_data = file_data.replace(old_string, new_string)  
            with open(file_path, 'w', encoding='utf-8') as file:  
                file.write(new_data)  
        print(f"Processed {file_path}")  
    except Exception as e:  
        print(f"Error processing {file_path}: {e}")  
  
def replace_string_in_directory(directory, old_string, new_string):  
    for root, dirs, files in os.walk(directory):  
        for file in files:  
            file_path = os.path.join(root, file)  
            replace_string_in_file(file_path, old_string, new_string)  
  
if __name__ == "__main__":  
    current_directory = os.getcwd()  
    old_string = "com.tsng.hidemyapplist"  
    new_string = "fuck.app.check"  
      
    print(f"Replacing '{old_string}' with '{new_string}' in files in directory: {current_directory}")
    replace_string_in_directory(current_directory, old_string, new_string)  
    print("Replacement completed.")