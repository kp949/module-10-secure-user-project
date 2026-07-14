# Module 10 Reflection Draft

In this module, I expanded my FastAPI calculator project by adding a secure user model with SQLAlchemy and Pydantic. This helped me understand how a web application connects API routes, validation, and a database together. I also learned why applications should never store plain text passwords. Instead, the app hashes the password before saving it and uses a verify function when checking a password.

One challenge was understanding how the database tests work differently from regular unit tests. Unit tests are smaller and focus on one function, like password hashing or schema validation. Integration tests are more realistic because they check how the API and database work together. I overcame this by separating my tests into unit and integration folders and using a test database so the tests could run safely.

Automated testing is important because it catches mistakes before code is deployed. GitHub Actions made this even more useful because tests run automatically every time I push my code. I also learned how Docker helps package the app so it can run in a consistent environment.

Using Git helped me track my changes and made the project easier to manage. Committing regularly is useful because it gives me checkpoints to return to if something breaks. I also tried to apply DRY principles by keeping repeated database and security logic in helper files. I want to keep improving my understanding of Docker Hub deployment, CI/CD secrets, and how real authentication systems are built in larger applications.

