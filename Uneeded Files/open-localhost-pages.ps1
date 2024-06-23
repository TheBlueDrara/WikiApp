

# List of ports to open
$ports = @(
    9090,
    9091,
    5000,
    8082,
    8081
)

# Loop through each port and open a new browser tab with the corresponding localhost address
foreach ($port in $ports) {
    $url = "http://localhost:$port"
    Start-Process "chrome.exe" -ArgumentList $url
}
