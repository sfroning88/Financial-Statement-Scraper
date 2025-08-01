date_patterns = [
            r'\bFY\s*(20\d{2})\b',
            r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s*(20\d{2})\b',
            r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s*(20\d{2})\b',
            r'\bQ[1-4]\s*(20\d{2})\b', r'\bQ[1-4]\s*FY\s*(20\d{2})\b',
            r'\b(20\d{2})[-/](20\d{2})\b', r'\b(20\d{2})[/-](0?[1-9]|1[0-2])\b',
            r'\b(0?[1-9]|1[0-2])[/-](20\d{2})\b',
            r'\b(0?[1-9]|[12]\d|3[01])[/-](0?[1-9]|1[0-2])[/-](20\d{2})\b',
            r'\b(0?[1-9]|[12]\d|3[01])[/-](0?[1-9]|1[0-2])[/-](20\d{2})\b',
            r'\b(0?[1-9])/(0?[1-9]|1[0-2])/(20\d{2})\b',
            r'\b(0?[1-9]|1[0-2])/(0?[1-9]|[12]\d|3[01])/(20\d{2})\b'
    ]

ar_patterns_primary = [
        r'accounts receivable', r'\ba\/r\b', r'\bar\b', r'trade receivables',
        r'customer receivables', r'notes receivable', r'bills receivable', r'receivables',
        r'accounts receivables', r'net receivables', r'gross receivables', r'current receivables',
        r'non-current receivables', r'other receivables'
    ]
        
ar_patterns_secondary = [
        r'loans receivable', r'advances to suppliers',
        r'advances to employees', r'advances to related parties', r'due from customers', r'due from affiliates',
        r'due from related parties', r'due from employees', r'due from officers', r'due from directors',
        r'due from shareholders', r'due from subsidiaries', r'due from parent', r'due from associates',
        r'due from joint ventures', r'due from partners', r'due from others', r'accounts and notes receivable',
        r'bills and accounts receivable', r'accounts receivable - trade', r'accounts receivable - other',
        r'accounts receivable - related parties', r'accounts receivable - affiliates', r'accounts receivable - employees',
        r'accounts receivable - officers', r'accounts receivable - directors', r'accounts receivable - shareholders',
        r'accounts receivable - subsidiaries', r'accounts receivable - parent', r'accounts receivable - associates',
        r'accounts receivable - joint ventures', r'accounts receivable - partners', r'accounts receivable - others',
        r'accounts receivable, net', r'accounts receivable, gross', r'accounts receivable, current', r'accounts receivable, non-current',
        r'accounts receivable, trade', r'accounts receivable, other', r'accounts receivable, related parties',
        r'accounts receivable, affiliates', r'accounts receivable, employees', r'accounts receivable, officers',
        r'accounts receivable, directors', r'accounts receivable, shareholders', r'accounts receivable, subsidiaries',
        r'accounts receivable, parent', r'accounts receivable, associates', r'accounts receivable, joint ventures',
        r'accounts receivable, partners', r'accounts receivable, others', r'trade debtors', r'customer accounts',
        r'customer balances', r'customer invoices', r'customer accounts receivable', r'customer trade receivables',
        r'customer notes receivable', r'customer bills receivable', r'customer receivable', r'customer trade receivable',
        r'customer note receivable', r'customer bill receivable', r'customer loan receivable', r'customer advance',
        r'customer deposit', r'customer prepayment', r'customer credit', r'customer debit', r'customer due',
        r'customer outstanding', r'customer balance', r'customer invoice', r'customer account receivable',
        r'customer trade receivable', r'customer note receivable', r'customer bill receivable', r'customer loan receivable',
        r'customer advance', r'customer deposit', r'customer prepayment', r'customer credit', r'customer debit',
        r'customer due', r'customer outstanding', r'customer balance', r'customer invoice', r'customer account receivable'
    ]

ap_patterns_primary = [
        r'accounts payable', r'\ba\/p\b', r'\bap\b', r'trade payables',
        r'vendor payables', r'bills payable', r'notes payable', r'payables',
        r'accounts payables', r'net payables', r'gross payables', r'current payables',
        r'non-current payables', r'other payables'
    ]
        
