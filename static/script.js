const sendBtn = document.getElementById("sendBtn");
const messageEl = document.getElementById("message");
const modelEl = document.getElementById("model");
const outputEl = document.getElementById("output");

sendBtn.addEventListener("click", async () => {
  outputEl.textContent = "Thinking...";

  const response = await fetch("/generate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      message: messageEl.value,
      model: modelEl.value
    })
  });

  const data = await response.json();
  outputEl.textContent = JSON.stringify(data, null, 2);
});