start_postgres

Crear ambiente virtual
pip install --upgrade distro-info
pip3 install --upgrade pip==23.2.1
pip install virtualenv
virtualenv djangoenv
source djangoenv/bin/activate
pip install Django psycopg2-binary

python3 manage.py makemigrations crud
python3 manage.py makemigrations related_objects

Esto nos debe dejar ver que se crearon las tablas que necesitamos. 

python3 manage.py migrate 

Con esto podemos ejecutar las migraciones. Con lo siguiente el Crud debería crearse OK

Operations to perform:
  Apply all migrations: crud
Running migrations:
  Applying crud.0001_initial... OK





  
