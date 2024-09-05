import os

# Define the directory and file structure
structure = {
    "backend": {
        "app.py": "",
        "skills": {
            "__init__.py": "",
            "email_skill.py": "",
            "calendar_skill.py": "",
        },
        "models": {
            "nlu_model.py": "",
            "train_nlu.py": "",
        },
        "utils": {
            "speech_recognition.py": "",
            "text_to_speech.py": "",
        },
        # requirements.txt already exists, so this won't be overwritten
    },
    "web": {
        "client": {
            "public": {},
            "src": {
                "App.js": "",
                "index.js": "",
                "components": {},
            },
            "package.json": "",
        },
        "server": {
            "models": {
                "User.js": "",
                "Skill.js": "",
            },
            "routes": {
                "users.js": "",
                "skills.js": "",
            },
            "server.js": "",
            "package.json": "",
        },
    }
}

# Function to create directories and files recursively
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            # Create directory
            os.makedirs(path, exist_ok=True)
            # Recursively create subdirectories and files
            create_structure(path, content)
        else:
            # Create file with optional initial content
            with open(path, 'w') as f:
                f.write(content)

# Create the directory structure
create_structure('.', structure)

print("Project structure created successfully.")
