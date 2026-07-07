from pathlib import Path

class NotesTool:
    def __init__(self, notes_dir):
        self.notes_dir = Path(notes_dir)

    def list_notes(self):
        return {'success': True, 'content': [note.name for note in self.notes_dir.glob("*.md")]}
    
    def read_note(self, note_name):
        note_path = self.notes_dir / note_name

        if not note_path.exists():
            return {
                'success': False,
                'error': f'Error: the file {note_name} is not found'
            }

        try:
            content = note_path.read_text(encoding="utf-8")
            return {'success': True, 'content': content}
        except PermissionError:
            return {
                'success': False,
                'error': 'You do not have permission to read this file'
            }
        
        
    def search_notes(self, substring):
        list_of_files_containing_substring = []

        for note in self.notes_dir.glob("*.md"):
            # Read everything into memory
            content = note.read_text(encoding="utf-8")

            # Check for substring (case-sensitive)
            if substring in content:
                list_of_files_containing_substring.append(note.name)

        return {'success': True, 'content': list_of_files_containing_substring}
              