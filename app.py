from flask import Flask, render_template

# Inicializa a aplicação Flask
app = Flask(__name__, template_folder='.', static_folder='.', static_url_path='')

@app.route('/')
def home():
    """Rota principal que serve a página index.html."""
    return render_template('index.html')

if __name__ == '__main__':
    # Roda o servidor local em modo de desenvolvimento na porta 5000
    app.run(debug=True, port=5000)
    