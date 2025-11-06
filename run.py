# /run.py

from dashboard import create_app

app = create_app()

if __name__ == '__main__':
    # Using port 5001 as specified in the original app.py
    app.run(debug=True, host='0.0.0.0', port=5001)