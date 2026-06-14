from flask import Flask, render_template, request, send_file
from converter.markdown_converter import MarkdownConverter
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        if "mdfile" not in request.files:
            return "No file received"

        file = request.files["mdfile"]

        if file.filename == "":
            return "No file selected"

        if not file.filename.endswith(".md"):
            return "Only .md files allowed"

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(input_path)

        with open(input_path, "r", encoding="utf-8") as f:
            md_text = f.read()

        converter = MarkdownConverter(md_text)
        html_content = converter.convert()

        output_file = file.filename.replace(".md", ".html")
        output_path = os.path.join(OUTPUT_FOLDER, output_file)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        return render_template(
            "result.html",
            html=html_content,
            filename=output_file
        )

    return render_template("index.html")


@app.route("/download/<filename>")
def download(filename):
    return send_file(
        os.path.join(OUTPUT_FOLDER, filename),
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)
