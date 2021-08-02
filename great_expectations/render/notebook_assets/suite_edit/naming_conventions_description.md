<p><font color='grey' size='2em'><em>There are a couple of ways by which you can define the data to be tested 
    <ul>
        <li>Specifying Query String in case of specific subset/rows for a table. Joining across tables is currently supported only for Canonical zone.</li>
        <li>Specifying database name and table name</li>
        </ul>
    This template will help you create a single expectations_suite at a time.
   </em></font></p>
   
<p><font color='green' size='2em'><em><strong>Suite Naming Conventions</strong><br/>
Datasource by query: {zone}.{database}.{tid}.{suite_description}<br/>
    Datasource by table: {zone}.{database}.{table}<br/>
    where tid = team id, zone=ledger/quarantine<br/>
    <strong>These database & table names should be as per Data Dictionary Naming Standards. </strong>
</em></font></p>