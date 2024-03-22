document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('contact-form');
    const submitButton = document.getElementById('submit-btn');
    const precioInput = document.getElementById('precio');
    const resInput = document.getElementById('resultado');

    form.addEventListener('submit', async function (event) {
        event.preventDefault();

        submitButton.classList.add('enviar-animacion');

        setTimeout(async function () {
            submitButton.classList.remove('enviar-animacion');
            await obtenerPrecio(); // Llama a la función para obtener el precio cuando se envía el formulario
        }, 500);
    });

    // Define la función obtenerPrecio dentro del evento DOMContentLoaded
    async function obtenerPrecio() {
        const precio = precioInput.value;
        try {
            const response = await fetch('http://127.0.0.1:8000/calcular', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ precio: parseFloat(precio) })
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            resInput.value = data.resultado;
        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
        }
    }
});
