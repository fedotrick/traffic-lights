import time
import os

class TrafficLight:
    def __init__(self):
        self.colors = {
            'Красный': '\033[91m', # Красный цвет
            'Желтый': '\033[93m',  # Желтый цвет
            'Зеленый': '\033[92m', # Зеленый цвет
        }
        self.reset_color = '\033[0m'  # Сброс цвета
        self.current_color = 0  # Индекс текущего цвета
        self.color_names = list(self.colors.keys())

    def show(self):
        os.system('clear' if os.name == 'posix' else 'cls')  # Очистка терминала
        print(f"{self.colors[self.color_names[self.current_color]]}{self.color_names[self.current_color]}{self.reset_color}")

    def change(self):
        self.current_color = (self.current_color + 1) % len(self.color_names)

def main():
    traffic_light = TrafficLight()
    
    while True:
        traffic_light.show()
        
        if traffic_light.color_names[traffic_light.current_color] == 'Красный':
            time.sleep(5)  # Красный свет 5 секунд
        elif traffic_light.color_names[traffic_light.current_color] == 'Желтый':
            time.sleep(2)  # Желтый свет 2 секунды
        elif traffic_light.color_names[traffic_light.current_color] == 'Зеленый':
            time.sleep(5)  # Зеленый свет 5 секунд
        
        traffic_light.change()

if __name__ == "__main__":
    main()
