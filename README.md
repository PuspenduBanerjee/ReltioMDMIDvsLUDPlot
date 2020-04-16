# ReltioMDMIDvsLUDPlot
 Plot Multiple set of AutoIncremented MDMID vs LastUpdate Date as TimeSeries Data
# Usecase:
    Recently noticed that the data synchronization between Reltio and Downstream system is not happening 
    for all the updated records in Reltio.
    To dig futher by MDM Unique Identifier present in Reltio  vs downstreams needed  a tool for visual representation.
    
# Result
    Built this tool using:
        1. Pandas
        2. Matplotlib
        
# $ value savings:
    Earlier, it was taking about :
        1. Process reltio export JSON file and Load in to a Relational Database
        2. Process Data from DownStream system and load to Same RDBMS
        3. Run queries to tally the data from #1 & #2 
        4. Overall approximately 2 hours per day =(2x$120=$240/Day)
        2. Cost of maintaining a Relational Database along with Historical data($10/Day)
     So, about $250/Day x 260 days = $65,000/year‬ has been saved
# Additional benefits:
    1. Run on-click on-demand
    2. Visually represent when the Data got created in Reltio 
    3. Visually represent if the data made its journey to downstream
    4. Provide visuall representation of such root-cause 
        i. if the data has been created in the system after synchronization process started or
        ii. really there is a process in sychronization