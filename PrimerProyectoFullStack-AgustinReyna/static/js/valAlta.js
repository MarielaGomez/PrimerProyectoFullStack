var user = document.getElementById("name"); //comprueba si existe y lo almacena en variable
var pass1 = document.getElementById("password");
var pass2 = document.getElementById("pass2");
var error = document.getElementById("error");
var email = document.getElementById("email");
//error.style.color = "red";
var formLog = document.getElementById("formLogin");

	
	function validacion() {
	var mensajesError = [];
		

		//expr = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
		
		var mensajesError = [];

		if (user.value === null || user.value === ""){ //Analizar variable nombre		
			mensajesError.push("Ingresa un usuario");
			error.innerHTML = mensajesError.join(", ");
			return false;
		} else if ( user.value.length <= 3 ) {
			mensajesError.push("El usuario tiene que tener al menos 4 digitos.");
			error.innerHTML = mensajesError.join(", ");
			return false;
		}else if (email.value === null || email.value === ""){ //Analizar variable nombre		
			mensajesError.push("ingresa un correo");
			error.innerHTML = mensajesError.join(", ");
			return false;
		}else if (pass1.value === null || pass1.value === ""){ //Analizar variable nombre
			mensajesError.push("Ingresa una contraseña");
			error.innerHTML = mensajesError.join(", ");
				return false;
			} else if (pass1.value.length <= 7) {
				mensajesError.push("La contraseña debe tener al menos 8 caracteres");
				error.innerHTML = mensajesError.join(", ");
					return false;
		}else if (pass1.value == pass2.value){				
					return true;			
		}else {
			mensajesError.push("Las contraseñas no son iguales");
			error.innerHTML = mensajesError.join(", ");
			
			return false;
		}
	
		
		
};

