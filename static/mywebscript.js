"use strict";
window.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("analyze");
  const output = document.getElementById("system_response");
  button.addEventListener("click", async () => {
    const value = document.getElementById("textToAnalyze").value;
    output.textContent = "Analyzing…";
    try {
      const response = await fetch(`/emotionDetector?textToAnalyze=${encodeURIComponent(value)}`);
      output.textContent = await response.text();
    } catch (_error) {
      output.textContent = "Could not connect to the server. Please try again.";
    }
  });
});
