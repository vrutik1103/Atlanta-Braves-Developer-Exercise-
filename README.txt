Batted Ball Data Visualization

Overview:
This application is designed to visualize and contextualize batted ball data from an uploaded Excel file.

Key Features:
- Upload Excel (.xlsx) files containing batted ball data.
- Visualizations include:
    - Batter Hits vs Pitcher: A bar chart showing the number of hits per batter against different pitchers.
    - Launch Angle vs Exit Speed: A scatter plot showing the correlation between launch angle and exit speed.
    - Hit Distance vs Hang Time: A scatter plot visualizing the relationship between hit distance and hang time.
    - Play Outcome Distribution: A bar chart displaying the distribution of various play outcomes.

Requirements:
- Python 3.x
- Flask
- Pandas
- Plotly

Instructions to Run the Application(Easy to run on Visual Studio Code):
1. Install the required libraries by running the following command:
    - command: pip install flask pandas plotly openpyxl
2. Clone or download the project files.
3. Open a terminal and navigate to the project directory. 
3. Ensure the necessary dependencies are install.
4. Run the following command to start the Flask server:
    - command: python app.py
5. Open a web browser and go to http://127.0.0.1:5000 to access the application.
6. Upload the provided BattedBallData.xlsx file (or any other similar data file) and explore the visualizations.

Notes:
- The application is designed to process a maximum of 1000 rows at a time for performance considerations. If you want to increase the number of rows past 1000, then can be done by editing the index.html file.
- Make sure the Excel file has the required columns, otherwise, an error message will be displayed.
- Two files are required to run the app. Index.html is located in templates. app.py file should be visible below README.txt file. 
- It's easy to either clone or download the github repository to veiw the exercise. Then follow the instructions to run.

