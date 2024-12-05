from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def embed_report():
    power_bi_embed_url = "https://app.powerbi.com/view?r=eyJrIjoiYjAzNjBkMGItMDNhNi00NGMwLWE5OGEtOGYyM2JjOTdkMDE0IiwidCI6ImU3OTQxZTI2LWUwODUtNGExNS1hMTI4LTdiNmUxNDE1MDczMCJ9"
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Power BI Report</title>
    </head>
    <body>
        <iframe 
            width="100%" 
            height="600px" 
            src="{power_bi_embed_url}" 
            frameborder="0" 
            allowFullScreen="true">
        </iframe>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
