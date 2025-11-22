# Ask user for the repository URL
$repoUrl = Read-Host "Please paste the new GitHub Repository URL (e.g., https://github.com/username/repo.git)"

# Check if URL is provided
if ([string]::IsNullOrWhiteSpace($repoUrl)) {
    Write-Host "Error: No URL provided." -ForegroundColor Red
    exit 1
}

# Add remote
Write-Host "Adding remote origin..."
git remote add origin $repoUrl

# Rename branch to main
Write-Host "Renaming branch to main..."
git branch -M main

# Push to GitHub
Write-Host "Pushing code to GitHub..."
git push -u origin main

Write-Host "Success! Your code is now on GitHub." -ForegroundColor Green
Pause
