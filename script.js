document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('contact-form');
    const submitButton = document.getElementById('submit-btn');

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        submitButton.classList.add('enviar-animacion');

        setTimeout(function () {
            submitButton.classList.remove('enviar-animacion');
            obtenerPrecio(); // Llama a la función para obtener el precio cuando se envía el formulario
        }, 500);
    });
});
document.addEventListener('DOMContentLoaded', function () {
    // Tu código JavaScript aquí
    const precioInput = document.getElementById('precio');
    const resInput = document.getElementById('resultado');

    async function obtenerPrecio() {
        const precio = precioInput.value;
        const response = await fetch(`http://127.0.0.1:8000/${precio}`);
        const data = await response.json();
        resInput.value = data.resultado;
    }

    const button = document.getElementById('submit-btn');
    button.addEventListener('click', obtenerPrecio);
});
