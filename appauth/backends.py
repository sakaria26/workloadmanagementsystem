from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

model = get_user_model()
class StaffBackend(object):

    def authenticate(self, request, staff_number=None, password=None):
        try:
            user = model.objects.get(staff_number=staff_number)
            if user.check_password(password):
                return user
            return None
        except model.DoesNotExist:
            return None
    
    def get_user(self, user_id):
        try:
            return model.objects.get(staff_number=user_id)
        except model.DoesNotExist:
            return None
   