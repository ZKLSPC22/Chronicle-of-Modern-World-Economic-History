document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById("modal");
    const modalTitle = document.getElementById("modal-title");
    const modalMessage = document.getElementById("modal-message");
    const modalInfo = document.getElementById("modal-info");
    const closeBtn = document.querySelector(".close");

    // Cell click handler
    document.querySelectorAll('.cell').forEach(cell => {
        cell.addEventListener('click', () => {
            const key = cell.getAttribute('data-key');
            const message = cell.getAttribute('data-message');
            
            // Display the message in the modal
            document.getElementById('modal-title').innerHTML = key;
            document.getElementById('modal-message').innerHTML = message;
            
            // Show the modal
            document.getElementById('modal').style.display = 'block';
        });
    });

    // Close handlers
    closeBtn.addEventListener('click', () => {
        modal.style.display = 'none';
    });

    window.addEventListener('click', (event) => {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });

    // Escape key handler
    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && modal.style.display === 'flex') {
            modal.style.display = 'none';
        }
    });
});
