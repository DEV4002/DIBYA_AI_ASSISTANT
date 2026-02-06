function sendMessage() {
    const input = document.getElementById("userInput");
    const chat = document.getElementById("chat");
    const mouth = document.querySelector(".mouth");

    const userMessage = input.value.trim();
    if (!userMessage) return;

    // Show user message
    chat.innerHTML += `<p><b>You:</b> ${userMessage}</p>`;
    chat.scrollTop = chat.scrollHeight;

    // Robot talking animation
    if (mouth) mouth.style.height = "16px";

    // Send message to Flask backend
    fetch("/get_response", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userMessage })
    })
    .then(response => response.json())
    .then(data => {
        chat.innerHTML += `<p><b>Dibya:</b> ${data.response}</p>`;
        chat.scrollTop = chat.scrollHeight;

        if (mouth) mouth.style.height = "8px";
    })
    .catch(error => {
        chat.innerHTML += `<p><b>Dibya:</b> ⚠️ Server error. Try again.</p>`;
        chat.scrollTop = chat.scrollHeight;

        if (mouth) mouth.style.height = "8px";
        console.error("Error:", error);
    });

    // Clear input box
    input.value = "";
}

function clearChat() {
    document.getElementById("chat").innerHTML = "";
}

function robotHi() {
    const hands = document.querySelectorAll(".left-hand, .right-hand");
    const chat = document.getElementById("chat");

    // Wave animation
    hands.forEach(hand => hand.classList.add("wave"));

    chat.innerHTML += `<p><b>Dibya:</b> Hi 👋 I’m Dibya! How can I help you?</p>`;
    chat.scrollTop = chat.scrollHeight;

    setTimeout(() => {
        hands.forEach(hand => hand.classList.remove("wave"));
    }, 1000);
}
