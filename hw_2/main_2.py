class Patient:

    def __init__(self, full_name: str, age: int, disease: str):
        """
        Формирует шаблон объекта Patient
        :param full_name: Пренимает ФИО пациента
        :param age: Пренимает возраст пациента
        :param disease: Пренимает заболевание пациента
        """
        self.full_name = full_name
        self.age = age
        self.disease = disease

    def makes_an_appointment(self, date: str):
        """
        Выводит уведомление о записи на прием к врачу на указанную дату
        :param date: Пренимает дату записи на прием
        :return:
        """
        print(f'Вы успешно записаны на прием на следующую дату: {date}\n')




