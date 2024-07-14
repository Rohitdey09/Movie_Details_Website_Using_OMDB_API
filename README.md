```markdown
# OMDB API Movie Details Website

## Overview

This is a web application that provides detailed information about movies using the OMDB API. The website is built using Flask to offer a simple and responsive user interface for fetching and displaying movie details.

## Features

- Search for movies by title
- Display movie details including plot, ratings, release date, and more
- Responsive design

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Rohitdey09/omdb-movie-details.git
   cd omdb-movie-details
   ```


2. **Set up the environment variables:**
   - Create a `.env` file in the root of your project.
   - Add your OMDB API key in the `.env` file:
     ```env
     OMDB_API_KEY=your_api_key_here
     ```

3. **Run the Flask development server:**
   ```sh
   flask run
   ```

## Usage

1. Open your web browser and go to `http://localhost:5000`.
2. Use the search bar to type in the name of the movie you want to look up.
3. Click the search button to fetch and display the movie details.

## Technologies Used

- **Backend:** Flask
- **Frontend:** HTML, CSS, JavaScript
- **API:** OMDB API


## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add your feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Open a pull request.

## Acknowledgements

- [OMDB API](http://www.omdbapi.com/)
- [Flask](https://flask.palletsprojects.com/)
```

