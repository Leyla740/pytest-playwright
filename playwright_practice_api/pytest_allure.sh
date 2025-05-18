#!/bin/bash

pytest "$@"
EXIT_CODE=$?

# Then view the report
if [ $EXIT_CODE -eq 0 ]; then
  allure serve allure-results
else
  allure generate allure-results -o allure-report --clean
  allure open allure-report
fi
