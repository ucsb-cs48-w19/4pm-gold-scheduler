function addSubject() {
			var subject1 = document.getElementById("subject");
			for(var j = 0; j<subjectArr.length; j++)
					{
						var value1 = subjectArr[j];
						var option1 = document.createElement("option");
						var text1 = document.createTextNode(value1);
						option1.appendChild(text1);
						subject1.appendChild(option1);
					}
		}