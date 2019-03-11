import RisingStar

app = RisingStar.create_website() 
if __name__ == '__main__':
    app.run(port=5000, debug=True)