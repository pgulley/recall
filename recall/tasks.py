from invoke import task, Collection, Program
import json
import os
import subprocess

COMMANDS_FILE = os.path.expanduser("~/.command_registry_invoke.json")

def load_commands():
    if os.path.exists(COMMANDS_FILE):
        with open(COMMANDS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_commands(commands):
    with open(COMMANDS_FILE, 'w') as file:
        json.dump(commands, file, indent=4)

def get_last_command():
    """
    Retrieve the last command from shell history.
    """
    try:
        # Use `fc` to fetch the last command (works in bash/zsh)
        result = os.getenv("LAST_COMMAND")
        print(result)
        return result
    except Exception as e:
        print(f"Error retrieving last command: {e}")
        return None

@task
def save(c, name, command=None, last=False):
    """
    Save a shell command with a given name.
    Use --last to save the most recently run command.
    """
    if last:
        command = get_last_command()
        if not command:
            print("Unable to retrieve the last command.")
            return

    if not command:
        print("You must provide a command or use --last to save the most recent command.")
        return

    commands = load_commands()
    commands[name] = command
    save_commands(commands)
    print(f"Saved command '{name}': {command}")


@task
def run(c, name):
    """
    Run a saved shell command by name.
    """
    commands = load_commands()
    if name in commands:
        command = commands[name]
        print(f"Running command '{name}': {command}")
        c.run(command, pty=True)
    else:
        print(f"No command found with name '{name}'")

@task
def list_(c):
    """
    List all saved commands.
    """
    commands = load_commands()
    if commands:
        print("Saved commands:")
        for name, command in commands.items():
            print(f"  {name}: {command}")
    else:
        print("No commands saved.")


ns = Collection()
ns.add_task(list_, name="list")
ns.add_task(save, name="save")
ns.add_task(run, name="run")

def main():
    program = Program(namespace=ns)  # Or pass your custom namespace
    program.run()