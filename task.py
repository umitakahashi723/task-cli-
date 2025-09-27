#!/usr/bin/env python3
import sys, json, os
from datetime import datetime

FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    tasks = json.load(open(FILE))
    # 给老任务补默认值
    for t in tasks:
        t.setdefault("priority", "medium")
        t.setdefault("time", "unknown")
    return tasks

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
        title, priority = " ".join(args), "medium"
        if "-p" in args:
            idx = args.index("-p")
            priority = args[idx+1]
            title = " ".join(args[:idx])
        tasks.append({"id": len(tasks)+1, "title": title,
                      "done": False, "priority": priority,
                      "time": str(datetime.now())[:16]})
        save_tasks(tasks)
        print(color(f"Added: {title} [{priority}]", "green"))

    elif cmd == "list":
        prio_color = {"high": "red", "medium": "yellow", "low": "blue"}
        if not tasks:
            print(color("No tasks yet.", "yellow"))
        for t in tasks:
            status = color("✓", "green") if t["done"] else color("✗", "red")
            p_color = prio_color.get(t["priority"], "white")
            print(f"{t['id']:>2}. {status}  {color(t['priority'], p_color)}  {t['title']}  {color(t['time'], 'blue')}")

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
