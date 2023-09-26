# wework-desk-booking-automation

## Usage

1. First of all, you need to clone this repo on your local machine.
2. After that set needed parameters into the `.env` file, you need to create it by yourself. You can use `.env.default` as a template. The `.env` file should be in the cloned repo directory.
   Besides the email and password from your WeWork account in the `.env.default` file, you will also find:
   - `OFFICE_ID`: `String(UUID)`, This is the ID of the office where want to book a desk. The default value is UUID for **North West House in Marylebone, London**.
   - `TIME_OFFSET`: `Integer`, This variable is for offsetting all actions on the web page. It is useful if you have a slow internet connection. The default value is **0**.
   - `DAYS`: `Integer`, This variable is for how many days you want to book a desk. The default value is **7**.
   - `WEEKENDS`: `Boolean`, Do you want to book a desk for weekends? The default value is **False**.
   - `BROWSER`: `String`, Which browser do you want to use? The default value is `Safari`. You can use `Chrome`, `Firefox`, or `Safari`.
   Please set all of these parameters into your `.env` file.
3. Also, you need to Allow Remote Automation in Safari. You can do it by clicking on Develop in the menu bar and then clicking on Allow Remote Automation(3rd from the bottom of the list).
4. Install `poetry`, installation guide - https://python-poetry.org/docs/#installation.
5. Install dependencies with `poetry`: `poetry install`.
6. Run the script(You should do it in repo directory om your local machine): `poetry run python3 __init__.py`.

### ✨Tip✨

If you want to start automation from any directory in your terminal, you can do it by running this command:

```bash
cd {{directory}} && poetry run python3 __init__.py
```

As you can see this command contains one variable - `{{directory}}`. `{{directory}}` is the path to the directory where the wework-desk-booking-automation repo is located on your machine. And if you want to execute this command from any directory, please start your `{{directory}}` with `/` or `~`. If you have a GitHub folder with all the repos in your Users Documents folder, then the `{{directory}}` should look like `~/Documents/Github/wework-desk-booking-automation`.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
