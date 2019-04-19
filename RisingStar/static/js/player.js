class Cover {
    // returns click as decimal (.77) of the total timelineWidth
    clickPercent(event) {
        return (event.clientX - getPosition(this.timeline)) / this.timelineWidth;
    }

    // this.mouseDown EventListener
    mouseDown() {
        this.onplayhead = true;
        window.addEventListener('mousemove', this.moveplayhead, true);
        this.music.removeEventListener('timeupdate', this.timeUpdate, false);
    }

    // this.mouseUp EventListener
    // getting input from all mouse clicks
    mouseUp(event) {
        if (this.onplayhead == true) {
            this.moveplayhead(event);
            window.removeEventListener('mousemove', this.moveplayhead, true);
            // change current time
            this.music.currentTime = this.duration * this.clickPercent(event);
            this.music.addEventListener('timeupdate', this.timeUpdate, false);
        }
        this.onplayhead = false;
    }
    // mousemove EventListener
    // Moves this.playhead as user drags
    moveplayhead(event) {
        var newMargLeft = event.clientX - getPosition(this.timeline);

        if (newMargLeft >= 0 && newMargLeft <= this.timelineWidth) {
            this.playhead.style.marginLeft = newMargLeft + "px";
        }
        if (newMargLeft < 0) {
            this.playhead.style.marginLeft = "0px";
        }
        if (newMargLeft > this.timelineWidth) {
            this.playhead.style.marginLeft = this.timelineWidth + "px";
        }
    }

    // this.timeUpdate
    // Synchronizes this.playhead position with current point in audio
    timeUpdate() {
        var playPercent = this.timelineWidth * (this.music.currentTime / this.duration);
        this.playhead.style.marginLeft = playPercent + "px";
        if (this.music.currentTime == this.duration) {
            this.pButton.className = "";
            this.pButton.className = "fas fa-play";
        }
    }

    //Play and Pause
    play() {
        // start this.music
        if (this.music.paused) {
            this.music.play();
            // remove play, add pause
            this.pButton.className = `fas fa-pause pButton ${this.coverName}`;
        } else { // pause this.music
            this.music.pause();
            // remove pause, add play
            this.pButton.className = `fas fa-play pButton ${this.coverName}`;
        }
    }

    // getPosition
    // Returns elements left position relative to top-left of viewport
    getPosition(el) {
        return el.getBoundingClientRect().left;
    }

    constructor(coverName) {
        console.log("creating " + coverName);
        this.coverName = coverName;
        this.music = document.getElementsByClassName(`music ${coverName}`)[0]; // id for audio element
        this.pButton = document.getElementsByClassName(`pButton ${coverName}`)[0]; // play button
        this.playhead = document.getElementsByClassName(`playhead ${coverName}`)[0]; // this.playhead
        this.timeline = document.getElementsByClassName(`timeline ${coverName}`)[0]; // timeline
        this.duration = this.music.duration; // Duration of audio clip, calculated here for embedding purposes

        // timeline width adjusted for this.playhead
        this.timelineWidth = this.timeline.offsetWidth - this.playhead.offsetWidth;

        // play button event listenter
        this.pButton.addEventListener("click", () => {this.play()} );
        // timeupdate event listener
        this.music.addEventListener("timeupdate", () => {this.timeUpdate()}, false);

        // makes timeline clickable
        this.timeline.addEventListener("click",  (event) => {
            this.moveplayhead(event);
            this.music.currentTime = this.duration * this.clickPercent(event);
        }, false);
        // makes this.playhead draggable
        this.playhead.addEventListener('mousedown', () => {this.mouseDown()}, false);
        window.addEventListener('mouseup', () => {this.mouseUp()}, false);

        // Boolean value so that audio position is updated only when the this.playhead is released
        this.onplayhead = false;
        // Gets audio file this.duration
        this.music.addEventListener("canplaythrough", () => {
            this.duration = this.music.duration;
        }, false);
    }

}


var covers = []
console.log('hello0');
var Smoke = new Cover("Smoke");
var Growth = new Cover("Growth");
var Abstract = new Cover("Abstract");