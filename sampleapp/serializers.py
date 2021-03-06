from rest_framework import serializers, status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import UserProfile

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
	def validate(self, attrs):
		print('in')
		user = authenticate(username=attrs['username'], password=attrs['password'])
		if user is not None:
			if user.is_active:
				data = super().validate(attrs)
				refresh = self.get_token(self.user)
				refresh['username'] = self.user.username
				try:
					obj = UserProfile.objects.get(user=self.user)
					refresh['employeeRole'] = obj.employeeRole
					data["refresh"] = str(refresh)
					data["access"] = str(refresh.access_token)
					data["employee_id"] = self.user.id
					data['user_name']= self.user.username
					data["employeeRole"] = obj.employeeRole
					data['first_name']= self.user.first_name
					data['last_name']= self.user.last_name
				except Exception as e:
					raise serializers.ValidationError('Something Wrong!')
				return data
			else:
				raise serializers.ValidationError('Account is Blocked')
		else:
			raise serializers.ValidationError('Incorrect userid/email and password combination!')


class RegistrationSerializer(serializers.ModelSerializer):

	email		 	= serializers.EmailField(style={'input_type': 'email'})
	username	    = serializers.CharField(min_length=1)


	class Meta:
		model = UserProfile
		fields = ['email','username', 'password']
		extra_kwargs = {
				'password': {'write_only': True,'min_length':8},
		}


	def	save(self):

		account = UserProfile(
					email=self.validated_data['email'],
					username=self.validated_data['username'],
                    password=self.validated_data['password']
				)
		account.save()
		return account
