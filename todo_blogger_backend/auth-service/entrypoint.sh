set -e

if [ "$FLASK_ENV" = "production" ]; then
  echo "Running auth-service in production mode with Gunicorn"
  exec gunicorn app:app --bind 0.0.0.0:5000 --workers 3
else
  echo "Running auth-service in development mode with Flask"
  exec python app.py
fi
