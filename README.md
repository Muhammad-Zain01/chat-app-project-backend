
## ChatGPT Clone Project (Backend

### Overview

This repository contains the backend component of a ChatGPT clone project, developed using Django ([for front end repo](https://github.com/Muhammad-Zain01/chat-app-project)). It serves as the intermediary between the front-end application, built with Next.js, and OpenAI's conversational AI via APIs. The Django backend is designed to handle requests from the front end, process them through OpenAI's API, and return conversational AI responses to the user interface. This setup enables a seamless integration of OpenAI's powerful AI models with a custom user-friendly web interface, allowing for rich, interactive AI conversations.

![Login](https://raw.githubusercontent.com/Muhammad-Zain01/chat-app-project/main/preview/preview1.png)
![Register](https://raw.githubusercontent.com/Muhammad-Zain01/chat-app-project/main/preview/preview2.png)
![Dashboard](https://raw.githubusercontent.com/Muhammad-Zain01/chat-app-project/main/preview/preview3.png)
![Dashboard](https://raw.githubusercontent.com/Muhammad-Zain01/chat-app-project/main/preview/preview4.png)

### Setup Instructions

##### Clone the Repository

```
    git clone https://github.com/Muhammad-Zain01/chat-app-project-backend
```

##### Create a Virtual Env

```
    python -m venv env
```
###### For Activate Env in Windows 

```
    env/Scripts/activate
```

###### For Activate Env in MacOS 

```
    source env/bin/activate
```

##### Install Dependencies

```
    cd chat-app-project-backend
    cd app
    pip install -r requirements.txt
```

##### Environment Configuration

Create a .env file in the root directory of your project and populate it with the necessary environment variables. Here's an example of what your .env file should look like

```
    OPENAPI_KEY="<API-KEY>"
```

##### Run the Migration

```
    python manage.py runmigrations
    python manage.py migrate
```

##### Run the Server

```
    python manage.py runserver
```

This will start the development server on [http://127.0.0.1:8000/](http://127.0.0.1:8000). Navigate to this URL in your browser to interact with the application.
