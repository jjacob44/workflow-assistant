from pydantic_ai import Agent
from tools.notes import NotesTool
from pathlib import Path

def main():
    project_root = Path(__file__).resolve().parent
    notes_dir = project_root / "notes"
    notes_tool = NotesTool(notes_dir)
    agent = Agent(
        model='openai:gpt-5-mini',
        tools=[notes_tool.list_notes, notes_tool.read_note, notes_tool.search_notes],
        instructions='You are an AI workflow assistant. Use the available tools when the user asks about notes. Do not invent note contents. If no relevant note is found, say so clearly. Keep responses concise and useful.'
    )

    results = agent.run_sync('Which notes do I have?')
    print(results)
    
if __name__ == '__main__':
    main()