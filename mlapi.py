from flask import Flask, request, jsonify
import json
import pickle

app = Flask(__name__)

# Load your pre-trained machine learning model here if necessary
# Example: model = pickle.load(open('smart_contract_model.pkl', 'rb'))

def extract_features_from_findings(findings):
    features = []
    
    if isinstance(findings, dict):
        vulnerabilities = findings.get("findings", [])
        feature_count = len(vulnerabilities)

        # Feature counts for specific vulnerabilities
        integer_overflow = 0
        unchecked_low_level_calls = 0
        warnings_count = 0
        suggestions = []

        for finding in vulnerabilities:
            if finding.get("vulnerability") == "integer_overflow":
                integer_overflow += 1
                suggestions.append(f"Suggestion: {finding.get('suggestion')}")
            if "low-level calls" in finding.get("description", "").lower():
                unchecked_low_level_calls += 1
                suggestions.append("Suggestion: Ensure return values of low-level calls are checked.")
            if "Warning" in finding.get("description", ""):
                warnings_count += 1

        features = [
            feature_count,
            integer_overflow,
            unchecked_low_level_calls,
            warnings_count,
        ]
    else:
        print("Unexpected findings structure.")
    
    return features, suggestions


@app.route('/analyze', methods=['POST'])
def analyze_contract():
    data = request.get_json()

    # Ensure the JSON request body has the required fields
    if not data or 'contract_code' not in data or 'contract_name' not in data:
        return jsonify({"error": "Invalid input. Please provide 'contract_code' and 'contract_name'."}), 400

    contract_code = data['contract_code']
    contract_name = data['contract_name']
    
    # Here, you would call your vulnerability analysis tool, e.g., Mythril or Slither
    findings = run_analysis_tool(contract_code)  # Placeholder for actual analysis logic
    
    # Example findings from the analysis tool (this should be dynamically generated)
    findings = {
        "findings": [
            {
                "cwe": "CWE-190",
                "description": "Integer overflow/underflow vulnerability detected.",
                "mitre": "T1518",
                "suggestion": "Use SafeMath library to prevent overflows and underflows.",
                "vulnerability": "integer_overflow"
            },
            {
                "description": "Warning: Return value of low-level calls not used.",
                "vulnerability": "unchecked_low_level_calls"
            },
            {
                "description": "Warning: SPDX license identifier not provided.",
                "vulnerability": "general_warning"
            }
        ]
    }

    # Extract features from the findings
    features, suggestions = extract_features_from_findings(findings)

    # Here, you can also perform predictions with your model if needed
    # prediction = model.predict([features])  # Use your model for predictions

    # Prepare the output JSON response
    response = {
        "contract_name": contract_name,
        "findings": findings,
        "features": features,
        "suggestions": suggestions,
        # "prediction": prediction.tolist()  # Include predictions if applicable
    }

    return jsonify(response), 200


def run_analysis_tool(contract_code):
    # This is a placeholder for the actual vulnerability analysis tool.
    # Replace this with the actual call to Mythril, Slither, or another tool.
    return {
        "findings": []
    }


if __name__ == '__main__':
    app.run(debug=True)
