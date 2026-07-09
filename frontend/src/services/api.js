const BASE_URL = "http://127.0.0.1:8000";
console.log("API FILE RUNNING");
export async function saveInteraction(data) {
  const response = await fetch(`${BASE_URL}/log-interaction`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  return response.json();
}
export async function getInteractions() {
  const response = await fetch(`${BASE_URL}/interactions`);
  return response.json();
}

export async function sendChat(message) {
  const response = await fetch(`${BASE_URL}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message }),
  });

  return response.json();
}