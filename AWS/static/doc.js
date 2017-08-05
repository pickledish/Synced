function sendText() {
	$.ajax({
		url: '/store',
		type: 'POST',
		dataType: 'json',
		data: {name: $('#siteRoom').attr("room"), text: $("#inputBox").val()},
		success: function(html) { console.log("recorded"); }
	});
}

var TogetherJSConfig_toolName = "My Site";
var TogetherJSConfig_autoStart = true;
var TogetherJSConfig_suppressJoinConfirmation = true;
var TogetherJSConfig_disableWebRTC = true;
var TogetherJSConfig_youtube = false;
var TogetherJSConfig_dontShowClicks = true;
var TogetherJSConfig_findRoom = $('#siteRoom').attr("room");
// var TogetherJSConfig_includeHashInUrl = true;

var TogetherJSConfig_on_ready = function () { 

	$(".togetherjs-cursor").hide();
	$("document").on("pagehide", sendText);
	window.onbeforeunload = sendText;

	$.ajax({
		url: '/retrieve',
		type: 'POST',
		dataType: 'html',
		data: {name: $('#siteRoom').attr("room")},
		success: function(html) { $('#inputBox').text(html) }
	});
};