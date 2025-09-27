#!/usr/bin/env python3
import sys, json, os

FILE = "tasks.json"

def load_tasks():
    return json.load(open(FILE)) if os.path.exists(FILE) else []

def save_tasks(tasks):
    json.dump(tasks, open(FILE, "w"), indent=2, ensure_ascii=False)

def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "add":
        tasks = load_tasks()
        tasks.append({"id": len(tasks)+1, "title": sys.argv[2], "done": False})
        save_tasks(tasks)
        print(f"Added: {sys.argv[2]}")
    elif cmd == "list":
        for t in load_tasks():
            print(f"{t['id']}. [{'x' if t['done'] else ' '}] {t['title']}")
    else:
        print("Usage: python task.py add|list")

if __name__ == "__main__":
    main()
