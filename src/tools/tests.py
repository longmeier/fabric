from django.test import TestCase

# Create your tests here.
import os


a = os.system('tar zxvf /home/data/code/bolin_uat/app/dist.tar ')
print(a)