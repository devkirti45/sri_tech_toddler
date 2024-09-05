# backend/app.py

from flask import Flask, request, jsonify
from models.nlu_model import classify_intent
from skills import email_skill, calendar_skill
from utils.speech_recognition import listen
from utils.text_to_speech import speak

app = Flask(__name__)

# Initialize skills
skills = {
    'email': email_skill,
    'calendar': calendar_skill
}

@app.route('/api/voice-command', methods=['POST'])
def handle_voice_command():
    data = request.json
    text = data.get('text', '')
    intent, skill_name, params = classify_intent(text)
    
    if skill_name in skills:
        response = skills[skill_name].execute(params)
    else:
        response = {'status': 'error', 'message': 'Unknown intent.'}
    
    return jsonify(response)

@app.route('/api/skills', methods=['GET', 'POST'])
def manage_skills():
    if request.method == 'GET':
        # Return available skills
        available_skills = list(skills.keys())
        return jsonify({'skills': available_skills})
    elif request.method == 'POST':
        # Add a new skill (this is a simplified example)
        new_skill = request.json.get('skill_name')
        # You would dynamically load and add the skill here
        return jsonify({'status': 'success', 'message': f'Skill {new_skill} added.'})

if __name__ == '__main__':
    app.run(debug=True)
