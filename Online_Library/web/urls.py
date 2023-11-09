from django.urls import path, include
from .views import add_book, edit_book, details_book, edit_profile, delete_profile

from Online_Library.web.views import index, add_profile

urlpatterns = [
    path('', index, name='index'),
    path('books/', include([
        path('add/', add_book, name='add-book'),
        path('edit/<int:pk>/', edit_book, name='edit-book'),
        path('details/<int:pk>/', details_book, name='details-book'),
    ]),
         ),
    path('profile/', include([
        path('profile/add/', add_profile, name='add_profile'),
        path('profile/edit/', edit_profile, name='edit-add_profile'),
        path('profile/delete/', delete_profile, name='delete-add_profile'),
    ]))
]
