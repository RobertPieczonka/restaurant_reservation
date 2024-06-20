from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Table, Reservation, MenuItem
from .forms import ReservationForm
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from datetime import datetime, timedelta

#Rejestracja
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_")
    else:
        form = UserCreationForm()
    return render(request, "reserv/register.html", {"form": form})

def login_(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("homepage")
    else:
        form = AuthenticationForm()
    return render(request, "reserv/login.html", {"form": form})

def logout_(request):
    if request.method == "POST":
        logout(request)
        return redirect("login_")

def homepage(request):
    tables = Table.objects.all()
    return render(request, 'reserv/homepage.html', {'tables': tables})

def restaurant_menu(request):
    # tables = Table.objects.all()
    items = MenuItem.objects.all()
    return render(request, 'reserv/restaurant_menu.html', {'items': items})

@login_required(login_url='/login')
def reserve_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('reservation_user')
    else:
        # Pobierz dane z formularza GET
        # Zainicjuj formularz danymi z żądania GET
        form = ReservationForm(initial={
            'table': request.GET.get('table'),
            'date': request.GET.get('date'),
            'time': request.GET.get('time'),
            'duration': request.GET.get('duration'),
            'name': request.user.username.title()
        })
       
    return render(request, 'reserv/reservation_form.html', {'form': form})


@login_required(login_url='/login')
def reservation_user(request):
    if request.method == 'POST':
        reservation = get_object_or_404(Reservation, id=request.POST.get('id'))
        reservation.delete()
        return redirect('reservation_user')
    else:
        reservations = Reservation.objects.filter(user=request.user.id)
        reservation_status = []
        for reservation in reservations:
            # Sprawdź, czy data i godzina rezerwacji są wcześniejsze niż obecna data i godzina
            if reservation.date < datetime.now().date() or (reservation.date == datetime.now().date() and reservation.time < datetime.now().time()):
                status = "Miniona"
            else:
                status = "Oczekuje"
            reservation_status.append((reservation, status))

    return render(request, 'reserv/reservation_user.html', {'reservations_status': reservation_status})


@require_GET
def check_availability(request):
    date = request.GET.get('date')
    time = request.GET.get('time')
    duration = request.GET.get('duration')

    if not date or not time or not duration:
        return JsonResponse({'tables': []})

    date_time = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
    duration_hours = int(duration)
    end_time = date_time + timedelta(hours=duration_hours)

    reservations_on_date = Reservation.objects.filter(date=date)

    available_tables = list(Table.objects.values_list('number', flat=True))

    for reservation in reservations_on_date:
        reservation_start = datetime.combine(reservation.date, reservation.time)
        reservation_end = reservation_start + timedelta(hours=reservation.duration)
        if not (end_time <= reservation_start or date_time >= reservation_end):
            if reservation.table.number in available_tables:
                available_tables.remove(reservation.table.number)

    return JsonResponse({'tables': available_tables})