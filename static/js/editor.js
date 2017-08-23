function init() 
{

	// Clear the user agent. Necessary to fix iOS 10-second load bug, whaatttt
	setUserAgent(window, 'Mozilla/5.0 (compatible)');

	var config = {
		apiKey: "AIzaSyCqRx270zo8stz3pIaAGGeoUaD9Jtn41UI",
		authDomain: "synced-3c7d7.firebaseapp.com",
		databaseURL: "https://synced-3c7d7.firebaseio.com",
		projectId: "synced-3c7d7",
		storageBucket: "synced-3c7d7.appspot.com"
	};

	firebase.initializeApp(config);
	var firepadRef = getReferenceFromString(key);

	var container = document.getElementById('firepad-container');
	var codeMirror = CodeMirror(container, { lineWrapping: true });

	var firePadParams = { richTextToolbar: false, richTextShortcuts: false };
	var firePad = Firepad.fromCodeMirror(firepadRef, codeMirror, firePadParams);
	console.log("after load")

	// Set up the contents of the pad once it's loaded
	firePad.on('ready', function() {
		console.log("is ready")
		if (firePad.isHistoryEmpty()) {
			firePad.setHtml("Write a new note");
		}
	});
}

function setUserAgent(window, userAgent) {
	var userAgentProp = { get: function () { return userAgent; } };
	try {
		Object.defineProperty(window.navigator, 'userAgent', userAgentProp);
	} catch (e) {
		window.navigator = Object.create(navigator, { userAgent: userAgentProp });
	}
}

function getReferenceFromString(str) {
	var parentRef = firebase.database().ref();
	var childRef = parentRef.child(str);
	console.log('Firebase data: ', childRef.toString());
	return childRef;
}



