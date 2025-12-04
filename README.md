This project is an AI-powered meeting assistant built with ReadAI's tech stack. It's primarily a backend service that 
processes meeting transcripts (via Claude AI) to extract key insights (action items, dicussion topics, and basic sentiment analysis).

**Prerequisites**
1. Docker Desktop
2. Anthropic API Key

**Installation**
1. Clone the repo ().
2. Set your API Key, I used Anthropic to generate mine (export ANTHROPIC_API_KEY="Enter your key here").
3. Download + open the project and install all necessary libraries.
2. Start the program ("docker-compose up --build").
3. Access the API by visiting "http://localhost:8000/docs" in your browser.

**How to Use It**
1. Register a user by clicking "Post" and "Try it out" under auth/register
<img width="798" height="67" alt="Screenshot 2025-12-03 at 3 57 13 PM" src="https://github.com/user-attachments/assets/edca156e-ba73-4086-8ba1-7d618737e2ff" />

2. Enter an example email and password to create a new user (email: test1@example.com, password: password1234)
<img width="759" height="143" alt="Screenshot 2025-12-03 at 3 57 58 PM" src="https://github.com/user-attachments/assets/2456f600-d55f-4900-9f4f-68c426ba717b" />

3. Click "Execute" to create a new user
<img width="754" height="53" alt="Screenshot 2025-12-03 at 3 58 35 PM" src="https://github.com/user-attachments/assets/cdca45ca-79ea-4843-8564-2dc9d009f982" />

4. Click "Authorize" to log in with new user credentials, enter your username + password and click "Login" 
<img width="179" height="58" alt="Screenshot 2025-12-03 at 3 59 00 PM" src="https://github.com/user-attachments/assets/607d489d-1e88-41f7-8a6f-d506806eba1a" />

5. Enter information of a new meeting by clicking "Post" and "Try it out" under meetings/meetings. Enter JSON data that includes: Title of meeting, transcript, Duration Minutes, and Participant Count.
<img width="766" height="288" alt="Screenshot 2025-12-03 at 4 01 15 PM" src="https://github.com/user-attachments/assets/a76095c6-3215-46d7-b39b-5f2e029a2865" />

6. Click "Execute" to generate meeting insights
<img width="763" height="446" alt="Screenshot 2025-12-03 at 4 02 42 PM" src="https://github.com/user-attachments/assets/097b3f53-67c8-4afa-80fd-efbe69270b98" />
   
**Tech Stack**
Language: Python
Framework: FastAPI
Database: PostgreSQL + SQLAlchemy
Validation: Pydantic
Auth: JWT
AI: Claude API (Anthropic)
Container: Docker
Interactive API Documentation: Swagger UI

