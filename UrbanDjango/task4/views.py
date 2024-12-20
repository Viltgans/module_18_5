from django.shortcuts import render

# Create your views here.
def main_page(request):
    title = 'Главная страница'
    menu_choice = {'main': 'Главная', 'shop': 'Магазин', 'cart': 'Корзина'}
    context = {
        'title': title,
        'menu_choice': menu_choice,
    }
    return render(request, 'fourth_task/main_page.html', context)

def games(request):
    title = 'Магазин'
    text = 'Игры'
    buy = 'Купить'
    back = 'Вернуться обратно'
    games_dict = {'games': ["Baldur's Gate III", "Cyberpunk 2077", "Dragon Age Veilguard"]}
    menu_choice = {'main': 'Главная', 'shop': 'Магазин', 'cart': 'Корзина'}
    context = {
        'title': title,
        'text': text,
        'buy': buy,
        'back': back,
        'games_dict': games_dict,
        'menu_choice': menu_choice,
    }
    return render(request, 'fourth_task/games.html', context)

def carting(request):
    title = 'Корзина'
    message = "Извините, Ваша корзина пуста"
    back = 'Вернуться обратно'
    menu_choice = {'main': 'Главная', 'shop': 'Магазин', 'cart': 'Корзина'}
    context = {
        'title': title,
        'message': message,
        'back': back,
        'menu_choice': menu_choice,
    }
    return render(request, 'fourth_task/cart.html', context)