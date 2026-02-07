def average_gdp(csv_data):
    gdp_by_country = {}

    for value in csv_data:
        if not gdp_by_country.get(value["country"], None):
            gdp_by_country[value["country"]] = []
        gdp_by_country[value["country"]].append(float(value["gdp"]))

    report_data = {"country": [], "gdp": []}
    for country, gdp in gdp_by_country.items():
        report_data["country"].append(country)
        report_data["gdp"].append(sum(gdp) / len(gdp))

    index_range = range(1, len(gdp_by_country) + 1)
    return report_data, index_range
