from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
from torchvision import transforms
from PIL import Image
import io

app = Flask(__name__)
CORS(app)  # autorise les requêtes depuis Laravel/Vue.js

# ── Configuration ──────────────────────────────────────────
CLASSES = ["cataract", "diabetic_retinopathy", "glaucoma", "normal"]
MODEL_PATH = r"C:\Users\menga\PycharmProjects\PythonProjecteffectif\outputs\checkpoints\model_scripted.pt"
device = torch.device("cpu")

# ── Charger le modèle ──────────────────────────────────────
model = torch.jit.load(MODEL_PATH, map_location=device)
model.eval()
print("Modèle chargé ✅")

# ── Transformation de l'image ──────────────────────────────
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# ── Route de test ──────────────────────────────────────────
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "ok", "message": "API Flask opérationnelle ✅"})

# ── Route principale : diagnostic ──────────────────────────
@app.route('/predict', methods=['POST'])
def predict():
    # Vérifier qu'une image est envoyée
    if 'image' not in request.files:
        return jsonify({"error": "Aucune image reçue"}), 400

    file = request.files['image']

    # Vérifier le format
    if file.filename == '':
        return jsonify({"error": "Fichier vide"}), 400

    try:
        # Lire et prétraiter l'image
        img_bytes = file.read()
        image = Image.open(io.BytesIO(img_bytes)).convert("RGB")
        tensor = transform(image).unsqueeze(0).to(device)  # (1, 3, 224, 224)

        # Prédiction
        with torch.no_grad():
            outputs = model(tensor)
            probs   = torch.softmax(outputs, dim=1)[0]
            pred_idx = probs.argmax().item()

        # Résultat
        result = {
            "diagnostic": CLASSES[pred_idx],
            "confidence": round(probs[pred_idx].item() * 100, 2),
            "probabilites": {
                CLASSES[i]: round(probs[i].item() * 100, 2)
                for i in range(len(CLASSES))
            }
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ── Lancer l'API ───────────────────────────────────────────
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)