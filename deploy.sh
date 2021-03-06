echo 'Running npm install & npm build'
npm set progress=false && npm install -s --no-progress && npm run build
echo 'Done...'

echo 'Format index.html as Jinja template'
python format_index_html.py
echo 'Done...'

echo 'Install python modules'
pip install -r requirements.txt
echo 'Done...'

echo 'Collect static'
python manage.py collectstatic --noinput
echo 'Done...'

if [ "$1" == "update" ]; then
  echo 'Updating to AWS '
  zappa update production
else
  echo 'Deploying to AWS '
  zappa deploy production
fi
