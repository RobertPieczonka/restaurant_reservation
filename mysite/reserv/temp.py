from reserv.models import MenuItem

def temp():
    menu_items = [
        {'name': 'Margherita', 'description': 'Tradycyjna pizza z sosem pomidorowym, mozzarellą i świeżą bazylią.', 'price': 25.00},
        {'name': 'Spaghetti Carbonara', 'description': 'Klasyczne spaghetti z sosem z jajek, sera pecorino, pancetty i pieprzu.', 'price': 30.00},
        {'name': 'Lasagna', 'description': 'Warstwowa zapiekanka z makaronu, mięsa wołowego, sosu pomidorowego i beszamelu.', 'price': 35.00},
        {'name': 'Risotto ai Funghi', 'description': 'Kremowe risotto z mieszanką świeżych grzybów, parmezanem i pietruszką.', 'price': 32.00},
        {'name': 'Fettuccine Alfredo', 'description': 'Makaron fettuccine w kremowym sosie z masła, śmietany i parmezanu.', 'price': 28.00},
        {'name': 'Bruschetta', 'description': 'Chrupiące grzanki z pomidorami, bazylią, czosnkiem i oliwą z oliwek.', 'price': 18.00},
        {'name': 'Caprese', 'description': 'Sałatka z pomidorów, mozzarelli, świeżej bazylii i oliwy z oliwek.', 'price': 22.00},
        {'name': 'Tiramisu', 'description': 'Klasyczny włoski deser z biszkoptów, mascarpone, kawy i kakao.', 'price': 20.00},
        {'name': 'Panna Cotta', 'description': 'Delikatny deser z gotowanej śmietany, wanilii i sosu owocowego.', 'price': 18.00},
        {'name': 'Minestrone', 'description': 'Gęsta zupa warzywna z fasolą, makaronem i świeżymi ziołami.', 'price': 22.00},
    ]

    for item in menu_items:
        MenuItem.objects.create(**item)
