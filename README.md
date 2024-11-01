
# Smart Contract Vulnerability Detection API

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Running the API](#running-the-api)
4. [Making a Request to the Analyze Endpoint](#making-a-request-to-the-analyze-endpoint)
5. [Understanding the Response](#understanding-the-response)
6. [Screenshots of Postman Requests and Responses](#screenshots-of-postman-requests-and-responses)
7. [Future Work](#future-work)
8. [Contributing](#contributing)
9. [License](#license)
10. [Acknowledgments](#acknowledgments)

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Python 3.6 or higher**: You can download it from [python.org](https://www.python.org/downloads/).
- **Pip**: This is typically included with Python installations.
- **Git**: You can download it from [git-scm.com](https://git-scm.com/downloads).

## Installation

1. **Clone the Repository**: Open your terminal or command prompt and run the following command to clone the API repository:
   ```bash
   git clone https://github.com/your-repo/smart-contract-vulnerability-api.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd smart-contract-vulnerability-api
   ```

3. **Create a Virtual Environment (Optional but recommended)**:
   It's a good practice to use a virtual environment to manage dependencies. You can create one with the following commands:
   ```bash
   python -m venv venv
   ```

   Then, activate the virtual environment:
   - **On Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **On macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:
   Install the required Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Running the API

1. **Start the Flask Application**:
   Once the dependencies are installed, you can start the Flask API by running:
   ```bash
   python app.py
   ```

2. **Check if the API is Running**:
   By default, the API will run on `http://127.0.0.1:5000`. You can verify that it’s running by visiting this URL in your web browser. You should see a message indicating that the API is up and running.

## Making a Request to the Analyze Endpoint

To analyze a smart contract, send a POST request to the `/analyze` endpoint.

### Example Request

You can use Postman to send the request. Here’s how to set it up:

1. **Set the Request Type**: Change the request type to `POST`.
2. **Enter the URL**: Use `http://127.0.0.1:5000/analyze`.
3. **Set the Headers**: Under the "Headers" tab, add:
   - `Content-Type`: `application/json`
4. **Enter the Request Body**: Under the "Body" tab, select `raw` and enter the following JSON data:

```json
{
    "contract_code": "pragma solidity ^0.8.0;\n\ncontract Example {\n    address public owner;\n\n    constructor() {\n        owner = msg.sender;\n    }\n\n    function transfer(address _to, uint256 _value) public {\n        require(_to != address(0), \"Invalid address\");\n        // Transfer logic here\n    }\n}",
    "contract_name": "Example"
}
```

## Understanding the Response

After sending the request, you will receive a response that looks similar to this:

```json
{
    "contract_name": "Example",
    "findings": {
        "findings": [
            {
                "cwe": "CWE-190",
                "description": "Integer overflow/underflow vulnerability detected.",
                "mitre": "T1518",
                "suggestion": "Use SafeMath library to prevent overflows and underflows.",
                "vulnerability": "integer_overflow"
            }
        ]
    },
    "features": [3, 1, 1, 2],
    "suggestions": [
        "Suggestion: Use SafeMath library to prevent overflows and underflows."
    ]
}
```

### Response Fields

- **contract_name**: The name of the analyzed smart contract.
- **findings**: Detailed findings about detected vulnerabilities, including:
  - **cwe**: The Common Weakness Enumeration identifier.
  - **description**: A brief description of the vulnerability.
  - **mitre**: Related MITRE ATT&CK identifier.
  - **suggestion**: Suggested mitigation for the vulnerability.
- **features**: An array of extracted features based on the findings.
- **suggestions**: An array of actionable suggestions for mitigating the issues detected.

## Screenshots of   Requests and Responses in our rest API
 

### 2. Sending the Request in our API and Response
![Postman Sending Request](https://github.com/alauddin-sabari/smart-contract-vulnerablity-detection-API/blob/main/postman_request_response.jpg)


 
## Future Work

- **Machine Learning Integration**: Future updates may include machine learning models to provide more accurate vulnerability predictions and risk assessments.
- **Enhanced Vulnerability Detection**: Ongoing improvements to increase the robustness of vulnerability detection capabilities.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request. 

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **OpenZeppelin** for their libraries that promote secure smart contract development.
- The blockchain community for their continuous efforts in improving smart contract security.
 

### Instructions for Adding Screenshots
To add screenshots:
1. **Take Screenshots**: Use a screenshot tool to capture the Postman interface showing the request setup, the sending of the request, and the response from the API.
2. **Upload Screenshots**: Upload these screenshots to your GitHub repository, ideally in a dedicated folder (e.g., `screenshots`).
3. **Update Links**: Replace the placeholder image URLs in the `README.md` with the actual URLs to your uploaded images.

### Saving the File
To save this as a `README.md` file, follow the same steps as before:
1. Open a text editor.
2. Copy the Markdown content above.
3. Paste it into the editor.
4. Save the file as `README.md` in the root directory of your project. 

 
