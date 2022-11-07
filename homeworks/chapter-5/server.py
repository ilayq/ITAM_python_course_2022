from uvicorn import run
from fastapi import FastAPI
from argparse import ArgumentParser
from settings import DB_NAME
from Student import Student, WrongData
from DB import DB
from typing import Union


app = FastAPI()
db = DB(db_name=DB_NAME)


if __name__ == '__main__':
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--db",
                            action="store_true",
                            required=False,
                            help="run --db to create table in db"
                            )
    arg_parser.add_argument("--clear",
                            action="store_true",
                            required=False,
                            help="run --clear to clear rows in db"
                            )
    args = arg_parser.parse_args()
    if args.db and args.clear:
        print("run only --db or only --clear")
    elif args.db:
        db.create_table()
        print(f"Table students created in {DB_NAME}")
    elif args.clear:
        db.clear_table()
    else:
        run('server:app')


@app.get('/')
def root() -> dict[str, str]:
    return {'message': 'api to work with students, \n post /student/add?student_id={student_id}&name={name}&group={group} -- add student \nget /student/?student_id={student_id}/ -- get info about student \nput /student/update/?student_id={student_id}&name={name}&group={group} -- update info about student \nget /student/all/ -- get info about all students'}


@app.post(path="/student/add/")
def add_student(student_id: int, name: str, group: str) -> Union[dict[str, bool], dict[str, Exception]]:
    try:
        st = Student(student_id, name, group)
        return {"message": db.add_student_to_table(st)}
    except Exception as e:
        return {"message": e}


@app.get(path='/student')
def get_info_about_student(student_id: int) -> Union[dict[str, Exception], dict[str, Union[int, str]]]:
    if type(student_id) != int:
        with WrongData as e:
            return {"message": e}
    try:
        return db.get_info_about_student_by_id(student_id)
    except Exception as e:
        return {"message": e}


@app.put(path='/student/update/')
def update_info_about_student(student_id: int, name: str, group: str) -> Union[dict[str, Exception], dict[str, bool]]:
    try:
        st = Student(student_id, name, group)
        return {"message": db.update_info_about_student(st)}
    except Exception as e:
        return {"message": e}


@app.get(path='/student/all')
def get_all_info() -> dict[str, list]:
    try:
        return db.get_all_info()
    except Exception as e:
        return {"message": [e]}
