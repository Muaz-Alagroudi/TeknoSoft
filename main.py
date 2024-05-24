import re
from Palbot import Palbot

from flask import Flask, render_template, request,session
# Download necessary NLTK data
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

app = Flask(__name__)
bot = Palbot()

app.secret_key = 'your_secret_key'

# Adding rules with lemmantized patterns
bot.add_rule(re.compile(r'\bname\b', re.I), "My name is PalBot, and im ready to answer your questions")
bot.add_rule(re.compile(r'\bwhat\b.*\bai\b|\bpurpose\b', re.I), "AI can perform tasks that typically require human intelligence, such as problem solving, natural language processing, and image recognition.")
bot.add_rule(re.compile(r'\buse\b', re.I), "Chatbots are used for customer service, information retrieval, task automation, and entertainment purposes.")
bot.add_rule(re.compile(r'\bhow\b.*\bwork\b', re.I), "Chatbots work by using natural language processing algorithms to understand user input and generate appropriate responses.")
bot.add_rule(re.compile(r'\blearn\b', re.I), "AI can learn from data through techniques such as machine learning and deep learning, where algorithms are trained on large datasets to improve their performance.")
bot.add_rule(re.compile(r'\bemotion(?:s)\b|\bfeel\b', re.I), "AI does not have emotions or consciousness. It operates based on algorithms and data, without subjective experiences.")
bot.add_rule(re.compile(r'\bappl(?:y|ication(?:s))\b', re.I), "AI is applied in various industries such as healthcare, finance, education, and agriculture, to solve complex problems and improve decision-making.")
bot.add_rule(re.compile(r'\bcreator\b'), "Created by Muaz Alagroudi for the Teknosoft internship, contact me here! malagroudi@gmail.com")
bot.add_rule(re.compile(r'\bcreate\b'), "Created by Muaz Alagroudi for the Teknosoft internship, contact me here! malagroudi@gmail.com")
bot.add_rule(re.compile(r'\badvantage\b.+\bchatbot\b|\bbot\b', re.I), "Chatbots can provide 24/7 customer support, reduce response times, handle multiple inquiries simultaneously, and improve user satisfaction.")
bot.add_rule(re.compile(r'\bevaluate\b', re.I), "AI models are evaluated based on metrics such as accuracy, precision, recall, F1-score, and area under the ROC curve, depending on the specific task and dataset.")
bot.add_rule(re.compile(r'\bhelp\b'), "Ask about: name, purpose, what is it used for, how it works, how it ai learns, emotions or feelings, applications, advantages of chatbots, evaluations, and who created this bot")
bot.add_rule(re.compile(r'\bbye\b|\bexit\b|\bgoodbye\b'), "Goodbye! Have a great day!")

# for terminal testing
def chat():
    # print("Hello, I am Palbot! and I am ready to answer a few questions related to AI and Chatbots")
    while True:
        user_input = input("You: ")
        response = bot.get_response(user_input)
        print(f"Bot: {response}")
        if re.match(r'\bbye\b|\bexit\b', user_input, re.I):
            break

# message_history = []
@app.route("/", methods=["POST", 'GET'])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        user_message = {"type": "user", "content": user_input}
        bot_response = bot.get_response(user_input)
        bot_message = {"type": "bot", "content": bot_response}
        
        # Store user and bot messages in session
        message_history = session.get('message_history', [])
        message_history.append(user_message)
        message_history.append(bot_message)
        session['message_history'] = message_history
    
    elif request.method == "GET":
        # Clear message history if the user refreshes the page
        session.pop('message_history', None)
    
    # Retrieve message history from session
    message_history = session.get('message_history', [])
    
    return render_template("index.html", message_history=message_history)


if __name__ == "__main__":
    app.run(debug=True)

