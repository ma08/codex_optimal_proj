#!/bin/bash

# Check for Homebrew,
# Install if we don't have it
if test ! $(which brew); then
  echo "Installing homebrew..."
  ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi

# Update homebrew recipes
brew update

# Install GNU core utilities (those that come with OS X are outdated)
brew install coreutils

# Install GNU `find`, `locate`, `updatedb`, and `xargs`, g-prefixed
brew install findutils

# Install Bash 4
brew install bash

# Install more recent versions of some OS X tools
brew tap homebrew/dupes
brew install homebrew/dupes/grep

binaries=(
  graphicsmagick
  webkit2png
  rename
  zopfli
  ffmpeg
  python
  sshfs
  trash
  node
  tree
  ack
  hub
  git
)

echo "installing binaries..."
brew install ${binaries[@]}

brew cleanup

# Install fonts
brew tap caskroom/fonts
brew cask install font-fira-code

# Install apps
brew tap caskroom/cask

apps=(
  iterm2
  google-chrome
  firefox
  slack
  skype
  dropbox
  spotify
  sublime-text
  visual-studio-code
  vlc
  gpgtools
  zeplin
  postman
  docker
  postgres
  mongodb
  robo-3t
  sequel-pro
  robomongo
  java
  android-studio
  # quick-look-plugins # https://github.com/sindresorhus/quick-look-plugins
  # qlcolorcode
  # qlstephen
  # qlmarkdown
  # quicklook-json
  # qlprettypatch
  # quicklook-csv
  # betterzipql
  # qlimagesize
  # webpquicklook
  # suspicious-package
)

# Install apps to /Applications
# Default is: /Users/$user/Applications
echo "installing apps..."
brew cask install --appdir="/Applications" ${apps[@]}

# Remove outdated versions from the cellar
brew cleanup
