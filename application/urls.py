from django.urls import path
from .views import ItemView, BuyItemView, OrderView, BuyOrderView

urlpatterns = [
    path('buy/item/<int:pk>', BuyItemView.as_view()),
    path('buy/order/<int:pk>', BuyOrderView.as_view()),
    path('item/<int:pk>', ItemView.as_view(), name = 'item'),
    path('order/<int:pk>', OrderView.as_view(), name = 'order'),
]
