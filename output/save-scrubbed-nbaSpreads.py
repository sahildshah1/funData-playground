

import pandas as pd

raw_dataframe = pd.read_csv("../data/nba-against-the-spread.csv")


#Build scrubbed_dataframe by looping over each column, splitting strings, 
#and then casting to numeric type, renaming column names etc and save to a file to load  
#and analzye 

# str.split works on Series (i.e. each column of the data frame) so loop over columns and concat
# b/c split apply combine group by or apply function's didn't work and there's only 9 columns

scrubbed_dataframe = raw_dataframe.iloc[:,0] # initalize scrubbed data frame 

for column_position in list(range(1,10)):

    scrubbed_dataframe = pd.concat([scrubbed_dataframe,
                                    raw_dataframe.iloc[:,column_position].str.split('-', expand = True)], 
                                    axis=1)


#Drop first row of "Team Total None None Home" and name columns 

scrubbed_dataframe = scrubbed_dataframe.drop(scrubbed_dataframe.index[0])

header =                     ["Team",
                              "SU_T_W",
                              "SU_T_L",
                              "SU_T_D",
                              "SU_H_W",
                              "SU_H_L",
                              "SU_H_D",
                              "SU_A_W",
                              "SU_A_L",
                              "SU_A_D",
                              "AS_T_W",
                              "AS_T_L",
                              "AS_T_D",
                              "AS_H_W",
                              "AS_H_L",
                              "AS_H_D",
                              "AS_A_W",
                              "AS_A_L",
                              "AS_A_D",
                              "OU_T_W",
                              "OU_T_L",
                              "OU_T_D",
                              "OU_H_W",
                              "OU_H_L",
                              "OU_H_D",
                              "OU_A_W",
                              "OU_A_L",
                              "OU_A_D"]



scrubbed_dataframe.columns = header

# Convert to integer and divide total number of games by 82

temp_dataframe = scrubbed_dataframe.iloc[:,1:].apply(pd.to_numeric)/82



scrubbed_dataframe.iloc[:,1:] = temp_dataframe


# Convert to numeric  https://stackoverflow.com/questions/15891038/change-data-type-of-columns-in-pandas

# errors = ignore ignores converting to numeric if invalid value is encountered 

df2 = scrubbed_dataframe.apply(pd.to_numeric, 
                               errors='ignore')


# Save dataframe as a pickle 

scrubbed_nbaSpreads = df2

scrubbed_nbaSpreads.to_pickle("./scrubbed_nbaSpreads.pkl")  



