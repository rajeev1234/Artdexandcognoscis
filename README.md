# Artdexandcognoscis



Create a virtual environment, python 3.6+.

Install dependencies mentioned in requirements.txt file

To check if its working run : => python manage.py runserver

To apply in-built migrations: => python manage.py migrate

Your code goes in the makerChecker directory



API are:

Description : User Creation
URL : /api/users/
Method : GET/ POST/
Request params : as per the model structure(need to pass username , password for compulsion plus there are more two params 
is_maker => Its a boolean , make it true while signup if you are maker
is_checker => Its a boolean, make it true while signup if you are checker
)


URL : api-token-auth/
Method: POST
description : for generating token


URL : api-token-verify/
Method: POST
description : for verifying token


URL : api-token-refresh/
Method: POST
description : for refreshing token


URL : /make or /make/<pk>
Method : GET/ POST/ PATCH
Headers: Authorization JWt<token>
Request params : as per the model structure
  
  
URL : /model or /model/<pk>
Method : GET/ POST/ PATCH
Headers: Authorization JWt<token>
Request params : as per the model structure
  
URL : /variant or /variant/<pk>
Method : GET/ POST/ PATCH
Headers: Authorization JWt<token>
Request params : as per the model structure
  
  
URL : /allDetails 
Method : GET
Headers: Authorization JWt<token>
Request params : collect all the data at once



  
