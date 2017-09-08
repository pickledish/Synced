# Trashpad

<hr>

### Tools Used

* [Materialize](http://materializecss.com/), for the frontend framework
* [Flask](http://flask.pocoo.org/), as always, for the backend framework
* [FirePad](https://github.com/firebase/firepad), for the collaborative text editing, which was built with:
* [FireBase](https://firebase.google.com/), for storing data in a backend accessible to all users
* [OT.js](https://github.com/Operational-Transformation/ot.js/), for the real work of operational transformations
* [CodeMirror](https://codemirror.net/), for an extensible and Firepad-friendly text editor
* [Redis](), via the RedisToGo Heroku extension, for persistence across servers

<hr>

### Currently To-Do:

* ~~Make it more responsive (for phones)~~ Was missing viewport header
* ~~Get "copy link" working they way it should~~ All done
* ~~Remove the random `favicon.ico` error?~~ Make this better eventually
* ~~Why does it sometimes display "key not found"?~~ Persistence, used Redis
* ~~Figure out why it takes 10x as long to load on mobile-sized browsers??~~
	* ~~It's literally just the iOS user agent???~~ Forced it to be Mozilla, feels gross
* ~~Move over from 6 words to like 10,000~~ Used a set of words from Google
* ~~Get a better favicon~~ Made it myself
* ~~Update the text to not be condescending~~ All set
* ~~Move from Redis to Postgres because why redis ever~~ done
* Add better error handling
* Make the user choose how long it lasts
* (Future) enable a spreadsheet mode
* (Future) add a poll mode?