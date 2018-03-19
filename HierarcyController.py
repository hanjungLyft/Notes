from flask import Flask, jsonify, request
from venv.ObjectModel.note import Note
from venv.DataAccessor.notecontext import NoteContext

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


if __name__ == "__main__":
    app.run()