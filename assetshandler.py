from jinja2 import Environment, FileSystemLoader
import os

# file_loader = FileSystemLoader("assets")
# env = Environment(loader=file_loader)


def title(address):
    return address[:len(address)-4]


def header(file_full_address):
    with open(file_full_address) as f:
        first_line = f.readline()
        first_line = first_line.replace("\n", "")
        f.close()
    return first_line


def body(file_full_address):
    with open(file_full_address, 'r') as f:
        lines = f.readlines()[1:]
        lines = "".join(lines)
        # lines = [i.replace("\n", "<br>") for i in lines]
        f.close()
    return lines


class AssetFile:
    def __init__(self, file):
        self.file = file + '.txt'
        self.cwd = os.getcwd().replace('\\','/')
        self.file_full_address = self.cwd + "/assets/" + self.file
        self.title = title(self.file)
        self.header = header(self.file_full_address)
        self.body = body(self.file_full_address)


class Assets:
    def __init__(self):
        self.cwd = os.getcwd().replace('\\','/')
        self.folder = self.cwd + "/assets/"
        self.folder_list = os.listdir(self.folder)
        self.files_list = [i for i in self.folder_list]
        self.posts_list = [i[:len(i)-4] for i in os.listdir(self.folder)]


class Posts:
    def __init__(self, post):
        self.post = post
