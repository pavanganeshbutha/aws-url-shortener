from flask import Flask, render_template, request, jsonify, redirect
import uuid
import boto3
import os

app = Flask(__name__)

# Configure AWS dynamo db table
dynamodb = boto3.resource("dynamodb", region_name="ap-south-1")
TABLE_NAME = "url-shortener-table"
table = dynamodb.Table(TABLE_NAME)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/shorten", methods=['POST'])
def shorten_url():
    try:
        data = request.get_json()
        original_url = data.get("url")

        if not original_url:
            return jsonify({"error": "URL is required!"}), 400

        short_code = str(uuid.uuid4())[:8]

        # Put item in dynamo DB
        table.put_item(
            Item={
                'short_code': short_code,
                "original_url": original_url
            }
        )

        short_url = request.host_url + short_code
        return jsonify({"short_url": short_url}), 201

    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred"}), 500


@app.route("/<short_code>", methods=["GET"])
def redirect_to_url(short_code):
    try:
        response = table.get_item(Key={"short_code": short_code})
        item = response.get("Item")

        if item:
            return redirect(item['original_url'])
        else:
            return jsonify({"error": "URL not found"}), 404

    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred"}), 500


if __name__ == "__main__":
    app.run(debug=True)
