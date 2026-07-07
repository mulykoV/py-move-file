import os


def move_file(command: str) -> None:
    parts = command.split()
    source = parts[1]
    destination = parts[2]

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    dest_dir = os.path.dirname(destination)

    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(source, "r") as source_file:
        content = source_file.read()

    with open(destination, "w") as destination_file:
        destination_file.write(content)

    os.remove(source)