ap_patterns_secondary = [
        r'loans payable', r'advances from customers',
        r'advances from employees', r'advances from related parties', r'due to suppliers', r'due to affiliates',
        r'due to related parties', r'due to employees', r'due to officers', r'due to directors',
        r'due to shareholders', r'due to subsidiaries', r'due to parent', r'due to associates',
        r'due to joint ventures', r'due to partners', r'due to others', r'accounts and notes payable',
        r'bills and accounts payable', r'accounts payable - trade', r'accounts payable - other',
        r'accounts payable - related parties', r'accounts payable - affiliates', r'accounts payable - employees',
        r'accounts payable - officers', r'accounts payable - directors', r'accounts payable - shareholders',
        r'accounts payable - subsidiaries', r'accounts payable - parent', r'accounts payable - associates',
        r'accounts payable - joint ventures', r'accounts payable - partners', r'accounts payable - others',
        r'accounts payable, net', r'accounts payable, gross', r'accounts payable, current', r'accounts payable, non-current',
        r'accounts payable, trade', r'accounts payable, other', r'accounts payable, related parties',
        r'accounts payable, affiliates', r'accounts payable, employees', r'accounts payable, officers',
        r'accounts payable, directors', r'accounts payable, shareholders', r'accounts payable, subsidiaries',
        r'accounts payable, parent', r'accounts payable, associates', r'accounts payable, joint ventures',
        r'accounts payable, partners', r'accounts payable, others', r'trade creditors', r'vendor accounts',
        r'vendor balances', r'vendor invoices', r'vendor accounts payable', r'vendor trade payables',
        r'vendor notes payable', r'vendor bills payable', r'vendor payable', r'vendor trade payable',
        r'vendor note payable', r'vendor bill payable', r'vendor loan payable', r'vendor advance',
        r'vendor deposit', r'vendor prepayment', r'vendor credit', r'vendor debit', r'vendor due',
        r'vendor outstanding', r'vendor balance', r'vendor invoice', r'vendor account payable',
        r'vendor trade payable', r'vendor note payable', r'vendor bill payable', r'vendor loan payable',
        r'vendor advance', r'vendor deposit', r'vendor prepayment', r'vendor credit', r'vendor debit',
        r'vendor due', r'vendor outstanding', r'vendor balance', r'vendor invoice', r'vendor account payable'
    ]

inv_patterns_primary = [
        r'inventory'
    ]
 
