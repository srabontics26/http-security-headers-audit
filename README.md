# HTTP Security Header Audit

A Python tool for checking common HTTP security headers and identifying missing protections.

## About the Project

This project checks the HTTP response headers of a website and reports whether several commonly used security headers are present or missing.

I created this project to practice Python, HTTP requests, and basic web security concepts.

## Features

- Checks common HTTP security headers
- Displays the HTTP status code
- Reports present and missing headers
- Accepts a website URL from the user
- Handles connection errors

## Security Headers Checked

- Content-Security-Policy
- Strict-Transport-Security
- X-Content-Type-Options
- X-Frame-Options
- Referrer-Policy
- Permissions-Policy

## Technologies Used

- Python 3
- Requests library
- HTTP

## Installation

Install the required Python library:

```bash
pip install requests
