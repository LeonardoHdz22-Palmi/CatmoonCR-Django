document.addEventListener("DOMContentLoaded", function () {
    const botonModo = document.getElementById("modo-toggle");
    const body = document.body;

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