inv_patterns_secondary = [
        r'stock', r'raw materials', r'finished goods',
        r'work in progress', r'work-in-progress', r'wip', r'goods in process',
        r'merchandise', r'merchandise inventory', r'consignment', r'consigned goods',
        r'packing materials', r'supplies', r'parts', r'spare parts', r'components',
        r'production supplies', r'factory supplies', r'warehouse stock', r'warehouse inventory',
        r'operating supplies', r'goods for resale', r'goods held for sale', r'goods held for resale',
        r'raw material inventory', r'finished goods inventory', r'process inventory', r'cycle stock',
        r'safety stock', r'buffer stock', r'obsolete inventory', r'excess inventory', r'inventory reserves',
        r'net inventory', r'gross inventory', r'current inventory', r'non-current inventory',
        r'perpetual inventory', r'periodic inventory', r'physical inventory', r'inventory on hand',
        r'inventory in transit', r'inventory valuation', r'inventory adjustment', r'inventory write-down',
        r'inventory write-off', r'inventory shrinkage', r'inventory loss', r'inventory gain',
        r'inventory turnover', r'inventory balance', r'inventory account', r'inventory assets',
        r'inventory liability', r'inventory provision', r'inventory allowance', r'inventory impairment',
        r'inventory obsolescence', r'inventory markdown', r'inventory markup', r'inventory cost',
        r'inventory expense', r'inventory capital', r'inventory holding', r'inventory carrying',
        r'inventory management', r'inventory control', r'inventory audit', r'inventory count',
        r'inventory record', r'inventory report', r'inventory system', r'inventory tracking',
        r'inventory valuation method', r'inventory method', r'inventory classification', r'inventory type',
        r'inventory group', r'inventory category', r'inventory item', r'inventory unit', r'inventory quantity',
        r'inventory price', r'inventory value', r'inventory turnover ratio', r'inventory days', r'inventory period',
        r'inventory cycle', r'inventory analysis', r'inventory summary', r'inventory detail', r'inventory listing',
        r'inventory ledger', r'inventory schedule', r'inventory worksheet', r'inventory reconciliation',
        r'inventory adjustment entry', r'inventory transfer', r'inventory movement', r'inventory transaction',
        r'inventory receipt', r'inventory issue', r'inventory return', r'inventory disposal', r'inventory sale',
        r'inventory purchase', r'inventory acquisition', r'inventory addition', r'inventory reduction',
        r'inventory withdrawal', r'inventory consumption', r'inventory usage', r'inventory allocation',
        r'inventory distribution', r'inventory shipment', r'inventory delivery', r'inventory receipt note',
        r'inventory issue note', r'inventory transfer note', r'inventory adjustment note', r'inventory return note',
        r'inventory disposal note', r'inventory sale note', r'inventory purchase note', r'inventory acquisition note',
        r'inventory addition note', r'inventory reduction note', r'inventory withdrawal note', r'inventory consumption note',
        r'inventory usage note', r'inventory allocation note', r'inventory distribution note', r'inventory shipment note',
        r'inventory delivery note', r'inventory record note', r'inventory report note', r'inventory system note',
        r'inventory tracking note', r'inventory valuation method note', r'inventory method note', r'inventory classification note',
        r'inventory type note', r'inventory group note', r'inventory category note', r'inventory item note', r'inventory unit note',
        r'inventory quantity note', r'inventory price note', r'inventory value note', r'inventory turnover ratio note',
        r'inventory days note', r'inventory period note', r'inventory cycle note', r'inventory analysis note', r'inventory summary note',
        r'inventory detail note', r'inventory listing note', r'inventory ledger note', r'inventory schedule note', r'inventory worksheet note',
        r'inventory reconciliation note', r'inventory adjustment entry note', r'inventory transfer note', r'inventory movement note',
        r'inventory transaction note', r'inventory receipt note', r'inventory issue note', r'inventory return note', r'inventory disposal note',
        r'inventory sale note', r'inventory purchase note', r'inventory acquisition note', r'inventory addition note', r'inventory reduction note',
        r'inventory withdrawal note', r'inventory consumption note', r'inventory usage note', r'inventory allocation note', r'inventory distribution note',
        r'inventory shipment note', r'inventory delivery note'
    ]

