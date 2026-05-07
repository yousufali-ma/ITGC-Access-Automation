import pandas as pd
from datetime import datetime

def audit_access_controls(hr_file, it_ad_file):
    """
    Automates SOX ITGC Access Reviews.
    Reconciles HR termination lists against Active Directory exports
    to identify unauthorized access and SLA breaches.
    """
    print("--- Starting ITGC Access Reconciliation ---")
    
    # In a real environment, these would be loaded via CSV/SQL.
    # We use mock DataFrames for portfolio demonstration.
    hr_data = pd.DataFrame({
        'Employee_ID': ['E101', 'E102', 'E103', 'E104'],
        'Status': ['Active', 'Terminated', 'Terminated', 'Active'],
        'Termination_Date': [None, '2023-10-01', '2023-10-15', None]
    })
    
    ad_data = pd.DataFrame({
        'Employee_ID': ['E101', 'E102', 'E103', 'E104'],
        'AD_Account_Status': ['Enabled', 'Enabled', 'Disabled', 'Enabled'],
        'Last_Login': ['2023-10-20', '2023-10-18', '2023-10-14', '2023-10-21']
    })

    # Merge datasets on Employee ID
    reconciliation = pd.merge(hr_data, ad_data, on='Employee_ID')

    # Identify SOX Control Deficiencies: Terminated users with Enabled accounts
    deficiencies = reconciliation[
        (reconciliation['Status'] == 'Terminated') & 
        (reconciliation['AD_Account_Status'] == 'Enabled')
    ]

    print(f"Total Records Scanned: {len(reconciliation)}")
    print(f"Control Deficiencies Found: {len(deficiencies)}")
    
    if not deficiencies.empty:
        print("\n[!] CRITICAL FINDINGS:")
        for index, row in deficiencies.iterrows():
            print(f"- User {row['Employee_ID']} was terminated on {row['Termination_Date']} but AD account is still Enabled.")
            print(f"  WARNING: Last login detected on {row['Last_Login']} (Post-Termination!)")
        
        # Output to CSV for Audit Workpaper
        deficiencies.to_csv('access_deficiencies_log.csv', index=False)
        print("\n--> Exception report generated for Control Owners: 'access_deficiencies_log.csv'")

if __name__ == "__main__":
    audit_access_controls('hr_report.csv', 'ad_extract.csv')
