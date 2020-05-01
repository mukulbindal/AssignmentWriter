function getimage(event)
		{
			if(!(event==null || event.keyCode==13 || event.keyCode==190))return;
			$text = document.getElementById("text").value;
			$fontwidth = document.getElementById("font-width").value;
			$fontheight = document.getElementById("font-height").value;
			$tableft = document.getElementById("tab-left").value;
			$tabright = document.getElementById("tab-right").value;
			$fontsize = document.getElementById("font-size").value;
			$fontcolor = document.getElementById("font-color").value;
			$.get('/write/',
				{
				string:$text,
				fontwidth: $fontwidth,
				fontheight: $fontheight,
				tableft: $tableft,
				tabright:$tabright,
				fontsize:$fontsize,
				fontcolor:$fontcolor
				},
				function(data)
				{
var img = document.getElementById("op");
img.src = 'data:image/jpeg;base64,' + data;
				}
			);
		}
