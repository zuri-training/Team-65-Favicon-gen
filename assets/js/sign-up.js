//toggle-password-visibility
const togglePasswords = document.querySelectorAll(".pass_input");
const password = document.querySelector("#password");
const passwordInput = document.querySelector('input[name=password]');
const message = document.querySelector('#signup_message');

togglePasswords.forEach(togglePassword => {
    const password = togglePassword.querySelector("input");
    const toggle_icon = togglePassword.querySelector("i");
    toggle_icon.addEventListener("click", () => {
        const type = password.getAttribute("type") === "password" ? "text" : "password";
        password.setAttribute("type", type);
        toggle_icon.classList.toggle("bi-eye");
    });
});

function onChangePassword() {
    const password = passwordInput.value;
    const letter = document.getElementById('letter');
    const capital = document.getElementById('capital');
    const number = document.getElementById('number');
    const length = document.getElementById('length');
    message.style.display = 'flex';
    if (password.match(/[a-z]/)) {
        letter.classList.replace('invalid', 'valid');
    } else {
        letter.classList.replace('valid', 'invalid')
    }
    if (password.match(/[A-Z]/)) {
        capital.classList.replace('invalid', 'valid');
    } else {
        capital.classList.replace('valid', 'invalid')
    }
    if (password.match(/[0-9]/)) {
        number.classList.replace('invalid', 'valid');
    } else {
        number.classList.replace('valid', 'invalid')
    }
    if (password.length >= 8) {
        length.classList.replace('invalid', 'valid');
    } else {
        length.classList.replace('valid', 'invalid')
    }
    const checks = [letter, capital, number, length];
    let valid = true;
    checks.forEach(check => {
        if (check.classList.contains('invalid')) {
            valid = false;
        }
    });
    if (valid) {
        document.querySelector('#message').style.display = 'none';
    }
}
function onChange() {
    const password = document.querySelector('input[name=password]');
    const confirm = document.querySelector('input[name=confirm_password]');
    if (confirm.value === password.value) {
        confirm.setCustomValidity('');
    } else {
        confirm.setCustomValidity('Passwords do not match');
    }
}