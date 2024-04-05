**Install dependencies:**
pip install -r requirements.txt

**Run migrations:**
python manage.py makemigrations
python manage.py migrate

**Run the local server:**
python manage.py runserver

**API Endpoints**

Matches Endpoints:
*GET /api/matches/: Retrieve a list of all matches.
*POST /api/matches/: Create a new match.

Admin Authentication Endpoints:
*POST /api/admin/signup/: Register a new admin user.
*POST /api/admin/login/: Log in an admin user.

Team Squad Endpoint:
*POST /api/teams/{team_id}/squad/: Add a player to the squad of a specific team.

Player Detail Enpoint:
*GET /api/players/{player_id}/: Retrieve a list of all players.

**Test Using Postman**
*Add Headers (if required):
*If your API requires headers (e.g., Authorization, Content-Type), click on the "Headers" tab below the request URL.
*Add headers by clicking on the "Add Row" button and entering the key-value pairs.
**key: Authorization
**value: Token <token>

**<token> : access token recived as a response after successful login



