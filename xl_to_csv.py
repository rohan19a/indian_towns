import pandas as pd
  
# Read and store content
# of an excel file 
read_file = pd.read_excel ("PC11_TV_DIR.xlsx")
  
# Write the dataframe object
# into csv file
read_file.to_csv ("census_data_towns_and_vilalges.csv", 
                  index = None,
                  header=True)
    
# read csv file and convert 
# into a dataframe object
  
# show the dataframe