from flask import Flask, request, render_template
import config
import openai

openai.api_key = config.API_KEY
app = Flask(__name__)

@app.route("/")
def index():
    # return "Hello, World!"
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"{userText}"},],
        max_tokens=1024,
        n=1,
        stop=None, 
        temperature=1,
    )
    
    answer = "".join(response.choices[0].message.content.strip())
    return answer


if __name__ == "__main__":
    app.run()