var user = document.getElementById("username");
var pass1 = document.getElementById("pass1");
var error = document.getElementById("error");

var formLog = document.getElementById("formLogin");

	
	function validacion() {
	var mensajesError = [];

	if (user.value === null || user.value === ""){ //Analizar variable nombre		
		mensajesError.push("Ingresa un usuario");
		error.innerHTML = mensajesError.join(", ");
		return false;
	} else if ( user.value.length <= 3 ) {
		mensajesError.push("El usuario tiene que tener al menos 4 digitos.");
		error.innerHTML = mensajesError.join(", ");
		return false;
	}else if (pass1.value === null || pass1.value === ""){ //Analizar variable nombre
		mensajesError.push("Ingresa una contraseña");
		error.innerHTML = mensajesError.join(", ");
			return false;
		} else if (pass1.value.length <= 2) {
			mensajesError.push("La contraseña debe tener al menos 8 caracteres");
			error.innerHTML = mensajesError.join(", ");
				return false;
	}else {
		return true;
	}



    

};