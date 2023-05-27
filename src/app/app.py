from flask import Flask, render_template, send_from_directory, request
from dotenv import load_dotenv

import hal9000

import os


load_dotenv()

app = Flask(__name__)


style_rules = [
        {
        'index': 1,
        'title ': "Active Voice",
        'text': """
        Use active voice instead of passive voice. Make clear who's performing the action.
        """
    },
    {
        'index': 2,
        'title ': "Sentence structure ",
        'text': """
        If you want to tell the reader to do something, try to mention the circumstance, conditions, or goal before you provide the instruction.
        """
    },
    {
        'index': 2,
        'title ': "Sentence structure ",
        'text': f"""{os.getenv('OPENAI_API_KEY')}"""
    },
    ]

def get_rules():
    return style_rules

@app.route('/')
def root():
    return send_from_directory('../client/dist', 'index.html')
    # return render_template('index.html', name="You")

# Path for the rest of the static files (JS/CSS)
@app.route('/<path:path>')
def assets(path):
    return send_from_directory('../client/dist', path)

@app.route('/rules', methods=['GET'])
def rules():
    rules_obj = get_rules()
    return { 'style_rules': rules_obj }

#  Create a new sticky note
@app.route('/rules', methods=['POST'])
def create_new_style_rule():
    data = request.get_json(force=True)
    text = data.get('text')

    idx = len(style_rules) + 1
    new_rule = {
        'index': idx,
        'title ': f"Sentence structure {idx}",
        'text': text
    }

    style_rules.append(new_rule)

    return new_rule

#  Delete a specific sticky note
@app.route('/rules/<index>', methods=['DELETE'])
def delete_style_rule(index):
    index = int(index)

    # remove index from style_rules
    style_rules[:] = [d for d in style_rules if d.get('index') != index]
    
    return {'deleted': index }


#  Create a new sticky note
@app.route('/critique', methods=['POST'])
def suggest_corrections():
    
    data = request.get_json(force=True)
    text = data.get('text')

    c = hal9000.correct_text('')
    print(c)

    corrected = f"Corrected: {c}"

    return {
        'suggestion': {'original_text': text, 'suggested_text': corrected}
    }


if __name__ == '__main__':
    app.run(debug=True)
