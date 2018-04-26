from flask import Flask, jsonify, request, Response, stream_with_context
from venv.ObjectModel.note import Note
from venv.DataAccessor.notecontext import NoteContext
from venv.Storage.s3 import S3Wrapper

app = Flask(__name__)


@app.route("/")
def index():
    return "Index!"


@app.route("/notes/<id>", methods=['POST'])
def add_note(id):
    data = request.get_json()
    note = Note(id, data['name'])
    note_context = NoteContext()
    note_context.add_container(note)
    return jsonify(id=note.id)


@app.route("/notes")
def get_notes():
    note_context = NoteContext()
    notes = note_context.get_containers_by_type('note')
    return jsonify(data=notes)


@app.route("/files/upload", methods=['POST'])
def upload_file():
    data = request.get_data()
    id = S3Wrapper.put(data)
    return jsonify(id=id)


@app.route("/files/<id>/download", methods=['GET'])
def download_file(id):
    response = S3Wrapper.get(id)
    return Response(response['Body'].read())

@app.route("/files/<id>/stream", methods=['GET'])
def stream_file(id):
    response = S3Wrapper.get(id)
    def generate():
        for chunk in iter(lambda: response['Body'].read(10000), b''):
            yield chunk
    return Response(stream_with_context(generate()), content_type='application/pdf')

if __name__ == "__main__":
    app.run()