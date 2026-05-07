# ITGC Access Automation & SOX Reconciliation
**Author:** Yousuf Ali Shaik | IT Risk & Controls Analyst

### Overview
This project demonstrates the automation of a core IT General Control (ITGC): the **User Access Review / Leavers Process**. 

In enterprise environments, a major SOX deficiency occurs when an employee is terminated by HR, but IT fails to revoke their Active Directory/ERP access within the required SLA (e.g., 24 hours). 

### What This Script Does
Instead of manually using Excel VLOOKUPs to compare thousands of rows of Information Produced by the Entity (IPE), this Python Pandas script:
1. Ingests the HR Termination list.
2. Ingests the Active Directory (AD) account status extract.
3. Automatically reconciles the two datasets.
4. Flags **Control Deficiencies** (Terminated users with 'Enabled' accounts).
5. Highlights high-risk anomalies (e.g., Logins occurring *after* the HR termination date).
6. Exports an automated exception log for audit workpapers.

**Skills Demonstrated:** Python (Pandas), SOX 404 Compliance, ITGC Testing (ToE), IPE Validation, Segregation of Duties (SoD).
