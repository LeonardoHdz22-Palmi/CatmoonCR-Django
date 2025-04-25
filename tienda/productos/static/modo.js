document.addEventListener("DOMContentLoaded", function () {
    let botonModo = document.getElementById("modo-toggle");
    let body = document.body;
    let footer = document.querySelector("footer"); // Asegurar que el footer también cambia

    if (!body.classList.contains("modo-claro") && !body.classList.contains("modo-oscuro")) {
        body.classList.add("modo-claro");
    }

    botonModo.addEventListener("click", function () {
        if (body.classList.contains("modo-claro")) {
            body.classList.remove("modo-claro");
            body.classList.add("modo-oscuro");
            botonModo.textContent = "Modo Claro ☀️";
        } else {
            body.classList.remove("modo-oscuro");
            body.classList.add("modo-claro");
            botonModo.textContent = "Modo Oscuro 🌙";
        }
    });
});
