#!/bin/bash

# Set path for Python interpreter
PYTHON_INTERPRETER=$(which python3)
echo "Python directory: $PYTHON_INTERPRETER"

# Set path for test script
CURRENT_DIR=$(pwd)
echo "Current directory: $CURRENT_DIR"
TEST_FILE=$1
TEST_SCRIPT="$CURRENT_DIR/tests/$TEST_FILE" # test_leagues.py

# Run the test script
echo "Running Appium tests..."
"$PYTHON_INTERPRETER" "$TEST_SCRIPT"
