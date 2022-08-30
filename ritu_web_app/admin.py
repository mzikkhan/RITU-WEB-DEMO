from django.contrib import admin
from .models import Task1Text, Task2Text, Task3Text, Marketplace,Leaderboard,Players,Task1Proof,Task2Proof,Task3Proof,OrderData,Messages

admin.site.register(Task1Text)
admin.site.register(Task2Text)
admin.site.register(Task3Text)
admin.site.register(Task1Proof)
admin.site.register(Task2Proof)
admin.site.register(Task3Proof)
admin.site.register(Marketplace)
admin.site.register(Leaderboard)
admin.site.register(Players)
admin.site.register(OrderData)
admin.site.register(Messages)

