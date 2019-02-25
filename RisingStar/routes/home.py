from flask import Blueprint, render_template

home_bp = Blueprint('home_bp', __name__, template_folder='templates', static_url_path='static')

@home_bp.route('/')
@home_bp.route('/home')
def home():
    return render_template('home.html', title="Home")

@home_bp.route('/about')
def about():
    return render_template('about.html', title="About")

@home_bp.route('/music')
def music():
    covers = [
        Song("Smoke From The Ashes","Smoke", "\"Sometimes the hardest thing and the right thing are the same.\" -The Fray \nCampfire debuts with his first album."),
        Song("Growth", "Growth","\"A goal withouut a plan is just a wish.\" - Jeff Rich. \nCampfire shares his story of becoming famous and the fears that arise from populatity and reveals it is a 2 edged sword"),
        Song("Abstract", "Abstract", "To dive into the knowledge that you have within you, you must first understand yourself. \nCampfire dives into his darkest fears and confronts them with the help of his friends")
    ]
    return render_template('music.html', covers=covers, title="Music")


class Song:
    def __init__(self, name, file_name, description):
        self.name = name
        self.front = f"images/music/{file_name}Front.png"
        self.back = f"images/music/{file_name}Back.png"
        self.description = description

