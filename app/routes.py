from flask import Blueprint, render_template, request
import requests
from .config import Config

main = Blueprint("main", __name__)

# Corrigidas as categorias para os nomes corretos
CATEGORIAS = {
    "geral": "general",
    "esportes": "sports",
    "negócios": "business",
    "tecnologia": "technology",
    "entretenimento": "entertainment",
    "saúde": "health",
    "ciência": "science"
}

@main.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        categoria = request.form.get("categoria", "geral").lower()
    else:
        categoria = request.args.get("categoria", "geral").lower()

    # Garante que a categoria é válida
    categoria_api = CATEGORIAS.get(categoria, "general")

    url = f"https://gnews.io/api/v4/top-headlines?category={categoria_api}&lang=pt&country=br&apikey={Config.NEWS_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        noticias = response.json().get("articles", [])
    else:
        noticias = []
    
    return render_template(
        "index.html",
        noticias=noticias,
        categoria_atual=categoria,
        categorias=CATEGORIAS.keys()  # Passa apenas os nomes das categorias
    )
