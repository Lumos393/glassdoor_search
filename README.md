# glassdoor_search
 
Two programs:
1. Find new HR jobs posted (Primary)
2. Go through Ashley's favorites list and copy data to Excel (Secondary)


Program #1
-----------

Program requirements:
1. Search Glassdoor for new HR jobs
    i.      Ignore sponsored posts
    ii.     Return results from multiple pages of search results
    iii.    Ignore duplicates
    iv.     Not overload server with requests
2. Save results to existing Excel workbook
    i.      New sheet per day?
    ii.     Name new sheets as that day's date
    iii.    Avoid overwriting existing data
3. Be packaged in an easy executable for Ashley to use

Steps:
1. Research best way to complete program and modules needed
    i.      Conflicts with OneDrive?
2. Identify Glassdoor URLs to search
3. Identify unique reference to parts of HTML to pull
4. Write code