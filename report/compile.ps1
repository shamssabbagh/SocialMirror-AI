# Compilation script for SocialMirror-AI Multilingual (Hebrew/English) Report
# Usage: .\compile.ps1

$reportDir = $PSScriptRoot
Set-Location $reportDir

Write-Host "Compiling SocialMirror-AI Multilingual (Hebrew RTL) Preparatory Report..." -ForegroundColor Cyan

# Ensure MiKTeX is in PATH if installed in user local directory
$miktexBin = "C:\Users\shams\AppData\Local\Programs\MiKTeX\miktex\bin\x64"
if ((Test-Path $miktexBin) -and ($env:Path -notlike "*$miktexBin*")) {
    $env:Path = "$miktexBin;$env:Path"
}

# Check for xelatex (required for Hebrew Unicode & System Fonts)
if (Get-Command xelatex -ErrorAction SilentlyContinue) {
    Write-Host "Pass 1: xelatex..." -ForegroundColor Green
    xelatex -interaction=nonstopmode -halt-on-error -disable-installer main.tex
    
    if (Get-Command bibtex -ErrorAction SilentlyContinue) {
        Write-Host "Pass 2: bibtex..." -ForegroundColor Green
        bibtex -disable-installer main
    }
    
    Write-Host "Pass 3: xelatex (resolving references & TOC)..." -ForegroundColor Green
    xelatex -interaction=nonstopmode -halt-on-error -disable-installer main.tex
    
    Write-Host "Pass 4: xelatex (final layout)..." -ForegroundColor Green
    xelatex -interaction=nonstopmode -halt-on-error -disable-installer main.tex
} else {
    Write-Host "xelatex was not found in the current PATH." -ForegroundColor Red
    Write-Host "Please ensure MiKTeX / TeX Live with XeLaTeX is installed." -ForegroundColor Yellow
}

if (Test-Path "main.pdf") {
    $pdf = Get-Item "main.pdf"
    Write-Host "Build complete: $($pdf.FullName) ($($pdf.Length) bytes)" -ForegroundColor Green
} else {
    Write-Host "Build failed. Check main.log for errors." -ForegroundColor Red
}
