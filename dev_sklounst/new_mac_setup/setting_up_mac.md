# setting_up_mac.md

My guide for setting up a new Mac(book|mini).

## Step 1

### Initial things

- Create or use an Apple ID
- Configure Mac system settings: Mouse, Trackpad, Keyboard, Accessibility, etc.
- Set keyboard stuff: key repeat, delay until repeat, keyboard hotkeys and modifier keys
- and other changes in system preferences: energy saver / screen saver, hot corners, enable filevault, ...

and,

- Update Mac OS, if an update is available
- Update apps from the Apple App store
- Install Xcode and Xcode tools
- Restart the machine

## Step 2

### Scriptable installs / setup

For these items, you can use the script `setup_new_mac.bash` or just follow these instructions.

- Disable smart quotes and dashes and all that silliness:

``` bash
for d in $(defaults domains|tr -d ,);do
  osascript -e "app id \"$d\""&>/dev/null||continue
  defaults write $d SmartQuotes -bool false
  defaults write $d SmartDashes -bool false
  defaults write $d SmartLinks -bool false
  defaults write $d SmartCopyPaste -bool false
  defaults write $d TextReplacement -bool false
  defaults write $d CheckSpellingWhileTyping -bool false
done
```

- Disable "keyboard press and hold":

```defaults write -g ApplePressAndHoldEnabled -bool false```

- Install homebrew:

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

- Install iTerm:

`brew install --cask iterm2`

If that worked, then Homebrew is working and you can move on to installing many programs at once.

*Note: some of these you may prefer to not install; or to have installed with Apple App Store or stand-alone pkg/dmg installers, as opposed to installed/managed with Homebrew. Look before you run this.*

- Install some favorite tools:

``` bash
brew install adoptopenjdk11 ansible argocd argocd-vault-plugin autoconf automake awscli azure-cli azure-storage-cpp azcopy bash bpython circleci coreutils docker-credential-helper-ecr expect gpg go gojq graphviz groovy ipython inframap jenkins-lts jenv jmeter jq kubecfg kubernetes-cli libpq libtool minikube nmap oci-cli openjdk pipenv postgresql python@3.10 python@3.9 python@3.8 ptpython pyenv rbenv-bundler-ruby-version rbenv-chefdk rbenv-default-gems ruby ruby@2.7 rubyfmt shellcheck termtosvg terragrunt tfenv tflint vault vault-cli wget yq
```

- And install the cask ones:

``` bash
brew install --cask adoptopenjdk atom chef-workstation dbvisualizer docker firefox gitkraken postman session-manager-plugin sublime-text vagrant visual-studio-code vlc temurin
```

### Manually install/configure software

Install DisplayLink driver/manager <https://www.synaptics.com/products/displaylink-graphics/downloads/macos>

