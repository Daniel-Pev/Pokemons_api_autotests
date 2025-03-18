
**Pokémon Battle API Test Suite**
=====================================

**Overview**
------------

This project is a test suite for the Pokémon Battle API. It uses Docker to automate testing and reporting.

**Features**
------------

* Automated testing of Pokémon Battle API endpoints
* Reporting of test results using Allure
* Support for multiple environments (DEV, PROD)

**Requirements**
---------------

* Docker 24.0.5 or later
* Python 3.10 or later

**Usage**
-----

1. Clone this repository
2. Create a `.env` file with the required environment variables (see below)
3. Run `docker compose up` to start the test suite

**Environment Variables**
------------------------

The following environment variables are required:

* `STAGE`: The environment to test (DEV or PROD)
* `TOKEN_PROD`: The API token for the PROD environment
* `TOKEN_DEV`: The API token for the DEV environment
* `TRAINER_ID_PROD`: The trainer ID for the PROD environment
* `TRAINER_ID_DEV`: The trainer ID for the DEV environment

**Reporting**
------------

Test results are reported using Allure. The report is generated after each test run and can be found in the `allure-report` directory.

You can see the tests run trend history on github pages:
https://daniel-pev.github.io/Pokemons_api_autotests
