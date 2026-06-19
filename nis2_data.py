"""
NIS2 Directive (EU) 2022/2555 — Reference data layer
Sectors from Annex I & II, size thresholds, obligations, article citations.
"""

EU_MEMBER_STATES = [
    "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech Republic",
    "Denmark", "Estonia", "Finland", "France", "Germany", "Greece",
    "Hungary", "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg",
    "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovakia",
    "Slovenia", "Spain", "Sweden",
]

# ---------------------------------------------------------------------------
# Annex I — High Criticality Sectors → typically Essential Entities
# Annex II — Other Critical Sectors → typically Important Entities
# ---------------------------------------------------------------------------

NIS2_SECTORS = {
    "annex_i": {
        "label": "Annex I — High Criticality Sector",
        "default_classification": "essential",
        "sectors": {
            "energy": {
                "name": "Energy",
                "subsectors": {
                    "electricity": {
                        "name": "Electricity",
                        "description": "Generation, transmission, distribution or supply of electricity; operators of electricity distribution systems; electricity undertakings; operators of aggregation, demand response or energy storage; transmission system operators; charging point operators",
                    },
                    "district_heating": {
                        "name": "District heating and cooling",
                        "description": "Operators of district heating or district cooling",
                    },
                    "oil": {
                        "name": "Oil",
                        "description": "Operators of oil transmission pipelines; operators of oil production, refining, treatment, storage and transmission; central stockholding entities",
                    },
                    "gas": {
                        "name": "Gas",
                        "description": "Supply undertakings; distribution system operators; transmission system operators; storage system operators; LNG system operators; natural gas undertakings; operators of natural gas refining and treatment facilities",
                    },
                    "hydrogen": {
                        "name": "Hydrogen",
                        "description": "Producers, distributors or operators of hydrogen transmission",
                    },
                },
            },
            "transport": {
                "name": "Transport",
                "subsectors": {
                    "air": {
                        "name": "Air transport",
                        "description": "Air carriers used for commercial purposes; airport management bodies; operators of airports; traffic management control operators providing air traffic control",
                    },
                    "rail": {
                        "name": "Rail transport",
                        "description": "Infrastructure managers; railway undertakings; rail service facility operators",
                    },
                    "water": {
                        "name": "Water-borne transport",
                        "description": "Inland waterway, sea and coastal passenger and freight water transport companies; operators of management bodies of ports; vessel traffic service operators; operators of ship traffic management services",
                    },
                    "road": {
                        "name": "Road transport",
                        "description": "Road authorities responsible for traffic management control; operators of intelligent transport systems",
                    },
                },
            },
            "banking": {
                "name": "Banking",
                "subsectors": {
                    "credit_institutions": {
                        "name": "Credit institutions",
                        "description": "Credit institutions as defined in Article 4(1)(1) of Regulation (EU) No 575/2013",
                    },
                },
            },
            "financial_market": {
                "name": "Financial Market Infrastructures",
                "subsectors": {
                    "trading_venues": {
                        "name": "Operators of trading venues",
                        "description": "Operators of trading venues as defined in Article 4(1)(24) of Directive 2014/65/EU",
                    },
                    "ccps": {
                        "name": "Central counterparties (CCPs)",
                        "description": "Central counterparties as defined in Article 2(1) of Regulation (EU) No 648/2012",
                    },
                },
            },
            "health": {
                "name": "Health",
                "subsectors": {
                    "healthcare_providers": {
                        "name": "Healthcare providers",
                        "description": "Healthcare providers as defined in Article 3(g) of Directive 2011/24/EU",
                    },
                    "eu_reference_labs": {
                        "name": "EU reference laboratories",
                        "description": "EU reference laboratories referred to in Article 15 of Regulation (EU) 2022/2371",
                    },
                    "rnd_medicinal": {
                        "name": "R&D entities for medicinal products",
                        "description": "Entities carrying out research and development activities of medicinal products as defined in Article 1(2) of Directive 2001/83/EC",
                    },
                    "pharma": {
                        "name": "Pharmaceutical manufacturers",
                        "description": "Entities manufacturing basic pharmaceutical products and pharmaceutical preparations; entities manufacturing medical devices considered critical during a public health emergency",
                    },
                },
            },
            "drinking_water": {
                "name": "Drinking Water",
                "subsectors": {
                    "suppliers": {
                        "name": "Suppliers and distributors",
                        "description": "Suppliers and distributors of water intended for human consumption (excluding distributors where distribution is part of a general activity of distributing other commodities not critical for NIS2)",
                    },
                },
            },
            "waste_water": {
                "name": "Waste Water",
                "subsectors": {
                    "collectors": {
                        "name": "Waste water undertakings",
                        "description": "Undertakings collecting, disposing of or treating urban waste water, domestic waste water or industrial waste water (excluding distributors of water)",
                    },
                },
            },
            "digital_infrastructure": {
                "name": "Digital Infrastructure",
                "subsectors": {
                    "ixp": {
                        "name": "Internet exchange point (IXP) providers",
                        "description": "Providers of internet exchange points",
                    },
                    "dns": {
                        "name": "DNS service providers",
                        "description": "DNS service providers, excluding operators of root name servers",
                        "auto_in_scope": True,
                        "auto_in_scope_note": "DNS service providers are in scope regardless of size (Art. 2(2)(b))",
                    },
                    "tld": {
                        "name": "TLD name registries",
                        "description": "Top-level domain (TLD) name registries",
                        "auto_in_scope": True,
                        "auto_in_scope_note": "TLD registries are in scope regardless of size (Art. 2(2)(a))",
                    },
                    "cloud": {
                        "name": "Cloud computing service providers",
                        "description": "Cloud computing service providers",
                    },
                    "data_centres": {
                        "name": "Data centre service providers",
                        "description": "Data centre service providers",
                    },
                    "cdn": {
                        "name": "Content delivery network (CDN) providers",
                        "description": "Content delivery network providers",
                    },
                    "trust_services": {
                        "name": "Trust service providers",
                        "description": "Trust service providers",
                        "qualified_note": "Qualified trust service providers are in scope regardless of size (Art. 2(2)(c))",
                    },
                    "electronic_comms_networks": {
                        "name": "Public electronic communications network providers",
                        "description": "Providers of public electronic communications networks",
                    },
                    "electronic_comms_services": {
                        "name": "Public electronic communications service providers",
                        "description": "Providers of publicly available electronic communications services",
                    },
                },
            },
            "ict_services": {
                "name": "ICT Service Management (B2B)",
                "subsectors": {
                    "managed_services": {
                        "name": "Managed service providers (MSPs)",
                        "description": "Providers of managed services",
                    },
                    "managed_security": {
                        "name": "Managed security service providers (MSSPs)",
                        "description": "Providers of managed security services",
                    },
                },
            },
            "public_administration": {
                "name": "Public Administration",
                "subsectors": {
                    "central": {
                        "name": "Central government entities",
                        "description": "Public administration entities of central governments as defined by Member States in accordance with national law",
                        "auto_in_scope": True,
                        "auto_in_scope_note": "Central government public administration entities are in scope regardless of size",
                    },
                    "regional": {
                        "name": "Regional/local government entities",
                        "description": "Public administration entities at regional level — only where designated by the Member State in accordance with Art. 2(2)(f)",
                    },
                },
            },
            "space": {
                "name": "Space",
                "subsectors": {
                    "ground_infrastructure": {
                        "name": "Ground-based space infrastructure operators",
                        "description": "Operators of ground-based infrastructure owned, managed and operated by Member States or by private parties, that support the provision of space-based services (excluding providers of public electronic communications networks)",
                    },
                },
            },
        },
    },
    "annex_ii": {
        "label": "Annex II — Other Critical Sector",
        "default_classification": "important",
        "sectors": {
            "postal": {
                "name": "Postal and Courier Services",
                "subsectors": {
                    "postal": {
                        "name": "Postal and courier service providers",
                        "description": "Postal service providers including parcel delivery services",
                    },
                },
            },
            "waste": {
                "name": "Waste Management",
                "subsectors": {
                    "waste": {
                        "name": "Waste management undertakings",
                        "description": "Undertakings carrying out waste management as defined in Article 3(9) of Directive 2008/98/EC, excluding undertakings for whom waste management is not their principal economic activity",
                    },
                },
            },
            "chemicals": {
                "name": "Chemicals",
                "subsectors": {
                    "chemicals": {
                        "name": "Manufacture, production and distribution",
                        "description": "Undertakings manufacturing, producing or distributing chemical substances and mixtures, or undertakings producing articles from chemical substances or mixtures",
                    },
                },
            },
            "food": {
                "name": "Food",
                "subsectors": {
                    "food": {
                        "name": "Food businesses",
                        "description": "Food businesses engaged in wholesale distribution, industrial production and processing",
                    },
                },
            },
            "manufacturing": {
                "name": "Manufacturing",
                "subsectors": {
                    "medical_devices": {
                        "name": "Medical devices and IVDs",
                        "description": "Manufacturers of medical devices and in vitro diagnostic medical devices (NACE Rev. 2 C26.6, C32.5)",
                    },
                    "computers_electronics": {
                        "name": "Computers and electronic/optical products",
                        "description": "Manufacturers of computers and electronic and optical products (NACE Rev. 2 C26)",
                    },
                    "electrical_equipment": {
                        "name": "Electrical equipment",
                        "description": "Manufacturers of electrical equipment (NACE Rev. 2 C27)",
                    },
                    "machinery": {
                        "name": "Machinery and equipment",
                        "description": "Manufacturers of machinery and equipment not elsewhere classified (NACE Rev. 2 C28)",
                    },
                    "motor_vehicles": {
                        "name": "Motor vehicles, trailers, semi-trailers",
                        "description": "Manufacturers of motor vehicles, trailers and semi-trailers (NACE Rev. 2 C29)",
                    },
                    "other_transport": {
                        "name": "Other transport equipment",
                        "description": "Manufacturers of other transport equipment (NACE Rev. 2 C30)",
                    },
                },
            },
            "digital_providers": {
                "name": "Digital Providers",
                "subsectors": {
                    "online_marketplaces": {
                        "name": "Online marketplaces",
                        "description": "Providers of online marketplaces as defined in Art. 2(n) of Directive 2011/83/EU",
                    },
                    "search_engines": {
                        "name": "Online search engines",
                        "description": "Providers of online search engines as defined in Art. 2(6) of Regulation (EU) 2019/1150",
                    },
                    "social_networks": {
                        "name": "Social networking services platforms",
                        "description": "Providers of social networking services platforms",
                    },
                },
            },
            "research": {
                "name": "Research",
                "subsectors": {
                    "research_organisations": {
                        "name": "Research organisations",
                        "description": "Research organisations as defined in Article 2(1) of Regulation (EU) 2021/695, whose primary goal is to conduct applied research or experimental development with a view to exploiting the results commercially",
                    },
                },
            },
        },
    },
}

