@echo off 
echo ���̃f�B���N�g���ɉ��z�����쐬���܂����H

pause


python -m venv .venv

rem �A�b�v�O���[�h pip
python.exe -m pip install --upgrade pip --proxy http://10.103.1.2:8080

rem requirements.txt ���Q�Ƃ����̃C���X�g�[��
pip install -r requirements.txt --proxy http://10.103.1.2:8080

rem ���z���̎��s
.venv/Scripts/activate.ps1

