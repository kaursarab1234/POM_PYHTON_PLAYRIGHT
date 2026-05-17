import os

from dotenv import load_dotenv


def test_passingDataFromCommandLine():
    #import sys
    username=os.getenv("USERNAME")
    password=os.getenv("PASSWORD")
    print("Username is: ", username)

def test_passingDataFromEnv():  
    load_dotenv(os.getenv("envpathgit")) 
    username=os.getenv("USERNAME")
    password=os.getenv("PASSWORD")
    print("Username is: ", username)
    print("Password is: ", password)