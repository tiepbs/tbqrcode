from flask import Flask, request, render_template, send_from_directory
import os
from qrcode_script import generate_qr_code  # Import script của bạn

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        logo = request.files.get('logo')
        
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'qr_code.png')
        logo_path = None

        if logo:
            logo_path = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
            logo.save(logo_path)
        
        generate_qr_code(url, file_path, logo_path)

        return render_template('index.html', qr_code='static/qr_code.png')
    
    return render_template('index.html')

@app.route('/static/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
