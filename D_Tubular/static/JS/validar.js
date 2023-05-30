// verificar_correo.js

function verificarCorreo(correo) {
	var dominio = "@opendeusto.com";
	var posicion = correo.indexOf(dominio);

	if (posicion !== -1 && posicion === correo.length - dominio.length) {
		return true;

	}
	else {
		var mensaje = "ERES UN MIERDAS";
		return (false + mensaje);

	}


}
