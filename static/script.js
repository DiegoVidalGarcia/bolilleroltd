document.getElementById("bolilleroForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Evita que la página se recargue

    let desde = parseInt(document.getElementById("desde").value);
    let hasta = parseInt(document.getElementById("hasta").value);

    if (desde >= hasta) {
        alert("El valor 'Desde' debe ser menor que 'Hasta'");
        return;
    }

    let numeroSorteado = Math.floor(Math.random() * (hasta - desde + 1)) + desde;
    
    document.getElementById("numeroSorteado").textContent = numeroSorteado;
    document.getElementById("resultado").classList.remove("d-none");
});
