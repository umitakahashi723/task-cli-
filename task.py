#!/usr/bin/env python3
import sys, json, os
from datetime import datetime

FILE = "tasks.json"

def load_tasks():
    return json.load(open(FILE)) if os.path.exists(FILE) else []

def save_tasks(tasks):
    json.dump(tasks, open(FILE, "w"), indent=2, ensure_ascii=False)

def color(text, c):
    colors = {"red": 31, "green": 32, "yellow": 33, "blue": 34}
    return f"\033[{colors[c]}m{text}\033[0m"

def main():
    if len(sys.argv) == 1:
        print(color("Usage: task <command> [args]", "yellow"))
        print("Commands: add, list, done <id>, delete <id>, clear")
        return

    cmd, *args = sys.argv[1:]
    tasks = load_tasks()

    if cmd == "add":
        title = " ".join(args)
        tasks.append({"id": len(tasks)+1, "title": title, "done": False, "time": str(datetime.now())[:16]})
        save_tasks(tasks)
        print(color(f"Added: {title}", "green"))

    elif cmd == "list":
        if not tasks:
            print(color("No tasks yet.", "yellow"))
        for t in tasks:
            status = color("✓", "green") if t["done"] else color("✗", "red")
            print(f"{t['id']:>2}. {status}  {t['title']}  {color(t['time'], 'blue')}")

    elif cmd == "done":
        tid = int(args[0])
        for t in tasks:
            if t["id"] == tid:
                t["done"] = True
                print(color(f"Task {tid} marked done.", "green"))
        save_tasks(tasks)

    elif cmd == "delete":
        tid = int(args[0])
        tasks = [t for t in tasks if t["id"] != tid]
        save_tasks(tasks)
        print(color(f"Task {tid} deleted.", "red"))

    elif cmd == "clear":
        save_tasks([])
        print(color("All tasks cleared.", "yellow"))

    else:
        print(color("Unknown command.", "red"))

if __name__ == "__main__":
    main()