rev_include_patterns = [
        r'revenue', r'sales', r'income', r'net sales', r'net revenue', r'gross sales', r'gross revenue',
        r'total revenue', r'total sales', r'operating revenue', r'operating income', r'operating sales',
        r'product revenue', r'product sales', r'service revenue', r'service sales', r'contract revenue',
        r'contract sales', r'project revenue', r'project sales', r'license revenue', r'license sales',
        r'royalty revenue', r'royalty sales', r'interest revenue', r'interest income', r'dividend revenue',
        r'dividend income', r'commission revenue', r'commission income', r'fee revenue', r'fee income',
        r'other revenue', r'other sales', r'other income', r'non-operating revenue', r'non-operating income',
        r'non-operating sales', r'non-operating revenue', r'non-operating income', r'non-operating sales',
        r'financial revenue', r'financial income', r'financial sales', r'financial revenue', r'financial income',
        r'financial sales', r'gain on sale', r'gain on disposal', r'gain on investment', r'gain on asset',
        r'gain on property', r'gain on equipment', r'gain on securities', r'gain on shares', r'gain on bonds',
        r'gain on derivatives', r'gain on foreign exchange', r'gain on currency', r'gain on revaluation',
        r'gain on fair value', r'gain on bargain purchase', r'gain on extinguishment', r'gain on restructuring',
        r'gain on settlement', r'gain on conversion', r'gain on modification', r'gain on transfer',
        r'gain on acquisition', r'gain on merger', r'gain on consolidation', r'gain on deconsolidation',
        r'gain on spin-off', r'gain on split-off', r'gain on split-up', r'gain on distribution',
        r'gain on dividend', r'gain on interest', r'gain on fee', r'gain on commission', r'gain on royalty',
        r'gain on license', r'gain on contract', r'gain on project', r'gain on service', r'gain on product',
        r'gain on sale of asset', r'gain on sale of property', r'gain on sale of equipment', r'gain on sale of securities',
        r'gain on sale of shares', r'gain on sale of bonds', r'gain on sale of derivatives', r'gain on sale of foreign exchange',
        r'gain on sale of currency', r'gain on sale of revaluation', r'gain on sale of fair value', r'gain on sale of bargain purchase',
        r'gain on sale of extinguishment', r'gain on sale of restructuring', r'gain on sale of settlement', r'gain on sale of conversion',
        r'gain on sale of modification', r'gain on sale of transfer', r'gain on sale of acquisition', r'gain on sale of merger',
        r'gain on sale of consolidation', r'gain on sale of deconsolidation', r'gain on sale of spin-off', r'gain on sale of split-off',
        r'gain on sale of split-up', r'gain on sale of distribution', r'gain on sale of dividend', r'gain on sale of interest',
        r'gain on sale of fee', r'gain on sale of commission', r'gain on sale of royalty', r'gain on sale of license',
        r'gain on sale of contract', r'gain on sale of project', r'gain on sale of service', r'gain on sale of product'
    ]

rev_exclude_patterns = [
        r'expense', r'cost', r'cogs', r'loss', r'other income', r'interest income', r'interest expense',
        r'operating expense', r'operating cost', r'operating loss', r'non-operating expense', r'non-operating cost',
        r'non-operating loss', r'financial expense', r'financial cost', r'financial loss', r'general expense',
        r'general cost', r'general loss', r'administrative expense', r'administrative cost', r'administrative loss',
        r'selling expense', r'selling cost', r'selling loss', r'marketing expense', r'marketing cost', r'marketing loss',
        r'research expense', r'research cost', r'research loss', r'development expense', r'development cost', r'development loss',
        r'restructuring expense', r'restructuring cost', r'restructuring loss', r'impairment expense', r'impairment cost',
        r'impairment loss', r'write-down', r'write-off', r'provision', r'allowance', r'bad debt', r'doubtful account',
        r'doubtful debt', r'doubtful receivable', r'doubtful loan', r'doubtful advance', r'doubtful deposit', r'doubtful prepayment',
        r'doubtful credit', r'doubtful debit', r'doubtful due', r'doubtful outstanding', r'doubtful balance', r'doubtful invoice',
        r'doubtful account receivable', r'doubtful trade receivable', r'doubtful note receivable', r'doubtful bill receivable',
        r'doubtful loan receivable', r'doubtful advance', r'doubtful deposit', r'doubtful prepayment', r'doubtful credit',
        r'doubtful debit', r'doubtful due', r'doubtful outstanding', r'doubtful balance', r'doubtful invoice', r'doubtful account payable',
        r'doubtful trade payable', r'doubtful note payable', r'doubtful bill payable', r'doubtful loan payable', r'doubtful advance',
        r'doubtful deposit', r'doubtful prepayment', r'doubtful credit', r'doubtful debit', r'doubtful due', r'doubtful outstanding',
        r'doubtful balance', r'doubtful invoice', r'doubtful account payable', r'doubtful trade payable', r'doubtful note payable',
        r'doubtful bill payable', r'doubtful loan payable', r'doubtful advance', r'doubtful deposit', r'doubtful prepayment',
        r'doubtful credit', r'doubtful debit', r'doubtful due', r'doubtful outstanding', r'doubtful balance', r'doubtful invoice'
    ]

exp_patterns = [
    r'cost of goods sold', r'supplies expense'
]
