# wework-desk-booking-automation

## Usage

1. First of all, you need to set your WeWork credentials into the `.env` file. You can use `.env.default` as a template. The `.env` file should be in the same directory as the script.
   Besides the email and password from your WeWork account in the `.env.default` file, you will also find:
   - `OFFICE_ID`: String(UUID), This is the ID of the office where want to book a desk. The default value is North West House in Marylebone, London.
   - `TIME_OFFSET`: Integer, This variable is for offsetting all actions on the web page. It is useful if you have a slow internet connection. The default value is 0.
   - `DAYS`: Integer, This variable is for how many days you want to book a desk. The default value is 1.
   - `WEEKENDS`: Boolean, Do you want to book a desk for weekends? The default value is False.
   - `BROWSER`: String, Which browser do you want to use? The default value is Safari. You can use Chrome, Firefox, or Safari.
2. Also, you need to Allow Remote Automation in Safari. You can do it by clicking on Develop in the menu bar and then clicking on Allow Remote Automation(3rd from the bottom of the list).
3. Install dependencies: `poetry install`.
4. Run the script: `poetry run python3 __init__.py`.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
