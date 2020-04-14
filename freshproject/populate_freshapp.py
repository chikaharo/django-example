import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freshproject.settings')

import django
django.setup()

import random
from freshapp.models import *
from faker import Faker

fakegen = Faker()

def populate(N=10):
    for entry in range(N):
        fakename = fakegen.name().split()
        fakefirst = fakename[0]
        fakelast = fakename[1]
        fakemail = fakegen.email()

        nuser = User.objects.get_or_create(first_name=fakefirst, last_name=fakelast, email=fakemail)[0]


if __name__ == "__main__":
    print("Populating")
    populate(50)
    print('COMPLETE!')