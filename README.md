# Simple Python Flask App

This is a simple Python Flask application that demonstrates various routes and functionality.

## Routes

### Home Page

- **Route:** `/` or `/index`
- **Description:** Displays the home page of the app.
- **Usage:** Access the app's main page.

### Hello Page

- **Route:** `/hello/` or `/hello/<name>`
- **Description:** Displays a greeting message. If a name is provided as a URL parameter, it's included in the greeting.
- **Usage:** Access this page to receive a greeting message. You can provide your name in the URL to personalize the greeting.

### User / Client IP Address Finder

- **Route:** `/myIP`
- **Description:** Displays the user/client's IP address.
- **Usage:** Access this page to find out your IP address.

### Test Page

- **Route:** `/test`
- **Description:** Displays a test page from the static files.
- **Usage:** Access this page to view a test page from the static files.

## Error Handling

- **Error 404 Page Not Found**
  - **Route:** `/<invalid_route>`
  - **Description:** Displays an error message when a requested page is not found.
  - **Usage:** Access an invalid route to see the 404 error page.

## How to Run

1. Clone or download this repository to your local machine.
2. Ensure you have Python and Flask installed.

```bash
  pip install -r requirements.txt
```

3. Open a terminal and navigate to the app's root directory.
4. Run the app using the following command:

```bash
  python app.py
```

5. Open a web browser and access the routes described above.

## Run in Docker Container

1. Pull the container image from Docker Registry

```bash
  docker pull 227prajwal/flask-app
```

2. Run the Docker Container using the following command:

```bash
  docker run -dit -p 5000:5000 227prajwal/flask-app
```

3. Open a web browser and access the routes described above.

## Author

- Prajwal Patil
- Contact: patilprajwal22@gmail.com
