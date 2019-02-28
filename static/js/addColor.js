// add color to the classes
function addColor(className, string, color) {
	var startCell = timeSplit(string)[0];
	var numOfCells = timeSplit(string)[1];
	var day = timeSplit(string)[2]
	for(var i = 0; i < numOfCells; i ++) {
		if(!(document.getElementById(day + 'T').getElementsByTagName('td')[i + startCell].style.backgroundColor)){
			document.getElementById(day + 'T').getElementsByTagName('td')[i + startCell].style.backgroundColor = color;
		} else {
			document.getElementById(day + 'T').getElementsByTagName('td')[i + startCell].style.backgroundColor = "red";
		}

	}
	var element = document.getElementById(day + 'T').getElementsByTagName('td')[startCell];
	var position = element.getBoundingClientRect();
	var x = position.left;
	var y = position.top;
	var body1 = document.getElementsByTagName("BODY")[0];
	var div1 = document.createElement('div');
	var text1 = document.createTextNode(className);
	var day = string.substring(0, 3);
	var hourS = string.substring(3, 5);
	var minS = string.substring(5, 7);
	var hourE = string.substring(8, 10);
	var minE = string.substring(10, 12);
	string = day + " " + hourS + ":" + minS + "-" + hourE + ":" + minE;
	var text2 = document.createTextNode(string);


	div1.style.position = 'absolute';

	div1.appendChild(text1);
	var br=document.createElement("BR");
	div1.appendChild(br);
	div1.appendChild(text2);
	body1.appendChild(div1);
	div1.style.left = x + "px";
	div1.style.top = y + "px";


}