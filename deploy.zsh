# zip to upload to AWS Lambda
(zip archive.zip main.py model.pkl) && (cd venv/lib/python3.9/site-packages && zip -r "$OLDPWD/archive.zip" .)