# Assignment 21

This folder contains two subfolders, named 1 and 2, each containing Python scripts for different projects.

## Project 1: Music Synthesizer

### Folder Structure:
- **Folder 1:**
  - main.py: Python script for generating a music synthesizer output.

#### Description:
The main.py script in Folder 1 utilizes the pysynth library to generate a musical composition. It defines a sequence of notes and their durations and then generates a corresponding WAV file.

#### Usage:
1. Ensure you have Python installed on your system.
2. Install the pysynth library using pip: `pip install pysynth`.
3. Run the main.py script to generate the music synthesizer output.

```python
import pysynth as ps

notes = [("c", 4), ("c", 4), ("g", 4), ("g", 4),
         ("a", 4), ("a", 4), ("g", 2),
         ("f", 4), ("f", 4), ("e", 4), ("e", 4),
         ("d", 4), ("d", 4), ("c", 2),
         ("g", 4), ("g", 4), ("f", 4), ("f", 4),
         ("e", 4), ("e", 4), ("d", 2),
         ("g", 4), ("g", 4), ("f", 4), ("f", 4),
         ("e", 4), ("e", 4), ("d", 2),
         ("c", 4), ("c", 4), ("g", 4), ("g", 4),
         ("a", 4), ("a", 4), ("g", 2),
         ("f", 4), ("f", 4), ("e", 4), ("e", 4),
         ("d", 4), ("d", 4), ("c", 2)]

ps.make_wav(notes, fn="test.wav")
```
Output Music:
------------

- [Download Music](./1/test.wav)


<br>

Project 2: Media Management System
----------------------------------

### Folder Structure:

*   **Folder 2:**
    *   actor.py: Python script defining the Actor class.
    *   clip.py: Python script defining the Clip class.
    *   documentary.py: Python script defining the Documentary class.
    *   film.py: Python script defining the Film class.
    *   media.py: Python script defining the Media class.
    *   series.py: Python script defining the Series class.
    *   main.py: Python script for managing media data and storing it in a SQLite database.

#### Description:

Folder 2 contains a collection of Python scripts for managing various types of media such as films, documentaries, series, and clips. The main functionality is implemented in the main.py script, which interacts with a SQLite database to store and retrieve media information.

#### Usage:

1.  Ensure you have Python installed on your system.
2.  Install the required dependencies:
    *   pytube: `pip install pytube`.
3.  Run the main.py script to manage media data. The script will create and interact with a SQLite database named `media.db`.

```python
# Run main.py script
python main.py
```

Prerequisites:
--------------

*   Python 3.x
*   pysynth library
*   pytube library
*   SQLite database

