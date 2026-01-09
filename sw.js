// Lakjit Service Worker - Cache-First Strategy
const CACHE_NAME = 'lakjit-v1';
const urlsToCache = [
    '/',
    '/index.html',
    '/static/style.css',
    '/static/background.jpg',
    '/static/background-night.jpg',
    '/static/yi-icon.png',
    '/static/ji-icon.png',
    '/static/dark-incense.png',
    '/static/white-incense.png',
    '/static/lak-jit.jpg',
    '/static/icon-192.jpg',
    '/static/icon-512.jpg',
    'https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;700;900&display=swap',
    'https://cdn.jsdelivr.net/npm/lunar-javascript@1.7.7/lunar.min.js',
    'https://cdn.jsdelivr.net/npm/html2canvas@1.4.1/dist/html2canvas.min.js'
];

// Install event - cache all resources
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => {
                console.log('Opened cache');
                return cache.addAll(urlsToCache);
            })
    );
    self.skipWaiting();
});

// Activate event - clean up old caches
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((cacheName) => {
                    if (cacheName !== CACHE_NAME) {
                        console.log('Deleting old cache:', cacheName);
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
    self.clients.claim();
});

// Fetch event - Cache-First strategy
self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request)
            .then((response) => {
                // Cache hit - return response from cache
                if (response) {
                    return response;
                }

                // Clone the request
                const fetchRequest = event.request.clone();

                return fetch(fetchRequest).then((response) => {
                    // Check if valid response
                    if (!response || response.status !== 200 || response.type !== 'basic') {
                        return response;
                    }

                    // Clone the response
                    const responseToCache = response.clone();

                    caches.open(CACHE_NAME)
                        .then((cache) => {
                            cache.put(event.request, responseToCache);
                        });

                    return response;
                }).catch(() => {
                    // If fetch fails, return offline page or cached version
                    return caches.match('/index.html');
                });
            })
    );
});
