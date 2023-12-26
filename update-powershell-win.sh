# Function to check if an update is available
function IsUpdateAvailable {
    $currentVersion = $PSVersionTable.PSVersion
    $latestVersion = Invoke-WebRequest -Uri "https://github.com/PowerShell/PowerShell/releases/latest" -MaximumRedirection 0
    $latestVersion = $latestVersion.Headers.Location -replace '.*/v', ''
    
    return [version]$latestVersion -gt $currentVersion
}

# Function to update PowerShell
function UpdatePowerShell {
    $downloadUrl = "https://github.com/PowerShell/PowerShell/releases/latest/download/PowerShell.Windows.x64.msi"
    $installerPath = "$env:TEMP\PowerShellUpdate.msi"

    # Download the latest installer
    Invoke-WebRequest -Uri $downloadUrl -OutFile $installerPath

    # Install the update
    Start-Process -FilePath "msiexec.exe" -ArgumentList "/i `"$installerPath`" /qn /norestart" -Wait

    # Clean up the installer
    Remove-Item $installerPath
}

# Main script
if (IsUpdateAvailable) {
    Write-Host "An update for PowerShell is available."
    Write-Host "Updating PowerShell..."
    UpdatePowerShell
    Write-Host "PowerShell has been updated."
} else {
    Write-Host "No update available for PowerShell."
}
