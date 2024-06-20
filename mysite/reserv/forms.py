from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'date', 'time', 'duration', 'name', 'phone', 'email']
        labels = {
            'table': 'Stolik',
            'date': 'Data',
            'time': 'Godzina',
            'duration': 'Czas trwania',
            'name': 'Imię rezerwującego',
            'phone': 'Numer telefonu',
            'email': 'Email',
        }
        widgets = {
            'table': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'readonly': 'readonly'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'readonly': 'readonly'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Pobieramy wartości początkowe pól formularza
        table_id = self.initial.get('table')
        date = self.initial.get('date')
        time = self.initial.get('time')
        duration = self.initial.get('duration')

        # Jeśli wartości są ustawione, inicjujemy pola formularza
        if table_id:
            self.fields['table'].widget.attrs['value'] = table_id
        if date:
            self.fields['date'].widget.attrs['value'] = date
        if time:
            self.fields['time'].widget.attrs['value'] = time
        if duration:
            self.fields['duration'].widget.attrs['value'] = duration
