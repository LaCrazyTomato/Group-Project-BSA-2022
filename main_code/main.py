from flask import Flask, jsonify
from flask import render_template, request

from google.cloud import aiplatform
from google.cloud.aiplatform.gapic.schema import predict
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value
import os

app = Flask(__name__)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "balmy-doodad-342313-8cdc1f171d37.json"  # fichier avec les clés

#
# Project of group Group Tesla
#   Mickaël Gandoulf, Timothée Pouly, Olivier Halkin
# Big Scale Analytics Class
# Prof. Vlachos
#

def predict_text_classification_single_label_sample(
        project: str,
        endpoint_id: str,
        content: str,
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
):
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)
    instance = predict.instance.TextClassificationPredictionInstance(
        content=content,
    ).to_value()
    instances = [instance]
    parameters_dict = {}
    parameters = json_format.ParseDict(parameters_dict, Value())
    endpoint = client.endpoint_path(
        project=project, location=location, endpoint=endpoint_id
    )
    response = client.predict(
        endpoint=endpoint, instances=instances, parameters=parameters
    )

    predictions = response.predictions

    # for prediction in predictions:
    # return dict(prediction)

    return dict(predictions[0])


# Routing POST
@app.route("/predict", methods=['POST'])
def predict_text():
    # data to connect API
    predictions = predict_text_classification_single_label_sample(
        project="642567623456",
        endpoint_id="2143687034349289472",
        location="us-central1",
        content=request.values.get('text')
    )

    label_ordered = ["A1", "A2", "B1", "B2", "C1", "C2"]
    confidences = []
    google_confidences = list(predictions["confidences"])
    google_labels = list(predictions["displayNames"])

    for label in label_ordered:
        label_index = google_labels.index(label)
        confidences.append(google_confidences[label_index])

    # Making a dic to easier display the data in the tab
    dic = {label: confidence for label, confidence in zip(label_ordered, confidences)}

    # Formatting the JSON (+adding dico)
    return jsonify({"displayNames": label_ordered,
                    "confidences": confidences, "dic":[dic]})


# Routing GET
@app.route("/", methods=['GET'])
def home(name=None):
    return render_template('index.html', name=name)


# Port
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
