import RisingStar
import setup import setupDatase
setupDatase()
app = RisingStar.create_website() 
if __name__ == '__main__':
    app.run(port=5000, debug=True)