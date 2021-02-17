# GooseTools
GooseTools is the Earlier Single-Tenant version of SpacePaperwork.com. 

## Project Structure
* The app under config/ is where you'll find the settings files and similar high level project configuration.
* Find the project's applications under the goosetools/ subfolder.

# Pre-Requisites
1. https://git-scm.com/book/en/v2/Getting-Started-Installing-Git/
2. https://docs.docker.com/get-docker/
3. https://docs.docker.com/compose/install/
4. All the commands assume you are working from a bash shell.

# How To Run Locally Using Docker
1. ```git clone git@github.com:GROON-Echoes-Dev-Team/goosetools.git && cd goosetools```
2.
    ```
    docker-compose -f local.yml up --build
    ```
3. Visit and Sign Up On http://localhost:8000/goosetools
4. Make yourself an admin after signing up by (replace username if you signup with a different one!): ```./docker_managepy.sh runscript make_user_admin --script-args="TEST USER123456789"```
5. Import market data using: ```./docker_managepy.sh runjobs hourly```
6. Get an interactive python shell into goosetools by ```./docker_managepy.sh shell_plus```
7. Run non-integration tests ```./tests.sh```
8. Run integration tests ```./integration_test.sh```
9. Watch filesystem for changes and re-run non-integration tests when something changes ```./test_watcher.sh```
10. Run pre-commit checks ```./pre_commit_checks.sh```

# How To Run Locally in a Virtual Environment

## Pre-Requisites
1. A running PostgreSQL server with a new database for use by Goosetools is required

## Steps

1. ```git clone git@github.com:GROON-Echoes-Dev-Team/goosetools.git && cd goosetools```
2.
    ```
    cp .env.local.example .env
    ```
3. Edit ```.env``` to match your environment, most importantly setting DATABASE_URL to match your new database.
4. Setup a virtual env:
    ```
    python3 -m venv venv
    ```
5. Activate the virtual env:
    ```
    source venv/bin/activate
    ```
6. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
7. Create the Database Schema:
   ```
   ./manage.py migrate
   ```
8. Load initial data:
   ```
   ./manage.py loaddata goosetools/**/fixtures/*.json
   ```
9. Run the server:
    ```
    ./manage.py runserver_plus
    ```
8. Visit and Sign Up On http://localhost:8000/goosetools
9. Make yourself an admin by (replace the username if you entered a non-default value on sign-up):
    ```
    ./manage.py runscript make_user_admin --script-args="TEST USER123456789"
    ```
10. Import market data using:
    ```
    ./manage.py runjobs hourly
    ```
11. Get an interactive python shell into goosetools:
    ```
    ./manage.py shell_plus
    ```
12. Run non-integration tests:
    ```
    pytest
    ```
13. Run integration tests:
    ```
    ./integration_test.sh
    ```
14. Watch filesystem for changes and re-run non-integration tests when something changes:
    ```
    ptw
    ```
15. Run pre-commit checks:
    ```
    pre-commit run --all-files
    ```
16. Install pre-commit checks:
    ```
    pre-commit install
    ```
