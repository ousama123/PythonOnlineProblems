from dotenv import load_dotenv
import os

load_dotenv()
FILE_PATH = os.getenv('FILE_PATH')
FILE_PATH_DEBUG = os.getenv('FILE_PATH_DEBUG')

def get_data():
    with open(FILE_PATH) as f:
        return f.read()

def main():
    data=get_data()
    rules, updates = data.split('\n\n')
    print(updates)


if __name__ == "__main__":
    main()