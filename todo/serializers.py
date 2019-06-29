from rest_framework import serializers

from todo.models import ToDo
# from todo.models import ToDoDone


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = 'id', 'text' , 'done','cuDate','expDate'
        # model = ToDoDone
        # fields = 'id', 'text' , 'done','cuDate','expDate'