// Redirect to login page
function redirectToLogin() {
    window.location.href = '/login/'; // Adjust the URL if needed
}

// Smooth scroll to sections
function getStarted() {
    const featuresSection = document.getElementById('features');
    featuresSection.scrollIntoView({ behavior: 'smooth' });
}

// Form validation (optional)
document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.querySelector('.contact form');

    contactForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const name = contactForm.querySelector('input[name="name"]').value;
        const email = contactForm.querySelector('input[name="email"]').value;
        const message = contactForm.querySelector('textarea[name="message"]').value;

        if (name && email && message) {
            alert('Message sent successfully! 🚀');
            contactForm.reset();
        } else {
            alert('Please fill out all fields.');
        }
    });
});
