import django_filters
from django.contrib.auth.models import User

class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name='username', lookup_expr='icontains')
    email = django_filters.CharFilter(field_name='email', lookup_expr='icontains')
    is_staff = django_filters.BooleanFilter()
    is_superuser = django_filters.BooleanFilter()
    class Meta:
        model = User
        fields = ['username','email','is_staff','is_superuser']