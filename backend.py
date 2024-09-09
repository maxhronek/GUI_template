import sys

def process_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        # Process the content as needed
        return f"File contents:\n{content}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        result = process_file(file_path)
        print(result)
    else:
        print("No file path provided")