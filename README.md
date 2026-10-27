# Offline Reference Library

Set up an offline reference library of PDF files that you can sync with a website and search using [Recoll](https://www.recoll.org/).

## Sample .env file

```
BOOKS_DIR=~/reference_library
SERVER_DIR=yourserver.com:~/www/reference-library
```

## Installation

### Mac

1. Download Skim PDF reader from https://skim-app.sourceforge.io/
1. Download .dmg file from https://www.recoll.org/downloads/macos/
1. Open Recoll
1. Preferences > GUI Configuration... > Choose editor applications
1. Select application/pdf
1. Enable New Values: > Exception to Desktop preferences
1. In Action (empty -> recoll default) input, write `open "skim:///%f#page=%p"`
1. Click Apply to current selection
1. Open `~/.recoll/recoll.conf` and add this line[^1]:
   ```
   recollhelperpath = /opt/homebrew/bin
   ```

[^1]: Recoll for Mac can't index PDFs by default because the `pdftotext` binary that it ships with expects `libfreetype` to be in `/usr/local/opt/freetype/lib`, which is not the case if you use homebrew.

### Linux

TBD

## Sync

1. Publish all books to your website by running `just publish`
1. Go to another computer
1. Visit the website at, say, https://yourserver.com/reference-library
1. Open a terminal and run the download command, adjusting the value of `--directory-prefix` as needed
