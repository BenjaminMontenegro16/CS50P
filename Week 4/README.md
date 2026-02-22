📂 Week 4: APIs & External Data Integration
This week, I mastered the art of fetching real-time data from external servers, handling authentication keys, and managing network-layer exceptions to build a live financial utility.

🚀 Project: The Real-Time Bitcoin Price Index
A professional-grade command-line tool that communicates with the CoinCap v3 REST API to provide instant Bitcoin-to-USD valuations.

API Authentication: Implemented secure HTTP Headers to pass Bearer Tokens, allowing authorized access to protected data endpoints.

JSON Deep-Parsing: Developed logic to traverse complex nested dictionaries and extract specific data points from JSON responses.

Production-Grade Error Handling: Utilized try/except blocks to catch RequestException, KeyError, and ValueError, ensuring the program exits gracefully without "Tracebacks" even if the API server is down.

Financial Formatting: Leveraged f-strings with thousands-separators (:,) and specific float precision (.4f) to meet international banking display standards.

📓 Developer Insights for US Recruiters

External Integration: This project proves I can connect Python applications to the outside world, a fundamental skill for any Backend Developer working in the US market.

Security Mindset: By moving from public endpoints to authenticated v3 APIs, I am practicing how to handle sensitive credentials like API Keys.

Handling Unreliability: I designed this script with the understanding that "the internet breaks," implementing silent exits to maintain a professional user experience.

🚀 Bonus Projects (Early Week 4)
I also worked on these utilities to sharpen my logic before hitting the APIs:

The Pro-CoinFlip: A probability simulator using the random library to test outcome frequencies.

DNI Age Estimator: A logic-heavy script that estimates a person's age based on Argentine DNI numbering patterns, using strictly local data and custom algorithms.
