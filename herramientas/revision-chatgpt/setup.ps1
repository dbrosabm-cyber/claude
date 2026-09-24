# Setup script for review_with_chatgpt.py on Windows.
# Run this from PowerShell, from the root of the cloned repo:
#   .\herramientas\revision-chatgpt\setup.ps1

$ErrorActionPreference = "Stop"

function Test-Command($name) {
    return [bool](Get-Command $name -ErrorAction SilentlyContinue)
}

Write-Host "== Checking prerequisites ==" -ForegroundColor Cyan

if (-not (Test-Command "git")) {
    Write-Host "Git not found. Install it from https://git-scm.com/download/win and re-run this script." -ForegroundColor Red
    exit 1
}

if (-not (Test-Command "python")) {
    Write-Host "Python not found. Install it from https://www.python.org/downloads/windows/ (check 'Add python.exe to PATH') and re-run this script." -ForegroundColor Red
    exit 1
}

Write-Host "Git and Python found." -ForegroundColor Green

Write-Host "== Installing Python dependencies ==" -ForegroundColor Cyan
python -m pip install -r (Join-Path $PSScriptRoot "requirements.txt")

Write-Host "== OpenAI API key ==" -ForegroundColor Cyan
$existing = [Environment]::GetEnvironmentVariable("OPENAI_API_KEY", "User")
if ($existing) {
    Write-Host "An OPENAI_API_KEY is already saved for your user account. Keeping it." -ForegroundColor Green
} else {
    $secureKey = Read-Host "Paste your OpenAI API key (input hidden)" -AsSecureString
    $bstr = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureKey)
    $plainKey = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($bstr)
    [System.Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr)

    if ([string]::IsNullOrWhiteSpace($plainKey)) {
        Write-Host "No key entered. Skipping. Set OPENAI_API_KEY manually before running review_with_chatgpt.py." -ForegroundColor Yellow
    } else {
        [Environment]::SetEnvironmentVariable("OPENAI_API_KEY", $plainKey, "User")
        $env:OPENAI_API_KEY = $plainKey
        Write-Host "Key saved for your Windows user account (persists across terminals)." -ForegroundColor Green
    }
}

Write-Host "== Setup complete ==" -ForegroundColor Cyan
Write-Host "Open a NEW PowerShell window (so the saved key loads), then run:"
Write-Host "  python herramientas\revision-chatgpt\review_with_chatgpt.py <path-to-file>" -ForegroundColor Yellow
