# Week 4 — Libraries, APIs & Logic Modules

> ⚠️ These are **personal projects** built while studying CS50P. They are not solutions to CS50P problem sets and were never submitted as such.

Week 4 focused on Python's modularity — solving real-world problems using external libraries and live API data.

---

## Projects

### DNI-Age-Estimator (Argentina)
A backend utility that estimates a person's age based on their Argentine DNI number.

- Developed a custom algorithm mapping DNI ranges to approximate birth years
- Implemented input validation to ensure correct integer format

### Dolar-to-Arg-Peso (Real-Time Converter)
A financial tool that tracks the Argentine exchange rate using live data.

- Fetches real-time exchange rates via API so the converter never goes stale
- Dynamic multiplication to convert USD to ARS based on the latest fetched rate

### PuedoSalir (Posadas & Dos de Mayo Editions)
Localized weather checkers that help users in Misiones decide if it's a good time to go outside.

- Used coordinates specific to Dos de Mayo and Posadas
- Utilized the `requests` library to communicate with weather APIs
- Decision engine that interprets weather data into a simple user-friendly recommendation

### Coin-Flip Simulator
A simple probability tool using Python's built-in `random` module.

- Clean, minimal code for quick iterative execution

---

## What I Learned
How to consume external APIs, handle live data, and build tools that solve real problems for real places — including my own hometown.
