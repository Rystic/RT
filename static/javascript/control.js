var previousCharacer = 0;
var totalKeyValue = 0;
			
var keyValues = new Map();
keyValues.set("w", 1);
keyValues.set("a", 10);
keyValues.set("s", 100);
keyValues.set("d", 1000);
			
var keysPressed = new Map();
keysPressed.set("w", false);
keysPressed.set("s", false);
keysPressed.set("a", false);
keysPressed.set("d", false);

var robot_name = document.getElementById("target").getAttribute("robot_name");
			
$( "#target" ).keypress(function( event) 
{
	//console.log("now pressing " + String.fromCharCode(event.which) + "(" + event.which+")");
	sendKey(event.which, true);
});
			
$( "#target" ).keyup(function() 
{
   	//console.log("now releasing " + String.fromCharCode(event.which) + "(" + event.which+")");
	sendKey(event.which, false);
});

function updateMsg()
{
 	console.log("running command");
  	$.ajax(
	{
	    url: "/pollactiverobots",
		type: "get",
		data:{name:robot_name},
	});
	setTimeout('updateMsg()', 4000);
}
updateMsg();
			
function sendKey(numCode, pressed)
{
 	$('input[type=text], textarea').val('');

    var charCode = String.fromCharCode(numCode).toLowerCase();
    var value = keyValues.get(charCode);
    if (value == undefined)
        return;
    
    if (pressed)
    {
    	if (keysPressed.get(charCode) == true) 
    		return;
    	keysPressed.set(charCode, true);
    }
    else
    {
    	keysPressed.set(charCode, false);
    	value *= -1;
    }
    					
    totalKeyValue += value;
    				
    var instructionString;
    if (totalKeyValue == 0)
    	instructionString = '0000'; 
    else if (totalKeyValue < 10 && totalKeyValue > 0)
    	instructionString = '0001';
    else if (totalKeyValue < 100)
    	instructionString = '00' + totalKeyValue;
    else if (totalKeyValue < 1000)
    	instructionString = '0' + totalKeyValue;
    else if (totalKeyValue >= 1000)
    	instructionString = totalKeyValue;
    console.log(instructionString)
    $.ajax(
    {
        url: "/instruction",
        type: "post",
        data:{value:instructionString, name:robot_name},
    });
}