# Generate a random number between 1 and 100
$randomNumber = Get-Random -Minimum 1 -Maximum 101

# Check if the random number is even or odd
if ($randomNumber % 2 -eq 0) {
    Write-Host "The random number $randomNumber is even"
} else {
    Write-Host "The random number $randomNumber is odd"
}