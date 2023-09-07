# wework-desk-booking-automation

## Usage

1. First of all, you need to set your wework credentials into .env file. You can use .env.default as a template. The .env file should be in the same directory as the script. Besides email and password, you also find environment variables such as `TIME` and `OFFICE_ID`. `TIME` variable is about your internet connection, so if the script fails, you can increase its value. `OFFICE_ID` is the id of wework office that you want to book desks in. The default value is North West House in Marylebone, London.
2. Install dependencies: `poetry install`.
3. Run the script: `poetry run python3 __init__.py`. It will book a desk for each day of the current month.
