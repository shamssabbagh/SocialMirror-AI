# Compilation script for SocialMirror-AI LaTeX report
# Usage: .\compile.ps1

$reportDir = $PSScriptRoot
Set-Location $reportDir

Write-Host "Compiling SocialMirror-AI Preparatory Report..." -ForegroundColor Cyan

# Check for pdflatex
if (Get-Command pdflatex -ErrorAction SilentlyContinue) {
    Write-Host "Running 3-pass pdflatex + bibtex compilation..." -ForegroundColor Green
    pdflatex -interaction=nonstopmode -halt-on-error -disable-installer main.tex
    if (Get-Command bibtex -ErrorAction SilentlyContinue) {
        bibtex -disable-installer main
    }
    pdflatex -interaction=nonstopmode -halt-on-error -disable-installer main.tex
    pdflatex -interaction=nonstopmode -halt-on-error -disable-installer main.tex
} elseif (Get-Command latexmk -ErrorAction SilentlyContinue) {
    Write-Host "Using latexmk..." -ForegroundColor Green
    latexmk -pdf -interaction=nonstopmode -synctex=1 main.tex
} else {
    Write-Host "Neither pdflatex nor latexmk was found in the current PATH." -ForegroundColor Yellow
    Write-Host "You can open this project in Overleaf or compile using MiKTeX / TeX Live." -ForegroundColor Gray
}

if (Test-Path "main.pdf") {
    Write-Host "Build complete: main.pdf generated successfully." -ForegroundColor Green
} else {
    Write-Host "Build finished. Check main.log if any errors occurred." -ForegroundColor Yellow
}
