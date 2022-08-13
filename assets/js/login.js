const togglePassword = document.querySelector("#togglePassword");
const password = document.querySelector("#password");

togglePassword.addEventListener("click", function () {
  const type =
    password.getAttribute("type") === "password" ? "text" : "password";
  password.setAttribute("type", type);
  this.classList.toggle("bi-eye");
});
const form = document.querySelector("form");
form.addEventListener("submit", function (e) { });

const rmCheck = document.getElementById("rememberMe");
const usernameInput = document.getElementById("username");
const passwordInput = document.getElementById("password");

if (localStorage.checkbox && localStorage.checkbox !== "") {
  rmCheck.setAttribute("checked", "checked");
  usernameInput.value = localStorage.username;
  passwordInput.value = localStorage.password;
} else {
  rmCheck.removeAttribute("checked");
  usernameInput.value = "";
  passwordInput.value = "";
}
function lsRememberMe() {
  if (rmCheck.checked && usernameInput.value.trim() !== '' && passwordInput.value.trim() !== "") {
    localStorage.username = usernameInput.value;
    localStorage.password = passwordInput.value;
    localStorage.checkbox = rmCheck.value;
  } else {
    localStorage.username = "";
    localStorage.checkbox = "";
    localStorage.password = "";
  }
}
