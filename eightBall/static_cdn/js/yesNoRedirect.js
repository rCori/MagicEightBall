function myFunctionYes() {
    window.location = "{% url 'submit' queryRow.id 'yes' %}";
	//Visual effects I will need to do
}

function myFunctionNo() {
    window.location = "{% url 'submit' queryRow.id 'no' %}";
	//Visual effects I will need to do
}