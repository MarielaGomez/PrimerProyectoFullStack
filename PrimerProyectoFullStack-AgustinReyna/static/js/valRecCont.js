var email = document.getElementById("email");
var error = document.getElementById("error");
var formLog = document.getElementById("formRecupera");

formLog.addEventListener("submit", function(evento){ //recibe dos parametros 1- evento a ejecutar 2 - funcion, la cual recibe un parametro 
	evento.preventDefault();  //previene que el formulario se envie por defecto

	expr = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;

	var mensajesError = [];

	if (email.value === null || email.value === ""){ //Analizar variable nombre
		mensajesError.push("Ingresa un correo");
	} else if ( !expr.test(email.value) ) {
		mensajesError.push("La dirección de correo no parece valida.");
	}

    error.innerHTML = mensajesError.join(", ");
});