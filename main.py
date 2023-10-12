# file to run the app
from myproject import app  # importing the app, myproject looks at __init__ file if not specified other file

if __name__ == "__main__":
    app.run(debug=True)  # debug mode, to run application when main file it is running
