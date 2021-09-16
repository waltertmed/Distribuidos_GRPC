set "curpath=%cd%"

start firefox.exe http://localhost:5000/

cd ../

set FLASK_APP=client.py

python client.py

flask run

pause