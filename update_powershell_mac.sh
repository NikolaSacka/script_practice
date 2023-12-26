#!/bin/bash

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "Homebrew is not installed. Please install Homebrew first."
    exit 1
fi

# Update Homebrew
brew update

# Check if PowerShell is installed
if ! command -v pwsh &> /dev/null; then
    echo "PowerShell is not installed. Please install PowerShell using Homebrew."
    exit 1
fi

# Update PowerShell
brew upgrade --cask powershell

echo "PowerShell has been updated."
