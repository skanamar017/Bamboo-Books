import os
import yaml

def stats(dir):
    """Display statistics about all notes."""
    total_notes = 0
    total_tags = {}
    total_length = 0

    # Iterate through all files in the notes directory
    for filename in os.listdir(dir):
        filepath = os.path.join(dir, filename)
        if os.path.isfile(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                parts = content.split('---')
                if len(parts) < 3:
                    continue
                header = parts[1]
                body = parts[2]
                try:
                    metadata = yaml.safe_load(header)
                except yaml.YAMLError:
                    continue

                total_notes += 1
                total_length += len(body)

                tags = metadata.get('tags', [])
                for tag in tags:
                    total_tags[tag] = total_tags.get(tag, 0) + 1

    # Print statistics
    print(f"Total notes: {total_notes}")
    avg_length = total_length / total_notes if total_notes > 0 else 0
    print(f"Average length of notes: {avg_length:.2f}")
    print("Tag frequencies:")
    for tag, count in total_tags.items():
        print(f"  {tag}: {count}")

# Run the stats function
stats()

