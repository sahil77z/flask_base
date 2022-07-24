import importlib.util
import os

package_name = 'pyrogram'

spec = importlib.util.find_spec(package_name)

if spec is None:
    print("Installing Modules 🔌")
    os.system("pip install -r requirements.txt")
    os.system("python app.py")

else:
  print("Starting Bot ⭐")
  os.system("python app.py")
