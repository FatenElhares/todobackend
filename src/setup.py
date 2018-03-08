from setuptools import setup, find_packages

setup (
  name = "todobackend",
  version = "0.1.0",
  description ="Todobackend Django Rest service",
  packages= find_packages(),
  include_package_data = True,
  scripts = ["manage.py"],
  install_requires= ["Django==1.11.10",
                     "django-cors-headers==2.1.0",
                     "djangorestframework==3.7.7",
                     "ez-setup==0.9",
                     "MySQL-python==1.2.5",
                     "numpy==1.14.1",
                     "pystan==2.17.1.0",
                      "pytz==2018.3",
                      "uwsgi>=2.0"],

  extras_require = {
  						"test":[

  							"colorama==0.3.9",
							"coverage==4.5.1",
							"Cython==0.27.3",
							"django-nose==1.4.5",
							"ez-setup==0.9",
							"MySQL-python==1.2.5",
							"nose==1.3.7",
							"numpy==1.14.1",
							"pinocchio==0.4.2",
							"pystan==2.17.1.0",
							"pytz==2018.3"]

  					} 
)