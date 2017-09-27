console.log("motor.js");

function requestMotorControll(message){
	const request =  new XMLHttpRequest();
	request.open("GET", "http://localhost:5000/" + message);

	request.addEventListener("load", (event) => {
		console.log(event.target.status);
		console.log(event.target.responseText);
	});

	request.send();
}

//DOMの解析が全部終わってからじゃないと、要素が取得できないことがあるんだねぇ
document.addEventListener("DOMContentLoaded", function(event) {
	console.log("DOM fully loaded and parsed");

	    
    var leftToggle =  document.querySelector("#left-toggle");
	leftToggle.addEventListener("click", function( event ){
		//console.log("left toggle");
		requestMotorControll("start");

	});
	
	var rightToggle =  document.querySelector("#right-toggle");
	rightToggle.addEventListener("click", function( event ){
		//console.log("right toggle");
		requestMotorControll("stop");
	});
	
});