# Comment to self, the "my application" prefix is the same, find a way to run this code without chaning manuly the ID.
# List of port-forward commands
$commands = @(
    "kubectl port-forward prometheus-kube-prometheus-stack-prometheus-0 -n observation 9090:9090",
    "kubectl port-forward kube-prometheus-stack-grafana-7664d8545c-49t4m -n observation 9091:3000",
    "kubectl port-forward my-application-myhelm-7d96744847-gl6b7 -n dev 5000:5000",
    "kubectl port-forward myjenkins-0 8082:8080",
    "kubectl port-forward argocd-server-84f8547bdf-g5gsj -n argocd 8081:8080"
)

# Loop through each command and open a new PowerShell terminal to run the command
foreach ($command in $commands) {
    Start-Process powershell -ArgumentList "-NoExit", "-Command", $command
}
