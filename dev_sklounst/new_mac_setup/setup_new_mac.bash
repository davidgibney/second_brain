#!/usr/bin/env /bin/bash

read -p 'Proceed with disabling Mac OS nonsense like SmartQuotes and TextReplacement? Y/n' yeet

if [[ "$yeet" -eq "Y" || "$yeet" -eq "y" ]]; then
  defaults write -g ApplePressAndHoldEnabled -bool false

  for d in $(defaults domains|tr -d ,);do
    osascript -e "app id \"$d\""&>/dev/null||continue
    defaults write $d SmartQuotes -bool false
    defaults write $d SmartDashes -bool false
    defaults write $d SmartLinks -bool false
    defaults write $d SmartCopyPaste -bool false
    defaults write $d TextReplacement -bool false
    defaults write $d CheckSpellingWhileTyping -bool false
  done
fi

read -p 'Proceed with installing HomeBrew? Y/n' yeet

if [[ "$yeet" -eq "Y" || "$yeet" -eq "y" ]]; then
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  eval "$(/opt/homebrew/bin/brew shellenv)"
  echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
fi

echo "Next is to install things using HomeBrew. But for some, you should decide if you would prefer to install with HomeBrew or Apple App Store or stand-alone pkg/dmg."
read -p 'Proceed with installing a pre-determined list of common tools and apps using HomeBrew? Y/n' yeet

if [[ "$yeet" -eq "Y" || "$yeet" -eq "y" ]]; then
  brew install adoptopenjdk11 ansible argocd argocd-vault-plugin autoconf automake awscli azure-cli azure-storage-cpp azcopy bash bpython circleci coreutils docker-credential-helper-ecr expect gpg go gojq graphviz groovy ipython inframap jenkins-lts jenv jmeter jq kubecfg kubernetes-cli libpq libtool minikube nmap oci-cli openjdk pipenv postgresql python@3.10 python@3.9 python@3.8 ptpython pyenv rbenv-bundler-ruby-version rbenv-chefdk rbenv-default-gems ruby ruby@2.7 rubyfmt shellcheck vault vault-cli termtosvg terragrunt tfenv tflint wget yq
  brew install --cask adoptopenjdk atom chef-workstation dbvisualizer docker firefox gitkraken postman session-manager-plugin sublime-text vagrant visual-studio-code vlc temurin
fi

echo "Some things have been installed."
echo "Remember to look through the other docs for checklists of other installs or configurations to do."
echo "For example, do not forget to also install..."
echo "https://github.com/ccontavalli/ssh-ident"
echo "https://ohmyz.sh/"
echo "And configure your dot files."
