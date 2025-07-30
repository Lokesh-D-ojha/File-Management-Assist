import os
import shutil
from pathlib import Path


def organize_files(folder_path=None):
    """Organize files in the specified folder (or current folder if none specified)"""

    # Use current directory if no path specified
    if folder_path is None:
        folder_path = os.getcwd()

    target_dir = Path(folder_path)

    # File type mappings
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.ico'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
        'Code': ['.py', '.js', '.html', '.css', '.cpp', '.java', '.php', '.rb'],
        'Others': []  # For unmatched files
    }

    # Create folders
    print(f"Organizing files in: {target_dir}")
    print("-" * 50)

    for folder_name in file_types.keys():
        folder_path = target_dir / folder_name
        folder_path.mkdir(exist_ok=True)

    # Count organized files
    organized_count = {folder: 0 for folder in file_types.keys()}

    # Get all files in the directory
    files = [f for f in target_dir.iterdir() if f.is_file()]

    # Organize each file
    for file_path in files:
        file_extension = file_path.suffix.lower()
        file_moved = False

        # Find matching category
        for category, extensions in file_types.items():
            if category == 'Others':
                continue

            if file_extension in extensions:
                destination_folder = target_dir / category
                destination_path = destination_folder / file_path.name

                # Handle name conflicts
                counter = 1
                original_destination = destination_path
                while destination_path.exists():
                    stem = original_destination.stem
                    suffix = original_destination.suffix
                    destination_path = destination_folder / f"{stem}_{counter}{suffix}"
                    counter += 1

                try:
                    shutil.move(str(file_path), str(destination_path))
                    print(f"Moved: {file_path.name} -> {category}/")
                    organized_count[category] += 1
                    file_moved = True
                    break
                except Exception as e:
                    print(f"Error moving {file_path.name}: {e}")

        # Move to Others if no category matched
        if not file_moved:
            destination_folder = target_dir / 'Others'
            destination_path = destination_folder / file_path.name

            # Handle name conflicts
            counter = 1
            original_destination = destination_path
            while destination_path.exists():
                stem = original_destination.stem
                suffix = original_destination.suffix
                destination_path = destination_folder / f"{stem}_{counter}{suffix}"
                counter += 1

            try:
                shutil.move(str(file_path), str(destination_path))
                print(f"Moved: {file_path.name} -> Others/")
                organized_count['Others'] += 1
            except Exception as e:
                print(f"Error moving {file_path.name}: {e}")

    # Show summary
    print("\n" + "=" * 50)
    print("ORGANIZATION COMPLETE!")
    print("=" * 50)

    total_files = sum(organized_count.values())
    print(f"Total files organized: {total_files}")
    print()

    for category, count in organized_count.items():
        if count > 0:
            print(f"{category}: {count} files")

    print("\nDone! Check your organized folders.")


# Run the organizer
if __name__ == "__main__":
    # You can specify a folder path here, or leave empty for current folder
    organize_files()  # Organizes current folder
    # organize_files("C:/Users/YourName/Downloads")  # Or specify a path
