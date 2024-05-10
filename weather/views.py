from .models import UserDetails
from django.conf import settings
from django.http import JsonResponse
from .utils import format_api_response
from dotenv import load_dotenv
import boto3
import json
load_dotenv()
   
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        phone_number = data.get('phone_number')
        
        client = boto3.client('cognito-idp', region_name='ap-south-1')
        
        try:
            response = client.sign_up(
                ClientId=settings.CLIENT_ID,
                Username=email,  
                Password=password,
                UserAttributes=[
                    {
                        'Name': 'email',
                        'Value': email
                    },
                    {
                        'Name': 'name',
                        'Value': name
                    }
                ]
            )
            print('response->', response)
            cognito_id = response['UserSub']
            print('cognito_userid->', cognito_id)
           
            user = UserDetails.objects.create(
                username=name,
                cognito_user=cognito_id,
                email=email, 
                first_name=first_name,
                last_name=last_name,
                phone_number = phone_number
            )
            response_data = format_api_response(success=True, message="user registered successfully")
            return JsonResponse(response_data)
        except client.exceptions.UsernameExistsException as e:
            response_data = format_api_response(success=False, message="username already exists",error=str(e))
            return JsonResponse(response_data)
        except Exception as e:
            response_data = format_api_response(success=False ,error=str(e))
            return JsonResponse(response_data)
        
        
import json
import boto3
from django.conf import settings
from django.http import JsonResponse
from .models import UserDetails

def verify_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        verification_code = data.get('verification_code')

      
        email = request.headers.get('email')
        print('email', email)
        print('verification_code', verification_code)

        if not email:
            response_data = format_api_response(success=False, message="Email is required in headers")
            return JsonResponse(response_data)
        if not verification_code:
            response_data = format_api_response(success=False, message="Verification code is required")
            return JsonResponse(response_data, status=400)

       
        cognito_client = boto3.client('cognito-idp', region_name='ap-south-1')

        try:
            response = cognito_client.confirm_sign_up(
                ClientId=settings.CLIENT_ID,
                Username=email,
                ConfirmationCode=verification_code
            )
            try:
                user = UserDetails.objects.get(email=email)
                user.is_verified = True
                user.save()
            except UserDetails.DoesNotExist:
                response_data = format_api_response(success=False, message="user does not exist")
                return JsonResponse(response_data) 

     
            response_data = format_api_response(success=True, message="verification success")
            return JsonResponse(response_data)

        except cognito_client.exceptions.UserNotFoundException as e:
            response_data = format_api_response(success=False, message="user does not exist", error=str(e))
            return JsonResponse(response_data)
        except cognito_client.exceptions.CodeMismatchException as e:
            response_data = format_api_response(success=False, message="invalid verification code", error=str(e))
            return JsonResponse(response_data)
        except cognito_client.exceptions.NotAuthorizedException as e:
            response_data = format_api_response(success=False, message="user is already confirmed", error=str(e))
            return JsonResponse(response_data)
        except Exception as e:
            response_data = format_api_response(success=False, message="error occurred", error=str(e))
            return JsonResponse(response_data)





def get_all_users(request):
    try:
        cognito_id = request.cognito_id
        print(cognito_id)
        if cognito_id:
            users = UserDetails.objects.all()
            if not users:
                response_data = format_api_response(success=True, message='no users are present')
                return JsonResponse(response_data)
            
            user_data = [{
                'cognito_id': user.cognito_user,
                'username': user.username,
                'email': user.email,
                'phone_number': user.phone_number,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'is_verified': user.is_verified,
                'image_url': user.image_url
            } for user in users]

            print("user_details->>>", user_data)
            response_data = format_api_response(success=True, data=user_data, message='user details retrieved successfully',)
            return JsonResponse(response_data)
        else:
            response_data = format_api_response(success=False,  message='user is not authorized',)
            return JsonResponse(response_data)
    except Exception as e:
        response_data = format_api_response(success=False, message='an error occurred while retrieving user details', error=str(e))
        return JsonResponse(response_data, status=500)





  






    





    

    
