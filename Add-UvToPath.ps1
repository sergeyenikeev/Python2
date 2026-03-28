$envKey = 'HKCU:\Environment'
try {
  $pythonScripts = (python -c "import pathlib, sysconfig; print(pathlib.Path(sysconfig.get_path('scripts', 'nt_user')).resolve())").Trim()
} catch {
  Write-Error "Не удалось определить папку скриптов Python: $_"
  exit 1
}
$userPath = $null
if (Test-Path $envKey) {
  $userPath = (Get-ItemProperty -Path $envKey -Name PATH -ErrorAction SilentlyContinue).PATH
}
$entries = @()
if ($userPath) {
  $entries = $userPath -split ';' | ForEach-Object { $_.Trim() } | Where-Object { $_ -ne '' }
}
$entries += $pythonScripts
$unique = [System.Collections.Generic.List[string]]::new()
foreach ($entry in $entries) {
  if ([string]::IsNullOrWhiteSpace($entry)) { continue }
  if (-not $unique.Contains($entry)) {
    $unique.Add($entry)
  }
}
$newPath = $unique -join ';'
New-ItemProperty -Path $envKey -Name PATH -PropertyType ExpandString -Value $newPath -Force | Out-Null
Write-Host "PATH пользователя обновлён. Новый путь скриптов: $pythonScripts. Откройте новое PowerShell-окно, чтобы изменения вступили в силу."
