# Week 5 — Unit Tests & API Integration

> ⚠️ These are **personal projects** built while studying CS50P. They are not solutions to CS50P problem sets and were never submitted as such.

Week 5 focused on making code production-ready — robust error handling, API consumption, and unit testing with `pytest`.

---

## Projects

### Dollar To Currencies (Telegram Bot)
My first full-scale Telegram bot providing real-time currency conversion for the global market.

- Fetches live data from the Frankfurter API using `requests`
- Used `python-dotenv` to keep sensitive tokens out of source code
- Implemented `try/except` to catch `ValueError` and `IndexError` — the bot stays online during bad user input
- Used HTML parsing to format a clean, readable currency list

### "Can I Go Out?" — Weather Checker (Los Angeles)
A weather utility that helps users in the USA decide if outdoor conditions are suitable.

- Evaluates temperature and sky conditions via external weather APIs
- Returns a simple Yes/No based on specific weather thresholds

### "Puedo Salir" — Weather Checker (Dos de Mayo)
A localized version of the weather tool for my hometown in Misiones, Argentina.

- Configured for the specific coordinates of Dos de Mayo
- Localized string responses while keeping backend logic in English
- Extracted specific values from complex nested JSON responses

---

## What I Learned
Error handling, API integration, and writing `pytest` unit tests — the skills that make code reliable enough to actually ship.
