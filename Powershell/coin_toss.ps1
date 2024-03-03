$PI = 3.14
Write-Host "The value of `$PI is $PI"

# Single quotes - what you write is what you get - literal
Write-Host 'Here is $PI'

# Double quotes - variables in strings are interpolated
Write-Host "Here is `$PI and its value is $PI"
# ` escapes interpolation

# $() - 