#!/bin/bash
################################################################################
# Install PostgreSQL and PostGIS for the Application Internal Database System  #
################################################################################

#sudo echo "deb http://apt.postgresql.org/pub/repos/apt xenial-pgdg main" >> /etc/apt/sources.list
#sudo wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | sudo apt-key add -
#sudo apt-get update
#sudo apt-get install postgresql-11
#sudo apt-get install postgresql-11-postgis-2.5
#sudo apt-get install postgresql-11-postgis-scripts
#sudo apt-get install postgis
#sudo apt-get install postgresql-11-pgrouting
#sudo service postgresql stop
#sudo service postgresql start

################################################################################
# Install pip3 for python package management using python3                     #
################################################################################

#sudo apt-get install python3-pip
#pip3 install pip --upgrade

################################################################################
# Install django dependency for webapp project structure                       #
################################################################################

pip install django

################################################################################
# Install django-rest-framework dependency for webapp web services project     #
# structure using REST architecture principles                                 #
################################################################################

pip install djangorestframework
pip install markdown         # Markdown support for the browsable API.
pip install django-filter    # Filtering support
pip install django-guardian  # An implementation of per object permissions
pip install Pygments         # Add syntax highlighting to Markdown processing
pip install coreapi          # Schema generation support

################################################################################
# Install django-oauth-toolkit dependency for webapp oauth2 capabilities and   #
# endpoints                                                                    #
################################################################################

pip install django-oauth-toolkit    # Webapp oauth2 capabilities and endpoints                       
pip install -e git+https://github.com/cedadev/dot-restrict-scopes.git@master#egg=dot_restrict_scopes 
                                    # Rrestricting oauth2 capabilities based on application scopes (not enabled by default)   
pip install drfdocs                 # Web services documentation
pip install drf-yasg                # Web services documentation
pip install coverage                # Indicators of unit tests run for the web services
pip install django-cors-headers     # CORS project configuration  

################################################################################
# Install to use custom parser and renderer                                    #
################################################################################

pip install djangorestframework-yaml    # See: https://github.com/jpadilla/django-rest-framework-yaml/  
pip install djangorestframework-xml     # See: https://github.com/jpadilla/django-rest-framework-xml/  
pip install drf-renderer-xlsx           # Custom XLSX
pip install djangorestframework-csv     # Custom CSV


################################################################################
# Install to use custom logging                                                #
################################################################################

pip install django-request-logging

################################################################################
# Install to connect databases                                                 #
################################################################################

#pip install SQLAlchemy
pip install psycopg2

################################################################################
# Install to use a data analytics                                              #
################################################################################

#pip install pandas
#pip install numpy
#pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

################################################################################
# Install to use the AWS SDK for Python (Boto3)                                 #
################################################################################

#pip install boto3

################################################################################
# Install to visualize the dependencies of the project                         #
################################################################################

pip install pipdeptree      # Visualize as a tree
pip check                   # Check for broken requirements or packages
pip list                    # List installed packages
pip list --outdated         # Check for outdated packages 
pip list --not-required     # Check for not required packages (packages that are not dependencies of installed packages)

################################################################################
# Create a package list file containing currently installed versions of each   #
# dependency python library                                                    #
################################################################################

pip freeze
pip freeze > requirements.txt

pipdeptree
pipdeptree > requirements_tree.txt
