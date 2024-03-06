from api import models
from api import end_user_serializers
import random
import string
import yagmail


def id_generate():
    id = str("".join(random.choices(string.ascii_uppercase+string.digits,k=11)))
    return id

def otp_generate():
    return int(random.randrange(1000,9999))

def validate_email(id):
    valid_data = models.End_Usermodel.objects.all()
    valid_email = end_user_serializers.EnduserSerializer(valid_data,many=True)
    data = False
    for i in valid_email.data:
        if id==i['email']:
            data = True
            break
    print("hii")
    return data
    
def validate_otp(id, otp):
    UserData = models.End_Usermodel.objects.get(uid = id)
    data = end_user_serializers.EnduserSerializer(UserData)
    valid = False
    if data.data['otp'] == otp:
        valid = True
    return valid

def verify_user(email, password):
    Data = models.End_Usermodel.objects.get(email = email)
    data = end_user_serializers.EnduserSerializer(Data)
    authentication = False
    if data.data['email'] == email and data.data['password'] == password:
        authentication = True
    print("hii")
    return authentication


def verify_user_otp(email):
    Data = models.End_Usermodel.objects.get(email = email)
    data = end_user_serializers.EnduserSerializer(Data)
    authentication = False
    if data.data['otp'] == data.data['user_otp']:
        authentication = True
    return authentication

def send_mail(receiver_email, otp):
    sender = 'abijithmailforjob@gmail.com'
    password = 'kgqzxinytwbspurf'
    subject = "Miogra Sign Up OTP"
    content = f"""
    OTP : {otp}
    """
    yagmail.SMTP(sender, password).send(
        to=receiver_email,
        subject=subject,
        contents=content
    )

def get_user_id(email):
    Data = models.End_Usermodel.objects.get(email = email)
    data = end_user_serializers.EnduserSerializer(Data)
    print(data.data["uid"])
    return data.data['uid']