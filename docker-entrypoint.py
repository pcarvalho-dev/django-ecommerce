from subprocess import call

# PRINT VARIABLES ENVIRONMENT
import os

# RUN APP
if __name__ == "__main__":
    call(["python", "manage.py", "runserver", "0.0.0.0:8000"])
