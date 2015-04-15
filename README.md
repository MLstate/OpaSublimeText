**This is the Opa plugin for Sublime Text 2/3**

- Opa: http://opalang.org
- Sublime Text: http://www.sublimetext.com/

# Plugin Features

1. Syntax highlighting
2. Build system
3. Code completion
4. Contextual access to the online API documentation
5. Tutorials (one for now)

# How to install the Opa plugin ?

1. Download the [package](https://github.com/downloads/MLstate/OpaSublimeText/Opa.sublime-package)
2. Move it to `~/.config/sublime-text(2)/Installed Packages/` (linux)
or `%APPDATA%\Sublime Text( 2)\Installed Packages\` (windows)
or `~/Library/Application Support/Sublime Text( 2)/Installed Packages` (mac)
3. Start sublime and check that menu entry [View -> Syntax -> Opa] is present. If not verify 1) and 2) and restart sublime again and again.

# How to have syntax highlighting?

Files with `.opa` extension should automatically get syntax highlighting. If not, please make sure you are using the Opa plugin [View -> Syntax -> Opa].

# How to build my application?

Choose a build system:

- [Tools -> Build -> Build System -> Opa-All] builds all Opa files in the current directory
- [Tools -> Build -> Build System -> Opa-One] builds the single Opa source code you are editing
- [Tools -> Build -> Build System -> Opa-Conf] uses opa conf files from the current directory.

Then press `F7` or launch from the menu [Tools -> Opa -> Build].
If there are compilation errors such as parsing or typing errors, you can navigate between them using `F4`.

# FAQ

## Can I use the classic Opa syntax?
Yes, the Opa plugin also supports the classic syntax of Opa. Edit `Opa-XXX.sublime-build`, and add `--parser classic` in the cmd field just after opa.

## How to run my application?

Press `F7` or [Tools -> Opa -> Run]
The compilation is done automatically, but there is a sync problem awaiting a fix.
So it's safer to build before for now.

# Other Features

- Hit [ctrl+d] or [right-click -> Opa Doc] to query doc.opalang.org for the highlighted word
- The Opa plugin features code completion on the Opa standard library.
  Try it, for instance by typing "Lfo" to expand to List.fold.
- The plugin also features skeletons for several Opa constructs. Try it, for instance by typing "function", select the completion, then:
   - enter the function name
   - press "tab"
   - enter the function body
   - press tab
- You can also play with the (first) tutorial by typing "TUTORIAL" and selecting the completion.

# Install from Source

Copy the content of the plugin repository to a new Opa directory in your Sublime directory.

You can build the Sublime package yourself if you want:

1. Install the AAAPackage Dev and Package Control Sublime packages
2. Transform Opa.JSON-tmLanguage:
  - Open the file
  - Select build system json to tmLanguage
  - F7
3. Hit [ctrl+p -> "Package Control: Create Package File" -> "Opa"]
4. You should have the plugin in Opa.sublime-package

# Questions, contributions

Please use GitHub Issues for bugs. You are welcome to fork and contribute Pull Requests to make the Opa plugin rock as much as possible.

Thanks!