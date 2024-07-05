

# Code Review System

The Code Review System is a full-stack application designed to analyze and provide feedback on code snippets. The system consists of a backend for data processing and model training, and a frontend for user interaction and visualization of feedback.

## Table of Contents
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Backend](#backend)
  - [Data Preprocessing](#data-preprocessing)
  - [Feedback](#feedback)
  - [Model Evaluation](#model-evaluation)
  - [Model Training](#model-training)
  - [Retrain Model](#retrain-model)
  - [Utilities](#utilities)
- [Frontend](#frontend)
  - [Components](#components)
  - [Styling](#styling)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```
code_review_system/
├── src/
│   ├── data_preprocessing.py
│   ├── feedback.py
│   ├── model_evaluation.py
│   ├── model_training.py
│   ├── retrain_model.py
│   └── utils.py
frontend/
├── .eslintrc.cjs
├── .gitignore
├── README.md
├── index.html
├── package-lock.json
├── package.json
├── postcss.config.js
├── src/
│   ├── App.jsx
│   ├── components/
│   │   ├── CodeInput.jsx
│   │   ├── Header.jsx
│   │   └── ResultFeedback.jsx
│   ├── index.css
│   └── main.jsx
├── tailwind.config.js
└── vite.config.js
```

## Installation

### Backend

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/code_review_system.git
    cd code_review_system
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Frontend

1. Navigate to the frontend directory:
    ```bash
    cd frontend
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

## Usage

### Backend

To run the backend processes, you can use the following scripts:
- `data_preprocessing.py`: Preprocesses the data for model training.
- `feedback.py`: Generates feedback based on the model's output.
- `model_evaluation.py`: Evaluates the performance of the model.
- `model_training.py`: Trains the model using the preprocessed data.
- `retrain_model.py`: Retrains the model with new data.
- `utils.py`: Contains utility functions used across the project.

Example command to run a script:
```bash
python src/data_preprocessing.py
```

### Frontend

1. Start the development server:
    ```bash
    npm run dev
    ```

2. Open your browser and navigate to `http://localhost:3000`.

### Components

- **Header**: Displays the header of the application.
- **CodeInput**: A textarea input where users can paste their code snippets.
- **ResultFeedback**: Displays feedback with strengths, weaknesses, and visual charts.

### Styling

The frontend uses Tailwind CSS for styling. Configuration files such as `tailwind.config.js` and `postcss.config.js` are included.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any bugs, features, or improvements.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Explanation:

- **Project Structure**: Lists all files and directories in the project.
- **Installation**: Provides steps to install dependencies for both the backend and frontend.
- **Usage**: Details how to run backend scripts and start the frontend development server.
- **Components**: Describes the key components of the frontend.
- **Styling**: Mentions the use of Tailwind CSS for styling.
- **Contributing**: Provides guidelines for contributing to the project.
- **License**: Mentions the license under which the project is distributed.

You can adjust the `git clone` URL and other details according to your specific repository and needs.

## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.

