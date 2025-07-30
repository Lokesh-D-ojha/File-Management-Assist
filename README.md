# File Organizer 📁

A simple Python script that automatically organizes your files into folders based on their type. Perfect for cleaning up messy Downloads folders, Desktop, or any directory with mixed file types.

## Features ✨

- **Automatic Organization**: Sorts files by type into organized folders
- **Safe Operation**: Moves files without deleting anything
- **Conflict Handling**: Automatically renames files if duplicates exist
- **Progress Tracking**: Shows what's being organized in real-time
- **Cross-Platform**: Works on Windows, Mac, and Linux

## Supported File Types 📄

| Category | Extensions |
|----------|------------|
| **Images** | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp`, `.ico` |
| **Documents** | `.pdf`, `.doc`, `.docx`, `.txt`, `.rtf`, `.xls`, `.xlsx`, `.ppt`, `.pptx` |
| **Videos** | `.mp4`, `.avi`, `.mkv`, `.mov`, `.wmv`, `.flv`, `.webm` |
| **Audio** | `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`, `.m4a` |
| **Archives** | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2` |
| **Code** | `.py`, `.js`, `.html`, `.css`, `.cpp`, `.java`, `.php`, `.rb` |
| **Others** | Any file type not listed above |

## Installation 🚀

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/file-organizer.git
   cd file-organizer
   ```

2. **No additional dependencies required** - uses only Python standard library!

## Usage 💻

### Basic Usage

Navigate to the folder you want to organize and run:

```bash
python file_organizer.py
```

### Organize Specific Folder

Edit the script and modify the last line:

```python
# For Windows
organize_files("C:/Users/YourName/Downloads")

# For Mac
organize_files("/Users/YourName/Downloads")

# For Linux
organize_files("/home/username/Downloads")
```

## Example 📋

**Before:**
```
Downloads/
├── report.pdf
├── vacation.jpg
├── song.mp3
├── movie.mp4
├── document.docx
└── archive.zip
```

**After:**
```
Downloads/
├── Documents/
│   ├── report.pdf
│   └── document.docx
├── Images/
│   └── vacation.jpg
├── Audio/
│   └── song.mp3
├── Videos/
│   └── movie.mp4
└── Archives/
    └── archive.zip
```

## Sample Output 📊

```
Organizing files in: /Users/username/Downloads
--------------------------------------------------
Moved: report.pdf -> Documents/
Moved: vacation.jpg -> Images/
Moved: song.mp3 -> Audio/
Moved: movie.mp4 -> Videos/
Moved: document.docx -> Documents/
Moved: archive.zip -> Archives/

==================================================
ORGANIZATION COMPLETE!
==================================================
Total files organized: 6

Documents: 2 files
Images: 1 files
Audio: 1 files
Videos: 1 files
Archives: 1 files

Done! Check your organized folders.
```

## Customization 🛠️

### Adding New File Types

Edit the `file_types` dictionary in the script:

```python
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.ico', '.tiff'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.xls', '.xlsx', '.ppt', '.pptx'],
    # Add your custom categories here
    'Design': ['.psd', '.ai', '.sketch', '.figma'],
    'Data': ['.csv', '.json', '.xml', '.sql'],
}
```

### Creating Custom Categories

You can easily add new categories for specific file types:

```python
'Fonts': ['.ttf', '.otf', '.woff', '.woff2'],
'Ebooks': ['.epub', '.mobi', '.azw3', '.fb2'],
'CAD': ['.dwg', '.dxf', '.step', '.iges'],
```

## Requirements 📋

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Safety Features 🛡️

- **Non-destructive**: Files are moved, not deleted
- **Conflict resolution**: Automatically handles duplicate file names
- **Error handling**: Continues processing even if individual files fail
- **Existing folder check**: Won't overwrite existing organized folders

## Contributing 🤝

Contributions are welcome! Here are some ways you can help:

1. **Report bugs** - Open an issue if you find any problems
2. **Suggest features** - Ideas for new functionality
3. **Add file types** - Submit PRs to support more file extensions
4. **Improve documentation** - Help make the README clearer

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Submit a pull request


## Author 👨‍💻

Created by [Lokesh Datta Ojha](https://github.com/Lokesh-D-ojha)

## Support 💬

If you found this helpful, please ⭐ star this repository!

**Happy organizing! 🎉**
