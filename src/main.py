import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='D:\DS\Terminal\project\secret.env')

author = os.getenv('AUTHOR')

def print_author():
    print(f"Автор проекта: {author}")

print_author()