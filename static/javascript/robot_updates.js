function updateMsg()
{
  	$.ajax(
	{
	    url: "/pollactiverobots",
		type: "post",
		success: function(html)
		{
		    $("#content").html(html);
		}
	});
	setTimeout('updateMsg()', 4000);
}
updateMsg();