import requests
import argparse


url = "http://127.0.0.1:8000"


def add():
    requests.post(url + "/student/add?student_id=1&name=Mikhail&group=bivt-22-7")


def get_info():
    r = requests.get(url + "/student?student_id=1")
    print(r.text)


def get_all_info():
    r = requests.get(url + "/student/all")
    print(r.text)


def update():
    requests.put(url + "/student/update?student_id=1&name=Mikhail&group=bivt-22-6")


if __name__ == "__main__":
    arg = argparse.ArgumentParser()
    arg.add_argument('--add',
                     action="store_true")
    arg.add_argument('--get',
                     action='store_true')
    arg.add_argument('--getinfo',
                     action='store_true')
    arg.add_argument('--update',
                     action='store_true')
    args = arg.parse_args()
    if args.add:
        add()
    elif args.get:
        get_info()
    elif args.getinfo:
        get_all_info()
    elif args.update:
        update()
    else:
        print('no command')
