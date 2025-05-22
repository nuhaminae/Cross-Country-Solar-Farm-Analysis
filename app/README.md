This dashboard provides an interactive analysis of solar farm data across selected countries and variables.
# **Features**

    Country Selection: Choose one of the available countries (Benin, Sierra Leone, Togo) to view its solar farm data.
    Variable Selection: Select one or more solar radiation variables (GHI, DNI, DHI) to visualize their distribution.
    Boxplots: The dashboard displays boxplots for the selected variable(s) for the chosen country, showing the distribution of data over time.
    Gridlines: The plots include gridlines for easier readability of values.

# **How to Use**

    Select a Country: Use the dropdown menu in the sidebar titled 'Select a Country' to choose the country you want to analyze. 'Benin' is selected by default.
    Select Variable(s): Use the multi-select option in the sidebar titled 'Select a Variable' to choose the solar radiation variable(s) you are interested in. 'GHI' is selected by default.
    View Boxplots: Based on your selections, the dashboard will display one or more boxplots horizontally. Each boxplot represents the distribution of a selected variable for the chosen country.

# **Data Source**

The data for this dashboard is loaded from the CSV file located locally.

# **Technical Details**

    The dashboard is built using the Streamlit library in Python.
    Data manipulation is handled by the pandas library.
    Visualizations are created using the seaborn and matplotlib libraries.

# **Setup**

To run this dashboard locally, you will need to have Python installed, along with the required libraries.

    Install Libraries: 
                    pip install streamlit pandas seaborn matplotlib
    Save the Code: Save the dashboard code as a Python file (e.g., dashboard.py).
    Run the Dashboard: Open your terminal or command prompt, navigate to the directory where you saved the file, and run:  
                    streamlit run dashboard.py
                    This will start the Streamlit server and open the dashboard in your web browser.


# **Note**

    The data file path is hardcoded in the script. If you move the data file, you will need to update the path in the pd.read_csv() line.
    The list of available countries in the sidebar is currently hardcoded (['Benin', 'Sierraleone', 'Togo']). If your data includes more countries you wish to make available, you will need to update this list.

# **Future Improvements**

    Add more interactive features, such as date range selection.
    Include other types of visualizations.
    Implement error handling for file loading.
    Dynamically load the list of countries from the data file.
