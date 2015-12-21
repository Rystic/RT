function updateMsg()
{
  	$.ajax(
	{
	    url: "/pollactiverobots",
		type: "post",
		success: function(html)
		{
		    $("#content").html(html);
			console.log("looping1")
		}
	});
	setTimeout('updateMsg()', 4000);
}
console.log("started")
updateMsg();