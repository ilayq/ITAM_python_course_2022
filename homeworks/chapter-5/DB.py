import sqlite3
from Student import Student


class DB:
    def __init__(self, db_name: str) -> None:
        self.name = db_name

    def __connect(self) -> sqlite3.connect:
        try:
            con = sqlite3.connect(self.name)
            return con
        except Exception:
            raise

    def create_table(self) -> bool:
        con = self.__connect()
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS students(id, name, student_group)
                    """)
        con.commit()
        con.close()
        return True

    def clear_table(self) -> bool:
        con = self.__connect()
        cur = con.cursor()
        cur.execute("""
                    DELETE from students
                    """)
        con.commit()
        con.close()
        return True

    def add_student_to_table(self, student: Student) -> bool:
        con = self.__connect()
        cur = con.cursor()
        cur.execute("""
            INSERT INTO students VALUES (?, ?, ?)
            """, [student.id, student.name, student.group])
        con.commit()
        con.close()
        return True

    def update_info_about_student(self, student: Student) -> bool:
        con = self.__connect()
        cur = con.cursor()
        cur.execute("""
                    UPDATE students SET name = ?, student_group = ?
                    WHERE id = ?
                    """, [student.name, student.group, student.id])
        con.commit()
        con.close()
        return True

    def get_info_about_student_by_id(self, student_id: int) -> dict:
        con = self.__connect()
        cur = con.cursor()
        result = {}
        for row in cur.execute("""SELECT * FROM students"""):
            if row[0] == student_id:
                result = {'id': row[0],
                          'name': row[1],
                          'group': row[2]
                          }
        con.close()
        return result

    def get_all_info(self) -> dict:
        con = self.__connect()
        cur = con.cursor()
        result = {}
        students = []
        for row in cur.execute("""
                                SELECT * FROM students
                                """):
            students.append(Student(student_id=row[0], name=row[1], group=row[2]))
        con.close()
        for student in students:
            result[student.id] = [student.name, student.group]
        return result
