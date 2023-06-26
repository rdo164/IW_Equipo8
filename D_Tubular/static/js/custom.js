// Obtener todos los elementos de texto en la página
var textElements = document.querySelectorAll('h1, h2, h3, h4, h5, h6, p, div, table, nav, li');

// Función para aumentar el tamaño de los elementos de texto
function aumentarTamanio() {
  for (var i = 0; i < textElements.length; i++) {
    var fontSize = window.getComputedStyle(textElements[i]).fontSize;
    var newSize = parseFloat(fontSize) + 2 + 'px';
    textElements[i].style.fontSize = newSize;
  }
}

// Función para disminuir el tamaño de los elementos de texto
function disminuirTamanio() {
  for (var i = 0; i < textElements.length; i++) {
    var fontSize = window.getComputedStyle(textElements[i]).fontSize;
    var newSize = parseFloat(fontSize) - 2 + 'px';
    textElements[i].style.fontSize = newSize;
  }
}

// Asignar eventos a los botones o enlaces correspondientes
document.getElementById('aumentarBtn').addEventListener('click', aumentarTamanio);
document.getElementById('disminuirBtn').addEventListener('click', disminuirTamanio);