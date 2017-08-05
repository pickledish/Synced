function init() 
{
	var config = {
		apiKey: "AIzaSyCqRx270zo8stz3pIaAGGeoUaD9Jtn41UI",
		authDomain: "synced-3c7d7.firebaseapp.com",
		databaseURL: "https://synced-3c7d7.firebaseio.com",
		projectId: "synced-3c7d7",
		storageBucket: "synced-3c7d7.appspot.com",
		messagingSenderId: "754507776693"
	};

	firebase.initializeApp(config);
	var firepadRef = getExampleRef();

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

// Helper to get hash from end of URL or generate a random one.
function getExampleRef() {
  var ref = firebase.database().ref();
  var hash = window.location.hash.replace(/#/g, '');
  if (hash) {
	ref = ref.child(hash);
  } else {
	ref = ref.push(); // generate unique location.
	window.location = window.location + '#' + ref.key; // add it as a hash to the URL.
  }
  if (typeof console !== 'undefined') {
	console.log('Firebase data: ', ref.toString());
  }
  return ref;
}



