def extract_revenue(df, num_periods):
    import re
    accounts = {}
    from support.definitions import rev_include_patterns, rev_exclude_patterns

    for idx, row in df.iterrows():
        account_name = str(row.iloc[0]).lower()
        for pattern in rev_include_patterns:
            if re.search(pattern, account_name):
                excluded = any(re.search(exclude_pattern, account_name) for exclude_pattern in rev_exclude_patterns)
                if excluded:
                    continue

                pattern_found = pattern
                values = []
                for cell in row.iloc[1:]:
                    try:
                        val = float(cell)
                        values.append(val)
                        if len(values) >= num_periods:
                            break
                    except:
                        continue
                accounts[pattern_found] = values
    
    sum_accounts = [sum(vals) for vals in zip(*accounts.values())]
    return sum_accounts if sum_accounts else []

def extract_expenses(df, num_periods):
    import re
    accounts = {}
    from support.definitions import exp_patterns

    for idx, row in df.iterrows():
        account_name = str(row.iloc[0]).lower()
        for pattern in exp_patterns:
            if re.search(pattern, account_name):

                pattern_found = pattern
                values = []
                for cell in row.iloc[1:]:
                    try:
                        val = float(cell)
                        values.append(val)
                        if len(values) >= num_periods:
                            break
                    except:
                        continue
                accounts[pattern_found] = values
    
    sum_accounts = [sum(vals) for vals in zip(*accounts.values())]
    return sum_accounts if sum_accounts else []

def extract_account(df, account_type, num_periods):
    import re
    accounts = {}
    match account_type:
        case 'ar':
            from support.definitions import ar_patterns_primary, ar_patterns_secondary
            pattern_match_primary = ar_patterns_primary
            pattern_match_secondary = ar_patterns_secondary
        
        case 'ap':
            from support.definitions import ap_patterns_primary, ap_patterns_secondary
            pattern_match_primary = ap_patterns_primary
            pattern_match_secondary = ap_patterns_secondary

        case 'inv':
            from support.definitions import inv_patterns_primary, inv_patterns_secondary
            pattern_match_primary = inv_patterns_primary
            pattern_match_secondary = inv_patterns_secondary
            
        case _:
            return []

    for idx, row in df.iterrows():
        account_name = str(row.iloc[0]).lower()
        for pattern in pattern_match_primary:
            if re.search(pattern, account_name):
                pattern_found = pattern
                values = []
                for cell in row.iloc[1:]:
                    try:
                        val = float(cell)
                        values.append(val)
                        if len(values) >= num_periods:
                            break
                    except:
                        continue
                return values

    for idx, row in df.iterrows():
        account_name = str(row.iloc[0]).lower()
        for pattern in pattern_match_secondary:
            if re.search(pattern, account_name):
                pattern_found = pattern
                values = []
                for cell in row.iloc[1:]:
                    try:
                        val = float(cell)
                        values.append(val)
                        if len(values) >= num_periods:
                            break
                    except:
                        continue
                accounts[pattern_found] = values
    
    sum_accounts = [sum(vals) for vals in zip(*accounts.values())]
    return sum_accounts if sum_accounts else []
