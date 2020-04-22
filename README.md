# Directory Organizer

A simple python program to organize a directory by filename. Inspired by [this reddit post](https://www.reddit.com/r/Python/comments/g4pfjj/i_made_a_python_script_that_organizes_a_folder/)

## Usage

`python3 organizer.py PATH`

path - absolute file path to directory to organize (example: `~/Pictures`)

## What Happens?

lets say you had the following structure

```
Pictures
  foo.png
  bar.png
  far.png
  baz.png
  foo.jpg
  bar.jpg
  far.jpg
  baz.jpg
  foo.gif
  bar.gif
  far.gif
  baz.gif
```

after running the program, the structure will be:

```
Pictures
  png
    foo.png
    bar.png
    far.png
    baz.png
  jpg
    foo.jpg
    bar.jpg
    far.jpg
    baz.jpg
  gif
    foo.gif
    bar.gif
    far.gif
    baz.gif
```

## Installation
```
git clone https://github.com/jonot-cyber/directory-organizer.git
cd directory-organizer
python3 organizer.py PATH
```
