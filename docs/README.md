# geometric_lib

## Общее описание 

*geometric_lib** - библиотека на языке Python с функциями для вычесления плошади и периметра фигур: квадрата, круга, треугольника, прямоугольника.

все работы велись в ветке "new_feature_561621".

## Возможности


| Файл          | Функции                          |
|---------------|----------------------------------|
|`circle.py`    |`area(r)`,    `perimeter(r)`      |
|`rectangle.py` |`area(a, b)`, `perimeter(a, b)`   |
|`square.py`    |`area(a)`,    `perimeter(a)`      |
|`triangle.py`  |`area(a, h)`, `perimeter(a, b, c)`|


## Использование

```bash
git clone https://github.com/<ваш_логин>/geometric_lib
cd geometric_lib
python -c "import rectangle; print(rectangle.area(3, 4))"
```

## История изменения

### Хеш      Содержимое комита 

#### 1b5cfa3 Я исправил ошибку в файле rectangle.py, был исправлена функция расчета периметра

#### 0070bf2 create a newfile: triangle.py

#### 40722a8 create a newfile: rectangle.py

#### 285475a Add documentation square.py

#### 5241519 Add documentation circle.py

#### 078d12d Add documentation triangle.py

#### 9b2df42 Add documentation rectangle.py
