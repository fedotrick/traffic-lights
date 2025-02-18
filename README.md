# traffic-lights

Этот проект реализует простой светофор в терминале на Python. Светофор отображает три цвета: красный, желтый и зеленый, с соответствующими таймерами для каждого цвета.

## Начало работы

### Требования

- Python 3.x
- Рабочая среда с поддержкой ANSI-кодов (терминал, поддерживающий цвет)

### Установка

1. Клонируйте этот репозиторий:

   ```bash
   git clone https://github.com/fedotrick/traffic-lights.git
   cd ваш-репозиторий
   ```

2. Убедитесь, что Python установлен на вашем компьютере. Проверьте версию Python:

   ```bash
   python --version
   ```

### Запуск

Для запуска светофора выполните следующую команду в терминале:

```bash
python main.py
```

## Как это работает

Скрипт использует ANSI-коды для отображения цветов в терминале. Он циклически переключается между тремя цветами светофора:

- **Красный**: 5 секунд
- **Желтый**: 2 секунды
- **Зеленый**: 5 секунд

Каждый цвет отображается в соответствующем цвете текста в терминале.

## Код

Основной код расположен в файле `main.py`. Вот краткое описание его структуры:

- **TrafficLight**: класс, отвечающий за логику светофора и отображение цветов.
  - `__init__`: инициализирует цвета и текущий цвет.
  - `show`: отображает текущий цвет.
  - `change`: меняет цвет на следующий.
  
- **main**: основная функция, которая запускает цикл светофора.

## Пример вывода

При запуске скрипта в терминале вы будете видеть следующий вывод, который будет меняться каждые 2-5 секунд:

```
Красный
```
(через 5 секунд)
```
Желтый
```
(через 2 секунды)
```
Зеленый
```
(через 5 секунд)
```

## Контакты

Если у вас есть вопросы или предложения, не стесняйтесь связаться со мной по электронной почте: warriorpacis@yandex.ru.
