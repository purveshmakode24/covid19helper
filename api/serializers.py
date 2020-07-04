from rest_framework import serializers
from .models import Category, Job, Applicant
from django.contrib.auth.models import User

# serialaizers provides read and write functionality by default

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name', 'slug', 'created_at')


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'job_offered_by', 'category', 'country', 'city', 'name', 'description', 'slug', 'available', 'created_at')


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ('id', 'applicant_name', 'job_name', 'created_at')
       
# changed write functionality down here
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password':{'write_only': True, 'required': True}}

    # hashed password by overwriting built-in method down here
    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        return user