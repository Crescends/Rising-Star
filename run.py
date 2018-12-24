from RisingStar import app

application = app.app

if __name__ == '__main__':
    application.run(port=5000, debug=True)