function init() 
{
	var config = {
		apiKey: "AIzaSyCqRx270zo8stz3pIaAGGeoUaD9Jtn41UI",
		authDomain: "synced-3c7d7.firebaseapp.com",
		databaseURL: "https://synced-3c7d7.firebaseio.com",
		projectId: "synced-3c7d7",
		storageBucket: "synced-3c7d7.appspot.com"
	};

	firebase.initializeApp(config);
	var key = getKey();
	var firepadRef = getReferenceFromString(key);

	var container = document.getElementById('firepad-container');
	var codeMirror = CodeMirror(container, { lineWrapping: true });

	var firePadParams = { richTextToolbar: false, richTextShortcuts: false };
	var firePad = Firepad.fromCodeMirror(firepadRef, codeMirror, firePadParams);

	// Set up the contents of the pad once it's loaded

	firePad.on('ready', function() {
		if (firePad.isHistoryEmpty()) {
			firePad.setHtml("This is now an empty pad!");
		}
	});
}

function getKey()
{
	var withSlash = window.location.pathname;
	var key = withSlash.replace('/', '');
	return key;
}

function getReferenceFromString(str)
{
	var parentRef = firebase.database().ref();
	var childRef = parentRef.child(str);
	console.log('Firebase data: ', childRef.toString());
	return childRef;
}





