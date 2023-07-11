"""Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании
экземпляра. Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого
предмета и по оценкам всех предметов вместе взятых.
"""
import csv


class NameDescriptor:
    """Проверяет чтобы с заглавной и буквы."""

    def __get__(self, instance, owner):
        return instance.tets_fio

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("ФИО должно быть строкой")
        if not value.istitle():
            raise ValueError("ФИО должно начинаться с заглавной буквы")
        if not value.replace(" ", "").isalpha():
            raise ValueError("ФИО должно состоять только из букв")
        instance.test_fio = value


class Student:
    """Основной."""
    fio = NameDescriptor()

    def __init__(self, fio, subjects_file):
        self.fio = fio
        self.subjects = self.load_subjects(subjects_file)
        self.scores = {my_subject: [] for my_subject in self.subjects}
        self.test_results = {my_subject: [] for my_subject in self.subjects}

    def load_subjects(self, subjects_file):
        """Читает csv файл и в список."""
        subjects = []
        with open(subjects_file, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                subjects.extend(row)
        return subjects

    def add_score(self, subject_2, score):
        """Проверка оценок."""
        if subject_2 not in self.subjects:
            raise ValueError("Нет предмета")
        if 2 > score > 5:
            raise ValueError("Оценка должна быть от 2 до 5")
        self.scores[subject_2].append(score)

    def add_test_result(self, subject_1, result):
        """Проверка результата теста."""
        if subject_1 not in self.subjects:
            raise ValueError("Недопустимый предмет")
        if 0 > result > 100:
            raise ValueError("Результат теста должен быть от 0 до 100")
        self.test_results[subject_1].append(result)

    def average_scores(self):
        """Расчёт среднего балла."""
        total_scores = []
        for subject_scores in self.scores.values():
            total_scores.extend(subject_scores)
        if not total_scores:
            return 0.0
        return sum(total_scores) / len(total_scores)

    def average_test_results(self, subject_3):
        """Расчёт среднего по предметам."""
        if subject_3 not in self.subjects:
            raise ValueError("Недопустимый предмет")
        subject_results = self.test_results[subject_3]
        if not subject_results:
            return 0.0
        return sum(subject_results) / len(subject_results)


if __name__ == '__main__':
    student = Student("Иванов Иван Иванович", "subjects.csv")
    student.add_score("Математика", 4)
    student.add_score("Математика", 2)
    student.add_test_result("Математика", 80)
    student.add_test_result("Математика", 90)
    student.add_score("Физика", 3)
    student.add_test_result("Физика", 75)
    print("Средний балл по оценкам:", student.average_scores())
    for subject in student.subjects:
        average_test_results = student.average_test_results(subject)
        print(f"Средний балл по тестам по предмету {subject}:", average_test_results)
