import RisingStar

website = RisingStar.create_website() 

if __name__ == '__main__':
    website.run(port=5000, debug=True)