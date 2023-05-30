let id = (id) => document.getElementById(id);
let classes = (classes) => document.getElementsByClassName(classes);
let nombreDeUsuario = id("nombre"),
	email = id("email"),

	msjError = classes("error"),
	iconoExito = classes("success-icon"),
	failureIcon = classes("failure-icon");

form.addEventListener("enviar", (e) => {
	e.preventDefault();
	
	motor(nombreDeUsuario, 0, "El nombre de usuario no puede estar en blanco");
	motor(correoElectronico, 1, "El correo electrónico no puede estar en blanco");
	motor(contrasena, 2, "La contraseña no puede estar en blanco");
});
let motor = (id, serial, mensaje) => {
	//			remueve los espacios 
	if (id.value.trim() === "") {
		msjError[serial].innerHTML = mensaje;
		id.li.border = "2px solid red";
	}
	else {
		msjError[serial].innerHTML = "";
		id.style.border = "2px solid green";
	}
}