import os
import subprocess
import shutil
os.system("cls" if os.name == "nt" else "clear")
bash_script = '''
echo "Nếu Cảm Thấy Vào Tool Chậm Vui Lòng Thử Bật VPN ..."
if [[ "$(python3 -V | awk '{print $2}' | sed 's/\./ /g' | awk '{print $2}')" != "11" ]]; then echo "Please install Python3.11"; exit 0;fi
curl "https://raw.githubusercontent.com/tienmai291207/update/main/MTT-TOOL.py" -o MTT-TOOL.py --silent
'''
subprocess.run(['bash', '-c', bash_script], shell=False, check=True)
shutil.move("MTT-TOOL.py", ".MTT-TOOL.py")
subprocess.run(['python3', '.MTT-TOOL.py'], shell=False, check=True)
