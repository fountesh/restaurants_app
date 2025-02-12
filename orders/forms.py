from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["phone_number", "address", "payment_method"]
        widgets = {
            "payment_method": forms.RadioSelect(choices=Order.PAYMENT_METHODS),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Отримуємо користувача з kwargs
        super(OrderForm, self).__init__(*args, **kwargs)
        
        if user and user.is_authenticated:
            # Підставляємо дані з профілю користувача
            if hasattr(user, 'profile'):
                self.fields['phone_number'].initial = user.profile.phone_number
                self.fields['address'].initial = user.profile.address