Install [oh-my-zsh](https://ohmyz.sh/)

Install [ssh-ident](https://github.com/ccontavalli/ssh-ident)

Install stand-alone or Mac Apple App Store apps, such as:

```
Atom
Bear
CopyClip
Magnet
DbVisualizer
DemoPro
Firefox Developer Edition
GitHub Desktop
GitKraken
Microsoft Remote Desktop
MySQL Workbench
PgAdmin
Slack
Spectacle
Sublime Text
Teaminator
Logitech G Hub
```

Install and use a password/secrets manager, such as:

- Strongbox
- 1password
- KeePassX
- BitWarden
- LastPass

Install and use browser addons / extensions, such as:

- OneTab
- Tree Style Tab
- uBlock Origin
- Container Tabs
- TamperMonkey
- Prioritab
- and a plugin for your preferred password manager such as LastPass or 1password

## Step 3

### Fonts

Install fontconfig

`brew install fontconfig`

Install some cool fonts:

- Fira Code [link](https://fonts.google.com/specimen/Fira+Code)
- Nanum Gothic Coding [link](https://fonts.google.com/specimen/Nanum+Gothic+Coding)

### Configure applications

Import settings profiles for iTerm, VS Code, Sublime Text, etc.

Copy settings for your "dot files" (`.zshrc`, `.zprofile`, `.ssh/config`, vim, git)

See the other files in this directory.

## Step 4

### Setup your dev tools such as vim, VS Code, and others

vim configurations, vimrc, zsh, zsh themes,

- https://linuxhint.com/vimrc_tutorial/
- https://github.com/amix/vimrc
- https://github.com/dotphiles/dotvim
- https://github.com/bougyman/dotvim

tmux and iterm:

- https://github.com/tmux-plugins/tpm
- https://iterm2.com/documentation-tmux-integration.html
- [Start multiple synchronized SSH connections with Tmux](https://gist.github.com/dmytro/3984680)
- https://medium.com/@gveloper/using-iterm2s-built-in-integration-with-tmux-d5d0ef55ec30

Suggested extensions for the VS Code IDE:

```
ls -la ~/.vscode/extensions/ | awk '{print $NF}'
alefragnani.bookmarks-13.2.2
alexcvzz.vscode-sqlite-0.14.0
davidanson.vscode-markdownlint-0.45.0
ecmel.vscode-html-css-1.10.2
eriklynd.json-tools-1.0.2
formulahendry.code-runner-0.11.6
formulahendry.github-actions-0.0.1
formulahendry.terminal-0.0.10
golang.go-0.29.0
grapecity.gc-excelviewer-3.0.44
hashicorp.terraform-2.16.0
hilleer.yaml-plus-json-1.8.0
hilleer.yaml-plus-json-1.9.2
ivanhofer.git-assistant-1.3.14
jebbs.plantuml-2.16.1
kevinrose.vsc-python-indent-1.14.2
me-dutour-mathieu.vscode-github-actions-3.0.1
ms-azuretools.vscode-docker-1.18.0
ms-kubernetes-tools.vscode-kubernetes-tools-1.3.4
ms-python.python-2021.11.1422169775
ms-python.vscode-pylance-2021.11.2
ms-toolsai.jupyter-2021.10.1101450599
ms-toolsai.jupyter-keymap-1.0.0
ms-toolsai.jupyter-renderers-1.0.3
ms-vscode-remote.remote-containers-0.205.2
naco-siren.gradle-language-0.2.3
naumovs.color-highlight-2.5.0
nicolasvuillamy.vscode-groovy-lint-1.4.0
nicolasvuillamy.vscode-groovy-lint-1.5.1
nicolasvuillamy.vscode-groovy-lint-1.5.2
njpwerner.autodocstring-0.5.4
quicktype.quicktype-12.0.46
rebornix.ruby-0.28.1
redhat.java-1.0.0
redhat.vscode-yaml-1.2.0
redhat.vscode-yaml-1.2.1
secanis.jenkinsfile-support-0.1.0
visualstudioexptteam.vscodeintellicode-1.2.14
vscjava.vscode-java-debug-0.36.0
vscjava.vscode-java-debug-0.37.0
vscjava.vscode-java-dependency-0.18.8
vscjava.vscode-java-pack-0.18.6
vscjava.vscode-java-test-0.32.0
vscjava.vscode-java-test-0.33.0
vscjava.vscode-maven-0.34.1
vscode-icons-team.vscode-icons-11.7.0
waderyan.gitblame-8.1.0
wholroyd.jinja-0.0.8
wingrunr21.vscode-ruby-0.28.0
yzhang.markdown-all-in-one-3.4.0
```

URLs for some of these VSCode extensions as they appear on the marketplace,

Name: BookmarksId: alefragnani.bookmarksDescription: Mark lines and jump to themVersion: 13.1.0Publisher: Alessandro FragnaniVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=alefragnani.Bookmarks  
 
 

Name: Color HighlightId: naumovs.color-highlightDescription: Highlight web colors in your editorVersion: 2.3.0Publisher: Sergii NaumovVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=naumovs.color-highlight  
 
 

Name: DockerId: ms-azuretools.vscode-dockerDescription: Makes it easy to create, manage, and debug containerized applications.Version: 1.14.0Publisher: MicrosoftVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker  
 
 

Name: Excel ViewerId: grapecity.gc-excelviewerDescription: View Excel spreadsheets and CSV files within Visual Studio Code workspaces.Version: 3.0.42Publisher: GrapeCityVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=GrapeCity.gc-excelviewer  
 
 

Name: Git BlameId: waderyan.gitblameDescription: See git blame information in the status bar.Version: 7.0.6Publisher: Wade AndersonVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=waderyan.gitblame  
 
 

Name: GoId: golang.goDescription: Rich Go language support for Visual Studio CodeVersion: 0.26.0Publisher: Go Team at GoogleVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=golang.Go  
 
 

Name: Gradle Language SupportId: naco-siren.gradle-languageDescription: Add Gradle language support for Visual Studio CodeVersion: 0.2.3Publisher: Naco SirenVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=naco-siren.gradle-language  
 
 

Name: HashiCorp TerraformId: hashicorp.terraformDescription: Syntax highlighting and autocompletion for TerraformVersion: 2.13.0Publisher: HashiCorpVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=HashiCorp.terraform  
 
 

Name: HTML CSS SupportId: ecmel.vscode-html-cssDescription: CSS Intellisense for HTMLVersion: 1.10.2Publisher: ecmelVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ecmel.vscode-html-css  
 
 

Name: Jenkinsfile SupportId: secanis.jenkinsfile-supportDescription: Adds syntax highlighting support for Jenkinsfile's. In this version, it's the same like Groovy is.Version: 0.1.0Publisher: 
￼

secanis.ch - developed in switzerland VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=secanis.jenkinsfile-support  
 
 

Name: JinjaId: wholroyd.jinjaDescription: Jinja template language support for Visual Studio CodeVersion: 0.0.8Publisher: wholroydVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=wholroyd.jinja  
 
 

Name: JSON ToolsId: eriklynd.json-toolsDescription: Tools for manipulating JSONVersion: 1.0.2Publisher: Erik LyndVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=eriklynd.json-tools  
 
 

Name: JupyterId: ms-toolsai.jupyterDescription: Jupyter notebook support, interactive programming and computing that supports Intellisense, debugging and more.Version: 2021.6.999662501Publisher: MicrosoftVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter  
 
 

Name: KubernetesId: ms-kubernetes-tools.vscode-kubernetes-toolsDescription: Develop, deploy and debug Kubernetes applicationsVersion: 1.3.3Publisher: MicrosoftVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-kubernetes-tools.vscode-kubernetes-tools  
 
 

Name: Markdown All in OneId: yzhang.markdown-all-in-oneDescription: All you need to write Markdown (keyboard shortcuts, table of contents, auto preview and more)Version: 3.4.0Publisher: Yu ZhangVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one  
 
 

Name: markdownlintId: davidanson.vscode-markdownlintDescription: Markdown linting and style checking for Visual Studio CodeVersion: 0.42.1Publisher: David AnsonVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint  
 
 

Name: Paste JSON as CodeId: quicktype.quicktypeDescription: Copy JSON, paste as Go, TypeScript, C#, C++ and more.Version: 12.0.46Publisher: quicktypeVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=quicktype.quicktype  
 
 

Name: PlantUMLId: jebbs.plantumlDescription: Rich PlantUML support for Visual Studio Code.Version: 2.15.1Publisher: jebbsVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml  
 
 

Name: PylanceId: ms-python.vscode-pylanceDescription: A performant, feature-rich language server for Python in VS CodeVersion: 2021.7.2Publisher: MicrosoftVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance  
 
 

Name: PythonId: ms-python.pythonDescription: IntelliSense (Pylance), Linting, Debugging (multi-threaded, remote), Jupyter Notebooks, code formatting, refactoring, unit tests, and more.Version: 2021.6.944021595Publisher: MicrosoftVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-python.python  
 
 

Name: Python Docstring GeneratorId: njpwerner.autodocstringDescription: Automatically generates detailed docstrings for python functionsVersion: 0.5.4Publisher: Nils WernerVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring  
 
 

Name: Python IndentId: kevinrose.vsc-python-indentDescription: Correct python indentation.Version: 1.14.2Publisher: Kevin RoseVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent  
 
 

Name: Remote - ContainersId: ms-vscode-remote.remote-containersDescription: Open any folder or repository inside a Docker container and take advantage of Visual Studio Code's full feature set.Version: 0.183.0Publisher: MicrosoftVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers  
 
 

Name: RubyId: rebornix.rubyDescription: Ruby language support and debugging for Visual Studio CodeVersion: 0.28.1Publisher: Peng LvVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=rebornix.Ruby  
 
 

Name: SQLiteId: alexcvzz.vscode-sqliteDescription: Explore and query SQLite databases.Version: 0.13.0Publisher: alexcvzzVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite  
 
 

Name: TerminalId: formulahendry.terminalDescription: Terminal for Visual Studio CodeVersion: 0.0.10Publisher: Jun HanVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=formulahendry.terminal  
 
 

Name: Visual Studio IntelliCodeId: visualstudioexptteam.vscodeintellicodeDescription: AI-assisted developmentVersion: 1.2.14Publisher: MicrosoftVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode  
 
 

Name: VSCode RubyId: wingrunr21.vscode-rubyDescription: Syntax highlighing, snippet, and language configuration support for RubyVersion: 0.28.0Publisher: Stafford BrunkVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=wingrunr21.vscode-ruby  
 
 

Name: vscode-iconsId: vscode-icons-team.vscode-iconsDescription: Icons for Visual Studio CodeVersion: 11.5.0Publisher: VSCode Icons TeamVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons  
 
 

Name: YAMLId: redhat.vscode-yamlDescription: YAML Language Support by Red Hat, with built-in Kubernetes syntax supportVersion: 0.21.0Publisher: Red HatVS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml

----

and if you want to see vscode profile settings from here,

example vscode settings,

``` json
{
    "workbench.colorTheme": "Default High Contrast",
    "telemetry.enableTelemetry": false,
    "telemetry.telemetryLevel": "crash",
    "editor.fontFamily": "Nanum Gothic Regular, NanumGothicCoding, Fira Code Retina, FiraCode-Retina, Fira Code, Menlo, Monaco, 'Courier New', monospace",
    "editor.fontLigatures": true,
    "editor.fontSize": 14,
    "workbench.iconTheme": "vscode-icons",
    "editor.suggestSelection": "first",
    "vsintellicode.modify.editor.suggestSelection": "automaticallyOverrodeDefaultValue",
    "window.zoomLevel": 2,
    "workbench.editorAssociations": {
        "*.ipynb": "jupyter.notebook.ipynb"
    },
    "python.pythonPath": "/usr/local/bin/python3",
    "security.workspace.trust.untrustedFiles": "open",
    "redhat.telemetry.enabled": false,
    "files.associations": {
        "*.tfvars": "terraform"
    },
    "go.toolsManagement.autoUpdate": true,
    "files.exclude": {
        "**/.classpath": true,
        "**/.project": true,
        "**/.settings": true,
        "**/.factorypath": true
    },
    "editor.renderWhitespace": "boundary",
    "editor.cursorStyle": "line",
    "editor.autoClosingBrackets": "beforeWhitespace",
    "editor.autoClosingQuotes": "beforeWhitespace",
    "editor.bracketPairColorization.enabled": true,
    "editor.letterSpacing": 1,
    "editor.showFoldingControls": "always",
    "editor.unfoldOnClickAfterEndOfLine": true,
    "editor.cursorBlinking": "smooth",
    "editor.cursorSmoothCaretAnimation": true
}
```

### Other dev tool things

Remember and use these software design methodologies:
https://12factor.net/

Kubernetes examples:
https://github.com/kelseyhightower/kubernetes-the-hard-way

RegEx tool:
https://regexr.com/

Remember to customize your git hooks:
https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks

Use this "Python Speed Sheet": https://speedsheet.io/s/python (here is a video to show how it works: https://www.youtube.com/watch?v=66RumAF50_4 )

Share articles with people you code with to help establish good common working habits among you:

- https://dhwthompson.com/2019/my-favourite-git-commit
- https://chris.beams.io/posts/git-commit/
- https://mtlynch.io/code-review-love/

Some other tools, references; or otherwise useful, helpful links:

https://github.com/google/yapf

https://github.com/koalaman/shellcheck

https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/

https://jmeter.apache.org/

https://api-university.com/blog/the-api-mandate/

http://www.zytrax.com/tech/lang/ruby/

https://alpha-docs-aws.amazon.com/awsstyleguide/latest/styleguide/Welcome.html

https://hackmd.io/#

https://hackmd.io/@vokunev/SkaVWm5BN

https://cryptopals.com/

https://en.wikibooks.org/wiki/Ad_Hoc_Data_Analysis_From_The_Unix_Command_Line

https://github.com/nbedos/termtosvg

https://pragprog.com/titles/bopytest/python-testing-with-pytest/

https://dnsviz.net/

http://www.votingpoker.com/

https://blog.cloudflare.com/mmproxy-creative-way-of-preserving-client-ips-in-spectrum/

https://github.com/learnbyexample/learn_gnuawk

https://github.com/kylelobo/The-Documentation-Compendium

https://genius.engineering/faster-and-simpler-with-the-command-line-deep-comparing-two-5gb-json-files-3x-faster-by-ditching-the-code/

https://github.com/pditommaso/awesome-pipeline

http://plantuml.com/deployment-diagram

https://explainshell.com/

https://gto76.github.io/python-cheatsheet/

https://github.com/awesome-selfhosted/awesome-selfhosted
