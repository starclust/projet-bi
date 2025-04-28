from flask import Flask, render_template, request
from utils.data_loader import load_data
from models.clustering import apply_all_clusterings

app = Flask(__name__)

# Chargement et application des clusters
df = load_data()
df = apply_all_clusterings(df)

# Dictionnaire des labels HDBSCAN
labels_dict = {
    6: "Clients réguliers",
    14: "Gros clients",
    8: "Bons payeurs",
    9: "Fidèles modérés",
    11: "Clients prudents",
    10: "Clients récents",
    5: "Dépense moyenne",
    -1: "Outlier",
    13: "À surveiller",
    1: "Croissance",
    12: "Potentiel",
    0: "Stable",
    3: "Saisonniers",
    4: "Risque élevé",
    7: "Irréguliers",
    2: "Nouveaux"
}

@app.route("/", methods=["GET", "POST"])
def index():
    cluster_result = None
    if request.method == "POST":
        client_id = request.form.get("client_id")
        try:
            client_id = int(client_id)
            row = df[df["code_client"] == client_id]

            if not row.empty:
                hdbscan_label = int(row["cluster_hdbscan"].values[0])
                hdbscan_label_name = labels_dict.get(hdbscan_label, "Inconnu")

                cluster_result = f"""
                🔹 <strong>HDBSCAN :</strong> {hdbscan_label_name} (Cluster {hdbscan_label}).<br>
                &nbsp;&nbsp;&nbsp;&nbsp;👉 {("Ce client est considéré comme un 'Outlier'." if hdbscan_label == -1 else "Client classifié avec HDBSCAN.")}
                """
            else:
                cluster_result = f"Client ID {client_id} non trouvé."

        except ValueError:
            cluster_result = "ID client invalide."

    return render_template("index.html", cluster_result=cluster_result)

if __name__ == "__main__":
    app.run(debug=True)
