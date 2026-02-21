Argentine DNI Age Estimator
A robust Python utility for demographic data estimation.

🚀 Overview
This project is a backend utility designed to estimate a user's age based on their Argentine National Identity Document (DNI) number. Since DNI numbers in Argentina are issued sequentially, the application uses numerical range logic to provide an approximate age bracket.

🛠️ Key Backend Features
To ensure the program is "production-ready" and user-friendly, I implemented several core programming concepts from CS50P (Harvard):

Data Sanitization: The script automatically handles localized formatting (e.g., 45.000.000) by stripping whitespace and removing decimal points before processing.

Defensive Programming: Using try/except blocks, the system catches ValueError exceptions to prevent crashes if a user enters non-numeric characters.

Infinite Input Loop: A while True loop ensures the application remains active until valid data is successfully processed.

Logical Efficiency: Uses optimized integer comparison ranges instead of heavy string manipulation for faster performance.

🌍 Localization Note
The user interface (prompts and outputs) is in Spanish to align with the local Argentine market. However, the codebase, logic structure, and documentation are maintained in English to meet international professional standards.
