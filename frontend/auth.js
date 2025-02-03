const backendURL = "http://127.0.0.1:5000"; // Ensure this matches your Flask server

function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    fetch(`${backendURL}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.uid) {
            document.getElementById("centerdiv").style.display = "none";
            document.getElementById("chat-container").style.display = "block";
        } else {
            alert("Login failed: " + data.error);
        }
    })
    .catch(error => alert("Error: " + error));
}

function register() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    fetch(`${backendURL}/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.uid) {
            alert("Registration successful! Please log in.");
        } else {
            alert("Registration failed: " + data.error);
        }
    })
    .catch(error => alert("Error: " + error));
}

function logout() {
    document.getElementById("centerdiv").style.display = "flex";
    document.getElementById("chat-container").style.display = "none";
}