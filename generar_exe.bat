@echo off
echo ========================================
echo   Regenerando ejecutable de EDMonitor
echo ========================================
echo.
echo Limpiando carpetas previas...
if exist build rd /s /q build
if exist dist rd /s /q dist

echo.
echo Ejecutando PyInstaller...
pyinstaller --clean --noconfirm EDMonitor.spec

echo.
echo ========================================
echo   PROCESO COMPLETADO
echo   El ejecutable esta en: dist\EDMonitor
echo ========================================
pause
