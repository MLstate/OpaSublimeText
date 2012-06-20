# Plugin functionalities :

1) Syntax highlighting (classic and js-like)

2) Build systems (js-like and classic via manual modification)

3) Completion based on the stdlib

4) Contextual access to the online API documentation

5) Tutorials (one for now, many are coming)


# How to install the Opa plugin ?

1) Get https://github.com/downloads/OpaOnWindowsNow/OpaSublimeText/Opa.sublime-package

2) Move it to ~/.config/sublime-text2/Installed Packages/ (linux)
or %APPDATA%\Sublime Text 2\Installed Packages\ (windows)
or <your_portable_install_path>\Sublime Text 2\Pristine Packages\ (windows)
or ~/Library/Application Support/Sublime Text 2/Installed Packages (mac)

3) Start sublime and check that menu entry [View -> Syntax -> Opa] is present
   If not verify 1) and 2) and restart sublime again and again


# How to have syntax highlight ?

File with opa extension should be colorised.
You can force the colorisation using the menu:
[View -> Syntax -> Opa]


# How to build ?

Choose a build system.
[Tools -> Build -> Build Sytem -> Opa-All]
or
[Tools -> Build -> Build Sytem -> Opa-One]

Then press F7 or go in menu [Tools -> Opa -> Build].

Opa-One will compile the file in the focused buffer.
Opa-All will compile all files in the same directory as the focus buffer.
Opa-Conf will compile the conf files in the same directory as the focus buffer.

Press F4 to naviguate in compilation error, if any.


# How to build with classic syntax ?

Edit Opa-XXX.sublime-build, and add "--parser classic" in the cmd field just after opa.


# How to run ?

Press F7 or [Tools -> Opa -> Run]
The compilation is done automatically, but there is a sync problem.
So it's safer to build before for now.


# What else ?

- [ctrl+d] or [right-click -> Opa Doc] to go on doc.opalang.org
- select some text then [ctr+d] or [right-click -> Opa Doc]
  will search the api with the selected text
- same thing with [right-click -> Opa Doc]

- completion using all stdlib entries
  e.g. write "Lfo" and choose List.fold expansion

- skeleton for langage keyword
  write "function", select the completion, then:
   - enter the function name
   - press "tab"
   - enter the function body
   - press tab
   ...

- integrated first step tutorial (write "TUTORIAL" and select the completion)

# How to install from source
Copy the content of the repo directory to a new Opa directory in
mkdir -p  ~/.config/sublime-text2/
cp -R * ~/.config/sublime-text2/

#How to build a package file
1) Install AAAPackage Dev and Package Control (sublime package)

2) Transform Opa.JSON-tmLanguage:
  -open the file
  -select build system json to tmLanguage
  -F7

3) [ctrl+p -> "Package Control: Create Package File" -> "Opa"

4) You obtain a plugin named Opa.sublime-package
