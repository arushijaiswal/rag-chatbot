// script.js - Main JavaScript for RAG Chatbot
// Handles user interactions, sending questions to Flask backend, and displaying answers

const sendBtn = document.getElementById('send-btn');
const userInput = document.getElementById('user-input');
const chatBox = document.getElementById('chat-box');

sendBtn.addEventListener('click', async () => {
    const question = userInput.value.trim();
    if (!question) return;

    // Display user question
    const userDiv = document.createElement('div');
    userDiv.textContent = `You: ${question}`;
    userDiv.style.fontWeight = 'bold';
    chatBox.appendChild(userDiv);

    // Clear input
    userInput.value = '';

    try {
        const response = await fetch('/ask', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question })
        });

        const text = await response.text(); // read raw text
        let data;

        try {
            data = JSON.parse(text);
        } catch {
            data = { answer: text || '⚠️ Invalid response from server' };
        }

        const botDiv = document.createElement('div');
        botDiv.textContent = `Bot: ${data.answer}`;
        botDiv.style.marginBottom = '10px';
        chatBox.appendChild(botDiv);

    } catch (err) {
        const botDiv = document.createElement('div');
        botDiv.textContent = `Bot: Request failed → ${err}`;
        botDiv.style.color = 'red';
        botDiv.style.marginBottom = '10px';
        chatBox.appendChild(botDiv);
    }

    // Scroll to bottom
    chatBox.scrollTop = chatBox.scrollHeight;
});

// Optional: Press Enter to send
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendBtn.click();
    }
});
