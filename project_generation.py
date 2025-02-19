import os
import json

class ProjectGenerator:
    def __init__(self, base_path=None):
        if base_path is None:
            self.base_path = os.getcwd()
        else:
            self.base_path = os.path.abspath(base_path)
            os.makedirs(self.base_path, exist_ok=True)
        
        print(f"Project will be created in: {self.base_path}")

    def create_structure(self, structure):
        """Creates project structure from a dictionary representation"""
        self._create_recursive(self.base_path, structure)
        print("\nProject structure created successfully!")
        print(f"Location: {self.base_path}")

    def _create_recursive(self, current_path, structure):
        for name, content in structure.items():
            path = os.path.join(current_path, name)
            
            if isinstance(content, dict):
                # If it's a dictionary, it's a folder
                os.makedirs(path, exist_ok=True)
                print(f"Created directory: {path}")
                self._create_recursive(path, content)
            else:
                # If it's not a dictionary, it's a file
                with open(path, 'w') as f:
                    f.write(str(content))
                print(f"Created file: {path}")

    def create_from_json(self, json_file):
        """Creates project structure from a JSON file"""
        with open(json_file, 'r') as f:
            structure = json.load(f)
        self.create_structure(structure)

# Usage example
if __name__ == "__main__":
    project_structure = {
        "todo_blogger": {
            "auth-service": {
                "app.py": "# Authentication Service\nfrom flask import Flask\n\napp = Flask(__name__)\n\nif __name__ == '__main__':\n    app.run()",
                "requirements.txt": "flask==2.0.1\nrequests==2.26.0",
                "Dockerfile": "FROM python:3.9-slim\n\nWORKDIR /app\nCOPY . .\nRUN pip install -r requirements.txt\n\nCMD [\"python\", \"app.py\"]"
            },
            "todo-service": {
                "app.py": "# Todo Service\nfrom flask import Flask\n\napp = Flask(__name__)\n\nif __name__ == '__main__':\n    app.run()",
                "requirements.txt": "flask==2.0.1\nrequests==2.26.0",
                "Dockerfile": "FROM python:3.9-slim\n\nWORKDIR /app\nCOPY . .\nRUN pip install -r requirements.txt\n\nCMD [\"python\", \"app.py\"]"
            },
            "blog-service": {
                "app.py": "# Blog Service\nfrom flask import Flask\n\napp = Flask(__name__)\n\nif __name__ == '__main__':\n    app.run()",
                "requirements.txt": "flask==2.0.1\nrequests==2.26.0",
                "Dockerfile": "FROM python:3.9-slim\n\nWORKDIR /app\nCOPY . .\nRUN pip install -r requirements.txt\n\nCMD [\"python\", \"app.py\"]"
            },
            "gateway-service": {
                "app.py": "# API Gateway Service\nfrom flask import Flask\n\napp = Flask(__name__)\n\nif __name__ == '__main__':\n    app.run()",
                "requirements.txt": "flask==2.0.1\nrequests==2.26.0",
                "Dockerfile": "FROM python:3.9-slim\n\nWORKDIR /app\nCOPY . .\nRUN pip install -r requirements.txt\n\nCMD [\"python\", \"app.py\"]"
            },
            "docker-compose.yml": "version: '3'\n\nservices:\n  auth-service:\n    build: ./auth-service\n    ports:\n      - \"5001:5000\"\n\n  todo-service:\n    build: ./todo-service\n    ports:\n      - \"5002:5000\"\n\n  blog-service:\n    build: ./blog-service\n    ports:\n      - \"5003:5000\"\n\n  gateway-service:\n    build: ./gateway-service\n    ports:\n      - \"5000:5000\"\n    depends_on:\n      - auth-service\n      - todo-service\n      - blog-service"
        }
    }

    # Save the structure to a JSON file
    with open('todo_blogger_structure.json', 'w') as f:
        json.dump(project_structure, f, indent=2)

    # Create generator and generate structure
    generator = ProjectGenerator("./my_todo_app")  # This will create in a directory called "my_todo_app"
    generator.create_from_json('todo_blogger_structure.json')  # Use create_from_json instead of create_structure