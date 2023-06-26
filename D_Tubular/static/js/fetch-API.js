const API_URL = "http://127.0.0.1:8000/appdeustutub/APIarchivos/"

fetch(API_URL)
    .then(response => response.json())
    .then( json => {
        addRows(json);
    });

function addRows(equipos) {
    tbody = document.getElementById("tbody");
    equipos.forEach(element => {
        tbody.appendChild(createEquipoRow(element))
    });
}

function createEquipoRow(equipo){
    let row = document.createElement("tr")

    let modelo = document.createElement("td")
        modelo.textContent = equipo.modelo;
        row.appendChild(modelo);

    let marca = document.createElement("td");
        marca.textContent = equipo.marca;
        row.appendChild(marca);
    
    let fecha_instalacion = document.createElement("td")
        fecha_instalacion.textContent = equipo.fecha_instalacion;
        row.appendChild(fecha_instalacion);
    
    let fecha_adquisicion = document.createElement("td")
        fecha_adquisicion.textContent = equipo.fecha_adquisicion;
        row.appendChild(fecha_adquisicion);
    
    let link_row = document.createElement("td")
    let link_list = document.createElement("li")

    let link_detail = document.createElement("a")
        // añadir enlace 
        link_detail.setAttribute('href', "http://127.0.0.1:8000/appdeustutub/equipos/"+equipo.id);
        // añadir texto 
        link_detail.innerHTML = "Detalles";

        link_list.append(link_detail);
        link_row.append(link_list);
        row.appendChild(link_row);

    return row;
}