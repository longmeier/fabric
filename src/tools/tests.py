from django.test import TestCase

# Create your tests here.
import os

ls = os.system('ls')
if os.path.exists('migrations'):
    print(1)
else:
    print(2)