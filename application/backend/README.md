
## Setup local environment

```shell
rm -rf .venv
python3 -m venv .venv ; pip install --upgrade pip ; source .venv/bin/activate


pip install -r requirements.txt

```


This will deploy the backend application in the port 8000


Start the application
```shell
uvicorn main:app --reload
```

To Stop the application type `ctrl + C` in the terminal that was started.





## FAQ

If the process doesn't stop, find the process and stop it manually
```shell
lsof -i :8000
kill -9 <PID>
```
