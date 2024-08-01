from flask import Flask, request, jsonify
import os
from together import Together

app = Flask(__name__)

# Initialisation du client Together
client = Together(api_key=os.environ.get('TOGETHER_API_KEY'))

@app.route('/', methods=['GET'])
def ask():
    # Récupérer la question depuis le paramètre 'ask' au lieu de 'question'
    question = request.args.get('ask', default='What are some fun things to do in New York?', type=str)
    
    # Faire la requête au modèle avec la question fournie
    response = client.chat.completions.create(
        model="Snowflake/snowflake-arctic-instruct",
        messages=[{"role": "user", "content": question}],
    )
    
    # Renvoyer la réponse en format JSON
    return jsonify(response.choices[0].message.content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
