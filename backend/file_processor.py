def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return f"File content of {file_path}:\n\n{content}"
    except Exception as e:
        return f"Error processing file {file_path}: {str(e)}"