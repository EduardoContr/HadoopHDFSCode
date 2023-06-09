# HadoopHDFSCode
Hadoop File System - Ambari, interface for uploading and organizing jobs, MR (Map Reduce) Code
In order to parse data from a warehouse, Map Reduce (MR) code is designed in order to analyze commonly known questions without employing
heavier workloads involving SSRS (Sql Server Reporting Services) best for more general queries - in other words ad hoc queries with some
value but not always key performamce indicators (kpi) from this contextual nature should be handled with less logical and mechanical overhead.  In this file I chose to look at a common query, what stocks in certain watchlists (Bottom Triangular Wedge pattern - Watchlist, Electric Vehicle (EV) battery -Watchlist(2), and from March 2022 - Watchlist(3)*(watchlist 3 is a generic watchlist of some interesting stocks from that particular month and year that caught the attention of some traders due to large moves or events)
Schema: datawarehouse, fact table, [{colname:Symbol},{colname2:Bid},{colname3:Ask}..{colname13:range}
(column headings/names in sum:  Symbol, Bid, Ask, Price, CHg$, Chg%, Open, High, Low, Vol., Watchlist, Date/Timestamp, Range(1 to 4 % pos/neg)
sql is select the rows where columnname range is in "1", e.g., and query "count" of this select query -> running them in parallel with mapper and reducer jobs seems logically easier in Map Reduce using python and MR jobs.  Again in sql running the query for each value for Rangewould be done synchronously whereas Map Reduce would run parallel jobs and in the clusters employing multiple machines that would run them in parallel with greater efficiency. 

Files included in folder:
1) csv file of fact table (datawarehouse object) containing columns i.d.'d above
2) csv file containing the primary key value pairs/foreign keys for the corresponding symbol and symbol i.d. corresponding to the symbol, the watchlistname and watchlist i.d. that are corresponding values to the primary csv file the fact table.
3) code file for use with any ide for Python, Intellij, VSCode, Atom, Jupyter Notebooks, Cloud based notebooks (databricks)
4) pending - sql object, code for the comparison of the legwork/effort

