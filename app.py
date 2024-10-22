from flask import Flask, request, render_template
import pandas as pd
import plotly.express as px
import os

app = Flask(__name__)

UPLOAD_FILE = 'uploads'
if not os.path.exists(UPLOAD_FILE):
    os.makedirs(UPLOAD_FILE)

@app.route('/')
def index():
    return render_template('index.html', show_logo=True)  

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file uploaded'
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    
    filepath = os.path.join(UPLOAD_FILE, file.filename)
    file.save(filepath)

    try:
        df = pd.read_excel(filepath)
        print("File uploaded and read successfully")
    except Exception as e:
        return f"Error reading the Excel file: {str(e)}"
    
    required_columns = ['BATTER_ID', 'BATTER', 'PITCHER_ID', 'PITCHER', 'GAME_DATE', 'LAUNCH_ANGLE', 'EXIT_SPEED', 'HIT_DISTANCE', 'HANG_TIME', 'PLAY_OUTCOME', 'VIDEO_LINK']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        return f"Required columns missing in the file: {', '.join(missing_columns)}"
    

    num_rows = int(request.form.get('rows', 100))
    df = df.head(num_rows)

    batter_hits = df.groupby(['BATTER', 'PITCHER'])['HIT_DISTANCE'].count().reset_index(name='Hit Count')
    batter_hits_fig = px.bar(batter_hits, x='BATTER', y='Hit Count', color='PITCHER', title="Batter Hits vs Pitcher")

    launch_fig = px.scatter(df, x='LAUNCH_ANGLE', y='EXIT_SPEED', title='Launch Angle vs Exit Speed', hover_data=['VIDEO_LINK', 'PLAY_OUTCOME'])

    distance_fig = px.scatter(df, x='HIT_DISTANCE', y='HANG_TIME', title='Hit Distance vs Hang Time', hover_data=['PLAY_OUTCOME', 'VIDEO_LINK'])

    play_outcomes = df['PLAY_OUTCOME'].value_counts().reset_index()
    play_outcomes.columns = ['Outcome', 'Count']  
    play_outcome_fig = px.bar(play_outcomes, x='Outcome', y='Count', title='Play Outcome Distribution')

    batter_hits_html = batter_hits_fig.to_html(full_html=False)
    launch_html = launch_fig.to_html(full_html=False)
    distance_html = distance_fig.to_html(full_html=False)
    play_outcome_html = play_outcome_fig.to_html(full_html=False)

    return render_template('index.html',
                           batter_hits_numbers_plot=batter_hits_html,
                           launch_plot=launch_html,
                           distance_plot=distance_html,
                           outcome_plot=play_outcome_html,
                           show_logo=False)  

if __name__ == '__main__':
    app.run(debug=True)
