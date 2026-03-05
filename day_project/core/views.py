from django.shortcuts import render
from datetime import datetime


def show_day(request):
    days = [
        "Понеділок", "Вівторок", "Середа",
        "Четвер", "П'ятниця", "Субота", "Неділя"
    ]

    # Отримуємо номер дня (0 = Понеділок, 6 = Неділя)
    day_num = datetime.now().weekday()

    context = {
        'day_name': days[day_num],
        'bg_image': f'core/images/day{day_num}.jpg'
    }
    return render(request, 'core/index.html', context)