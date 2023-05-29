# Writer's Block

Writer's Block is a proof of concept for a virtual writing companion, providing writers with real-time suggestions and corrections based on established style guides. This AI-powered editor ensures that your writing aligns with the recommended conventions, grammar rules, and best practices of your desired style guide. With an intuitive interface and a user-friendly experience, 

## Features

- Apply a default set of style rules to your writing
- HTML and Markdown outputs

## Requirements

- An OpenAI API Key

## Running locally

Create an environment file using the sample, and edit it to supply required values:
```shell
cp .env_sample .env
```


Activate the environment:
```shell
poetry install
poetry shell
```

Then, start the Flask backend.
```shell
PYTHONPATH=src/libs FLASK_APP=src/app/app.py flask run
```

Start the Front-End
```shell
npm install
cd src/client
npm install
npm run autobuild
```

## References

- https://dev.to/mburszley/an-introduction-to-poetry-2b6n#installation
- https://www.twilio.com/blog/build-digital-sticky-notes-app-flask-svelte
