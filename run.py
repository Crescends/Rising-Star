import RisingStar
from setup import setup_datbase
setup_datbase()

app = RisingStar.create_website() 
if __name__ == '__main__':
    app.run(port=5000, debug=True)