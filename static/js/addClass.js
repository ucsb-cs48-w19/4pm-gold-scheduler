function addClass() {

            var sub = document.getElementById("subject").value;
            var classValue = document.getElementById("class1").value;
            var lecValue = document.getElementById("teacherLecTime").value;
            var sectionValue = document.getElementById("section").value;

            var finalData = classValue + "*" + lecValue + "*" + sectionValue;

		    var data = finalSplite();
		    if(data == "") {
		        alert("Please choose a course! Or go home!");
            } else {
		        var className = data[0];
		        for(var i = 1; i < data.length; i ++) {
		        addColor(data[0], data[i], color[colorIndex]);
            }
            }
		    colorIndex++;
		    classArr.push(finalData);

		    var arr1 = classArr;


		    var classOn = document.getElementById("classOn");


			    var options1 = classOn.getElementsByTagName("option");
			for(var m = 0; m<options1.length; m++)
			{
				var op = options1[m];
				classOn.removeChild(op);
				m--;
			}

			    for(var j = 0; j<arr1.length; j++)
					{
						var value1 = arr1[j];
						var option1 = document.createElement("option");
						var text1 = document.createTextNode(value1);
						option1.appendChild(text1);
						classOn.appendChild(option1);
					}
        }