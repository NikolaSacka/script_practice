# Install the Posh-SSH module if not already installed
# Install-Module -Name Posh-SSH

# Import the Posh-SSH module
Import-Module Posh-SSH

# Configuration parameters
# Replace the placeholders like DEVICE_IP, USERNAME, and PASSWORD with the actual values.
$deviceIP = "DEVICE_IP"
$username = "USERNAME"
$password = "PASSWORD"
# Commands that will be executed
$commands = @(
    "config t",
    "interface GigabitEthernet0/1",
    "ip address 192.168.1.1 255.255.255.0",
    "no shutdown",
    "end",
    "wr"
)

# Establish SSH connection
$sshSession = New-SSHSession -ComputerName $deviceIP -Credential (Get-Credential -UserName $username -Message "Enter password")

# Check if the SSH session is established
if ($sshSession -ne $null) {
    Write-Host "SSH session established to $deviceIP"

    # Execute commands on the device
    $output = Invoke-SSHCommand -SessionId $sshSession.SessionId -Command $commands

    # Display command output
    foreach ($line in $output.Output) {
        Write-Host $line
    }

    # Close SSH session
    Remove-SSHSession -SessionId $sshSession.SessionId
    Write-Host "SSH session closed"
} else {
    Write-Host "Failed to establish SSH session to $deviceIP"
}
