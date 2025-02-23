
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):

    # name = serializers.CharField(max_length=100)
    # age = serializers.IntegerField()
    # email = serializers.EmailField()
    # phone = serializers.CharField(max_length=11)
    # city = serializers.CharField(max_length=100)

    class Meta:
        model = Student
        # fields = '__all__'
        # exclude = ['id']
        fields = ['name', 'age', 'email', 'phone', 'city']

    def validate(self, data):
        
        if data['age'] < 18:
            raise serializers.ValidationError('Age should be greater than 18')
        return data
    
        if data['name'] :
            for n in data['name']:
                if n.isnumeric():
                    raise serializers.ValidationError('Name should not contain numbers')
                