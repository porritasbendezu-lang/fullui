@echo off
set VERSION=0.2.4

echo ============================
echo  LIMPIANDO ARCHIVOS VIEJOS
echo ============================

rmdir /s /q dist
rmdir /s /q build
for /d %%i in (*.egg-info) do rmdir /s /q "%%i"

echo.
echo ============================
echo  CONSTRUYENDO PAQUETE
echo ============================

py -m build
if %errorlevel% neq 0 (
    echo ERROR EN BUILD
    pause
    exit /b
)

echo.
echo ============================
echo  SUBIENDO A PYPI
echo ============================

py -m twine upload dist/*
if %errorlevel% neq 0 (
    echo ERROR EN UPLOAD PYPI
    pause
    exit /b
)

echo.
echo ============================
echo  PROCESO COMPLETADO
echo ============================

echo.
echo ............................

echo.
echo ============================
echo  GIT ADD / COMMIT
echo ============================

git add .

git commit -m "release %VERSION%"

echo.
echo ============================
echo  TAG VERSION
echo ============================

git tag %VERSION%

echo.
echo ============================
echo  PUSH MAIN + TAG
echo ============================

git push origin main
git push origin %VERSION%

echo.
echo ============================
echo  TODO COMPLETADO
echo ============================

pause