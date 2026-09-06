@echo off
chcp 65001 > nul
echo ========================================================
echo  👾 PixelPrompt Studio - Windows 실행 파일 빌드 스크립트
echo ========================================================
echo.

echo [1/3] 가상환경 및 의존성 패키지 확인...
pip install -r requirements.txt

echo.
echo [2/3] PyInstaller 단일 실행 파일(.exe) 빌드 시작...
python -m PyInstaller ^
  --noconsole ^
  --onefile ^
  --name "PixelPromptStudio" ^
  --icon "assets/app_icon.ico" ^
  --add-data "ui.html;." ^
  --add-data "assets/app_icon.ico;assets" ^
  --add-data "assets/app_icon.png;assets" ^
  --collect-all pywebview ^
  app_webview.py

echo.
echo [3/3] 빌드 완료 파일 배치...
if exist "dist\PixelPromptStudio.exe" (
    copy /y "dist\PixelPromptStudio.exe" "PixelPromptStudio.exe"
    copy /y "dist\PixelPromptStudio.exe" "..\PixelPromptStudio.exe"
    echo.
    echo ========================================================
    echo  🎉 빌드 성공! PixelPromptStudio.exe 가 생성되었습니다.
    echo ========================================================
) else (
    echo.
    echo ❌ 빌드 중 오류가 발생했습니다. 로그를 확인하세요.
)
pause
