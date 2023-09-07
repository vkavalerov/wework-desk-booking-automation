# wework-desk-booking-automation

## Usage

1. First of all, you need to set your wework credentials into .env file. You can use .env.default as a template. The .env file should be in the same directory as the script.
   Besides email and password, you will also find:
   - `OFFICE_ID`: String(UUID), This is the ID of the office where want to book a desk. The default value is North West House in Marylebone, London.
   - `TIME_OFFSET`: Integer, This variable is for offsetting all actions on the web page. It is useful if you have a slow internet connection. The default value is 0.
   - `DAYS`: Integer, This variable is for how many days you want to book a desk. The default value is 1.
   - `WEEKENDS`: Boolean, Do you want to book a desk for weekends? The default value is False.
2. Install dependencies: `poetry install`.
3. Run the script: `poetry run python3 __init__.py`. It will book a desk for each day of the current month.
