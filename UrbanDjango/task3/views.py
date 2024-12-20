from django.shortcuts import render

# Create your views here.
def main_page(request):
    title = 'Главная страница'
    text = 'Главная'
    shop = 'Магазин'
    cart = 'Корзина'
    context = {
        'title': title,
        'text': text,
        'shop': shop,
        'cart': cart
    }
    return render(request, 'fourth_task/main_page.html', context)

def games(request):
    title = 'Магазин'
    text = 'Игры'
    buy = 'Купить'
    back = 'Вернуться обратно'
    games_dict = {'first': "Baldur's Gate III", 'second': "Cyberpunk 2077", 'third': "Dragon Age Veilguard"}
    context = {
        'title': title,
        'text': text,
        'buy': buy,
        'back': back,
        'games_dict': games_dict,
    }
    return render(request, 'fourth_task/games.html', context)

def cart(request):
    title = 'Корзина'
    text = "Извините, Ваша корзина пуста"
    back = 'Вернуться обратно'
    context = {
        'title': title,
        'text': text,
        'back': back
    }
    return render(request, 'fourth_task/cart.html', context)