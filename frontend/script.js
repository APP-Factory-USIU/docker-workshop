const API_URL = "http://localhost:5000";

async function loadFeedback() {

    const response =
        await fetch(`${API_URL}/feedback`);

    const feedback =
        await response.json();

    document.getElementById("feedback-list").innerHTML =
        feedback
            .map(item => `<li>${item}</li>`)
            .join("");
}

async function submitFeedback() {

    const input =
        document.getElementById("feedback");

    const message =
        input.value.trim();

    if (!message) {
        return;
    }

    await fetch(`${API_URL}/feedback`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message
        })
    });

    input.value = "";

    loadFeedback();
}

loadFeedback();
