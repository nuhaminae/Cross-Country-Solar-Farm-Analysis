import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#set page title
st.set_page_config(page_title='Country Solar Farm Data Analysis Dashboard')
st.title('Cross Country Solar Farm Data Analysis')

df = pd.read_csv('C:/Users/nuhamin/Documents/kifiya/week 0/Cross-Country-Solar-Farm-Analysis/data/All_Countries_df.csv', header=[0, 1])

#widget to select country 
st.sidebar.header('Select a Country')
all_countries = ['Benin', 'Sierraleone', 'Togo']
selected_country = st.sidebar.selectbox(
    ' ', all_countries, 
    index=all_countries.index('Benin')  #set 'Benin' as default
)

#widget to select variables
st.sidebar.header('Select a Variable')
all_variables = ['GHI','DNI', 'DHI']
selected_variable = st.sidebar.multiselect(
    ' ',all_variables,
    default='GHI' #select GHI by default
)

#show barplot
#filter data based on selected country
if selected_country:
    df_filtered_country = df[selected_country]

    #show visualizations for selected variables
    if selected_variable:
        num_variables = len(selected_variable)
        fig, axes = plt.subplots(1, num_variables, figsize=(num_variables * 5, 6))

        #ensure axes is an iterable
        if num_variables == 1:
            axes = [axes]

        #iterate through the selected variables and plot each on a different subplot
        for i, variable in enumerate(selected_variable):
            sns.boxplot(data=df_filtered_country, y=variable, ax=axes[i])
            axes[i].grid(True)
            axes[i].set_xlabel('Country', fontsize=12)
            axes[i].set_ylabel(variable, fontsize=12)
            axes[i].set_title(f'{variable} for {selected_country}')

        #adjust layout
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig) #close the figure to free up memory