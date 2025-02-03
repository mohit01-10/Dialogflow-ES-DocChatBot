function sendMessage() {

    const message = document.getElementById("user-input").value;
    if (!message) return;

    const chatbox = document.getElementById("chatbox");

    // Append user message
    chatbox.innerHTML += `<div class="message user"><strong>You:</strong> ${message}</div>`;

    fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ session_id: "12345", message: message })
    })
    .then(response => response.json())
    .then(data => {
        // Append bot message
        chatbox.innerHTML += `<div class="message bot"><strong>Bot:</strong> ${data.response}</div>`;
    
        scrollToBottom();

    });

    document.getElementById("user-input").value = "";

    scrollToBottom();
}


function scrollToBottom() {
    const chatboxContainer = document.getElementById("chatbox");
    chatboxContainer.scrollTop = chatboxContainer.scrollHeight;
}

document.addEventListener("DOMContentLoaded", function () {
 
    document.getElementById("user-input").addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            event.preventDefault(); // Prevent default form submission
            sendMessage();
        }
    });
});