# ---------------------------------------------------------------------------
# Size thresholds — Art. 2 + Commission Recommendation 2003/361/EC
# ---------------------------------------------------------------------------

SIZE_THRESHOLDS = {
    "large": {
        "label": "Large enterprise",
        "employees": "≥ 250 employees",
        "turnover": "> €50 million annual turnover",
        "balance_sheet": "> €43 million balance sheet total",
        "note": "Meets ANY one of the above thresholds",
    },
    "medium": {
        "label": "Medium enterprise",
        "employees": "50–249 employees",
        "turnover": "≤ €50 million annual turnover",
        "balance_sheet": "≤ €43 million balance sheet total",
        "note": "Below large thresholds but ≥ 50 employees",
    },
    "small": {
        "label": "Small enterprise",
        "employees": "10–49 employees",
        "turnover": "≤ €10 million annual turnover",
        "balance_sheet": "≤ €10 million balance sheet total",
    },
    "micro": {
        "label": "Micro enterprise",
        "employees": "< 10 employees",
        "turnover": "≤ €2 million annual turnover",
        "balance_sheet": "≤ €2 million balance sheet total",
    },
}

# ---------------------------------------------------------------------------
# Obligations by classification
# ---------------------------------------------------------------------------

OBLIGATIONS = {
    "essential": {
        "label": "Essential Entity (EE)",
        "colour": "🔴",
        "summary": (
            "Your organisation is likely an **Essential Entity** under NIS2. "
            "Essential Entities are subject to proactive supervisory measures and the most stringent "
            "cybersecurity and incident reporting obligations."
        ),
        "articles": {
            "Art. 2": "Scope — your entity type and size fall within Annex I coverage",
            "Art. 3(1)": "Classification as an Essential Entity",
            "Art. 20": "Management bodies must approve cybersecurity risk-management measures and oversee implementation; managers must undertake cybersecurity training",
            "Art. 21": "Security measures — risk analysis, incident handling, business continuity, supply chain security, network security, access control, cryptography and encryption, HR security, MFA/continuous authentication, vulnerability disclosure",
            "Art. 23": "Incident reporting — early warning within 24 hours; notification within 72 hours; intermediate report on request; final report within 1 month",
            "Art. 24": "Use of European cybersecurity certification schemes where mandated by Commission implementing acts",
            "Art. 27": "Registration — entities must register with their national competent authority (NCA)",
            "Art. 32": "Supervisory and enforcement measures — proactive, including regular audits, on-site inspections, targeted security scans, requests for documentation",
            "Art. 34": "Administrative fines — up to €10 million or 2% of total worldwide annual turnover, whichever is higher",
        },
    },
    "important": {
        "label": "Important Entity (IE)",
        "colour": "🟡",
        "summary": (
            "Your organisation is likely an **Important Entity** under NIS2. "
            "Important Entities have the same technical security and incident reporting obligations as "
            "Essential Entities, but are subject to lighter-touch, reactive supervision."
        ),
        "articles": {
            "Art. 2": "Scope — your entity type and size fall within Annex I or Annex II coverage",
            "Art. 3(2)": "Classification as an Important Entity",
            "Art. 20": "Management bodies must approve cybersecurity risk-management measures; managers must undertake cybersecurity training",
            "Art. 21": "Security measures — same technical obligations as Essential Entities: risk analysis, incident handling, business continuity, supply chain security, access control, cryptography, MFA, vulnerability disclosure",
            "Art. 23": "Incident reporting — same timeline obligations as Essential Entities: 24h early warning, 72h notification, 1-month final report",
            "Art. 27": "Registration — entities must register with their national competent authority (NCA)",
            "Art. 33": "Supervisory and enforcement measures — reactive (ex-post), triggered by evidence of non-compliance or at NCA discretion",
            "Art. 34": "Administrative fines — up to €7 million or 1.4% of total worldwide annual turnover, whichever is higher",
        },
    },
    "out_of_scope": {
        "label": "Outside NIS2 Scope",
        "colour": "🟢",
        "summary": (
            "Based on your answers, your organisation does not appear to fall within the scope of NIS2. "
            "No mandatory obligations apply under this Directive. You may still voluntarily adopt the "
            "security measures in Art. 21 as best practice."
        ),
        "articles": {
            "Art. 2(1)": "NIS2 applies to entities of the type and size covered in Annexes I and II — your entity does not meet the threshold",
        },
    },
}

