from rest_framework import serializers
from student.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def to_representation(self, instance):
        return {
             "student": {
                "id": instance.id,
                "name": instance.name,
                "age": instance.age,
                "email": instance.email
            },
            "class_info": {
                "student_class": instance.student_class
            }
        
            
        }