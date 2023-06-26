document.getElementById('formulario').addEventListener('submit', function(event) {
    event.preventDefault();  // Evita que se envíe el formulario

    // Obtén el valor del campo DNI
    var dniInput = document.getElementById('id_dni');
    var dniValue = dniInput.value.trim();

    // Validar formato de DNI
    var dniRegex = /^\d{8}[a-zA-Z]$/;
    if (!dniRegex.test(dniValue)) {
        dniInput.style.borderColor = 'red';
    } else {
        dniInput.style.borderColor = '';  // Restablece el color del borde si es válido
    }

    // Obtén el valor del campo email
    var emailInput = document.getElementById('id_email');
    var emailValue = emailInput.value.trim();

    // Validar formato de email
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(emailValue) || !emailValue.toLowerCase().endsWith("@appdeustutub.com")) {
        emailInput.style.borderColor = 'red';
    } else {
        emailInput.style.borderColor = '';  // Restablece el color del borde si es válido
    }

    // Verificar si alguno de los campos es inválido
    if (dniInput.style.borderColor === 'red' || emailInput.style.borderColor === 'red') {
        return;
    }

    // Si la validación fue exitosa, envía el formulario
    this.submit();
});