# ---------------------------------------------------------------------------
# Auto-in-scope triggers (Art. 2(2)) — bypass size thresholds
# ---------------------------------------------------------------------------

AUTO_IN_SCOPE_TRIGGERS = [
    {
        "id": "qualified_tsp",
        "label": "Qualified trust service provider",
        "article": "Art. 2(2)(c)",
        "note": "Qualified trust service providers are in scope regardless of size",
        "verdict": "essential",
    },
    {
        "id": "tld_registry",
        "label": "TLD name registry operator",
        "article": "Art. 2(2)(a)",
        "note": "TLD name registries are in scope regardless of size",
        "verdict": "essential",
    },
    {
        "id": "dns_provider",
        "label": "DNS service provider (excluding root servers)",
        "article": "Art. 2(2)(b)",
        "note": "DNS service providers are in scope regardless of size",
        "verdict": "essential",
    },
    {
        "id": "sole_provider",
        "label": "Sole provider of a service essential to society in your Member State",
        "article": "Art. 2(2)(d)",
        "note": "Sole providers of services essential to societal or economic activities are in scope regardless of size",
        "verdict": "essential",
    },
    {
        "id": "critical_infrastructure",
        "label": "Identified as critical infrastructure under the CER Directive (EU) 2022/2557",
        "article": "Art. 2(2)(e)",
        "note": "Critical entities designated under the CER Directive are in scope",
        "verdict": "essential",
    },
    {
        "id": "central_gov",
        "label": "Central government public administration entity",
        "article": "Art. 2(2)(f)",
        "note": "Central government entities are in scope regardless of size",
        "verdict": "essential",
    },
]
