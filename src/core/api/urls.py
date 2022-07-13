    AddressCreateView,
    AddressUpdateView,
    AddressDeleteView,
    OrderItemDeleteView
    OrderItemDeleteView,
    PaymentListView
)

urlpatterns = [
@@ -35,4 +36,6 @@
         OrderItemDeleteView.as_view(), name='order-item-delete'),
    path('order-item/update-quantity/',
         OrderQuantityUpdateView.as_view(), name='order-item-update-quantity'),
    path('payments/', PaymentListView.as_view(), name='payment-list'),

]
