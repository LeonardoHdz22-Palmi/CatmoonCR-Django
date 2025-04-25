document.addEventListener("DOMContentLoaded", function() {
    console.log("El script de valoración se ejecutó correctamente.");
    setTimeout(mostrarValoracion, 5000);
});

function mostrarValoracion() {
    let valoracion = document.getElementById("valoracion");
    if (valoracion) {
        console.log("Se encontró el elemento y se muestra.");
        valoracion.style.display = "block";
    } else {
        console.error("No se encontró el elemento de valoración");
    }
}
