""""Интроспекция"
Задание:
Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента
и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль,
и другие свойства.
1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации
о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
  - Другие интересные свойства объекта, учитывая его тип (по желанию).

"""

import requests



class Introspection:
    def __init__(self, obj):
        self.obj = obj
    def get_info(self):
        obj_type = type(self.obj)
        attributes = [attr for attr in dir(self.obj)
            if not callable(getattr(self.obj, attr))]
        methods = [attr for attr in dir(self.obj)
            if callable(getattr(self.obj, attr))]
        module = getattr(self.obj, '__module__', 'builtins')

        info = {
            "type": obj_type,
            "attributes": attributes,
            "methods": methods,
            "module": module,
        }
        return info

    def __str__(self):
        return str(self.get_info())


number_info = Introspection(42)
print(number_info)
