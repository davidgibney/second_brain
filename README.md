# second_brain

my "second brain" (public)

## Introduction

I read a blog post titled "How to build a second brain as a software developer."

This repo is my implementation of that post's ideas.

Purpose and intent:

- Keep two repos: 'second_brain' (public repo) and '_second_brain' (private repo).
- Use the private repo for keeping notes.
- Copy from the private repo to the public repo for whatever you want to publish to the world.
- Either way, this can be used for all note taking and to establish a personal wiki system. Adding input is easy since you have options: use any favorite editor (VS Code, vim, sublime-text, etc). Viewing is easy since--again--you have options: open files/folders in a web browser, or use any markdown viewer app, etc.
- Enjoy having the "best of two worlds" if you go with using markdown files: you can enjoy plain text and formatted text.
- Search is easy with common Linux tools like `grep` or `find` (searching locally), or even with the github website search feature.
- You can link to other "pages" like you would in a real wiki system. Just link to other files as you would in markdown syntax.

Suggested top-level directories to use:

- inbox
- projects
- areas
- resources
- archives

Tips:

- Use 'split-pane view' in VS Code to simultaneously see the markdown "code" as well as the rendered view so you can live-preview as you work on your documents. Bear (an app) is another good choice for drafting.
- Another efficient workflow is to edit in vim and then easily launch viewer apps against your files right from the shell.
- Easily export to other formats or wiki systems: markdown is easy to export to PDF or MS Word for example. There are many tools to help you do this. And you can also simply copy+paste the rendered markdown into other places (e.g., Confluence) and the content and formatting will all copy over.
- Use "tags" by simply putting keywords in your files as appropriate. `grep` will find them.
- Be liberal in your usage of this system. Write or copy as many things as you want into the repo. The point is to have a central for information and which facilitates organization and quick-lookup.

## tk ToDo

write a script to regularly export browser bookmarks into the repo? (another backup for bookmarks).

write a script to sync notes with Apple Notes or Google Docs?

write a script to audit the inodes to see what files haven’t been accessed in the past 12 months? and then auto suggest to move them to the `archive` directory?

## Related

<https://aseemthakar.com/how-to-build-a-second-brain-as-a-software-developer/>
