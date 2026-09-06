@echo off
chcp 65001 > nul
title PixelPrompt Studio - Desktop Shortcut Generator

echo ========================================================
echo  👾 PixelPrompt Studio - 바탕화면 바로가기 생성기
echo ========================================================
echo.

set "TARGET_DIR=%~dp0"
set "TARGET_EXE=%TARGET_DIR%PixelPromptStudio.exe"
set "ICON_PATH=%TARGET_DIR%assets\app_icon.ico"

if not exist "%TARGET_EXE%" (
    echo [오류] PixelPromptStudio.exe 파일을 찾을 수 없습니다.
    pause
    exit /b 1
)

powershell -NoProfile -ExecutionPolicy Bypass -Command "$ws = New-Object -ComObject WScript.Shell; $sc = $ws.CreateShortcut([Environment]::GetFolderPath('Desktop') + '\PixelPrompt Studio.lnk'); $sc.TargetPath = '%TARGET_EXE%'; $sc.WorkingDirectory = '%TARGET_DIR%'; $sc.IconLocation = '%ICON_PATH%, 0'; $sc.Description = 'PixelPrompt Studio - 고해상도 도트 그래픽 & 앱 아이콘 전문 프롬프트 빌더'; $sc.Save()"

if exist "%USERPROFILE%\Desktop\PixelPrompt Studio.lnk" (
    echo [성공] 바탕화면에 'PixelPrompt Studio' 아이콘 바로가기가 생성되었습니다!
    echo       바탕화면에서 👾 도트 아이콘을 더블 클릭하여 즉시 실행하실 수 있습니다.
) else (
    echo [확인] 바로가기 생성을 확인해주세요.
)

echo.
pause
