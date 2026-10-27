# Windows 10/11 x64. Default mode only checks commands. Use -Install to install.
# Sources: Microsoft WinGet community repository; PyPI via Astral uv.
[CmdletBinding()]
param([switch]$Install)
$ErrorActionPreference = 'Stop'
function Refresh-ToolPath {
    $parts = @($env:Path, [Environment]::GetEnvironmentVariable('Path','Machine'), [Environment]::GetEnvironmentVariable('Path','User'))
    $env:Path = ($parts | Where-Object { $_ }) -join ';'
}
function Resolve-Tool([string]$Name) {
    $command = Get-Command $Name -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($command) { return $command.Source }
    return $null
}
function Invoke-Checked([string]$Exe, [string[]]$Arguments) {
    & $Exe @Arguments
    if ($LASTEXITCODE -ne 0) { throw "$Exe failed (exit $LASTEXITCODE). Stop here; fix the reported error and retry." }
}
function Ensure-Tool([string]$Name,[string]$PackageId) {
    if (Resolve-Tool $Name) { Write-Host "Reuse: $Name"; return }
    Write-Host "Installing: $PackageId. Review any installer or license prompts."
    Invoke-Checked 'winget' @('install','--id',$PackageId,'--exact','--source','winget')
    Refresh-ToolPath
    if (!(Resolve-Tool $Name)) { throw "$Name installed but is not on PATH. Restart your terminal and run this script again." }
}
try {
    if ($Install) {
        if (!(Resolve-Tool 'winget')) { throw 'WinGet is missing. Install or update Microsoft App Installer, then retry: https://aka.ms/getwinget' }
        if (![Environment]::Is64BitOperatingSystem -or $env:PROCESSOR_ARCHITECTURE -eq 'ARM64') { throw 'This starter installer targets Windows x64. Use vendor instructions for your architecture.' }
        Ensure-Tool 'uv' 'astral-sh.uv'
        Ensure-Tool 'ffmpeg' 'Gyan.FFmpeg'
        Ensure-Tool 'pandoc' 'JohnMacFarlane.Pandoc'
        Ensure-Tool 'magick' 'ImageMagick.ImageMagick'
        # Isolated uv tool environment; does not pip-install into existing Conda/system Python.
        # Re-running ensures the requested document-format dependencies are present.
        Invoke-Checked 'uv' @('tool','install','--python','3.12','markitdown[pdf,docx,pptx,xlsx,xls]')
        Invoke-Checked 'uv' @('tool','update-shell')
        Refresh-ToolPath
        $toolBin = (& uv tool dir --bin | Out-String).Trim()
        if ($LASTEXITCODE -ne 0) { throw 'Could not resolve the uv tool binary directory.' }
        if (Test-Path -LiteralPath $toolBin -PathType Container) { $env:Path = "$toolBin;$env:Path" }
    }
    $checks = @(
        @{Name='uv'; Arguments=@('--version')},
        @{Name='ffmpeg'; Arguments=@('-version')},
        @{Name='ffprobe'; Arguments=@('-version')},
        @{Name='pandoc'; Arguments=@('--version')},
        @{Name='magick'; Arguments=@('-version')},
        @{Name='markitdown'; Arguments=@('--help')}
    )
    $missing = 0
    foreach ($check in $checks) {
        $toolPath = Resolve-Tool $check.Name
        if (!$toolPath) { Write-Host "MISSING: $($check.Name)" -ForegroundColor Yellow; $missing++; continue }
        $checkArgs = $check.Arguments
        $probeOutput = & $toolPath @checkArgs 2>&1
        if ($LASTEXITCODE -ne 0) { Write-Host "FAILED: $($check.Name)" -ForegroundColor Red; $missing++; continue }
        Write-Host "OK: $($check.Name) -> $toolPath" -ForegroundColor Green
    }
    if ($missing -gt 0) {
        Write-Host "$missing command(s) missing or failed. To install: .\install-agent-starter.ps1 -Install"
        exit 2
    }
    if ($Install) {
        # Small end-to-end checks. New unique directory; never overwrite the user's files.
        $checkDir = Join-Path $PSScriptRoot ('starter-check-' + [guid]::NewGuid().ToString('N').Substring(0,8))
        New-Item -ItemType Directory -Path $checkDir | Out-Null
        $md = Join-Path $checkDir 'sample.md'
        $docx = Join-Path $checkDir 'sample.docx'
        $roundtrip = Join-Path $checkDir 'roundtrip.md'
        $png = Join-Path $checkDir 'sample.png'
        $wav = Join-Path $checkDir 'sample.wav'
        Set-Content -LiteralPath $md -Value '# Agent Starter Check' -Encoding UTF8
        Invoke-Checked 'pandoc' @($md,'-o',$docx)
        Invoke-Checked 'markitdown' @($docx,'-o',$roundtrip)
        if (!(Select-String -LiteralPath $roundtrip -SimpleMatch 'Agent Starter Check' -Quiet)) { throw 'Document round-trip check failed.' }
        Invoke-Checked 'magick' @('-size','64x64','xc:white',$png)
        Invoke-Checked 'magick' @('identify',$png)
        Invoke-Checked 'ffmpeg' @('-hide_banner','-loglevel','error','-f','lavfi','-i','anullsrc=r=16000:cl=mono','-t','1',$wav)
        Invoke-Checked 'ffprobe' @('-v','error','-show_entries','format=duration','-of','default=nw=1',$wav)
        Write-Host "Sample files: $checkDir"
        Write-Host 'Smoke checks passed. Restart your Agent app so it receives the updated PATH.' -ForegroundColor Green
    } else { Write-Host 'Command checks passed. File-processing smoke checks run only with -Install.' }
    exit 0
} catch {
    Write-Host $_.Exception.Message -ForegroundColor Red
    Write-Host 'Setup did not complete. Existing installations have not been removed.'
    exit 1
}
