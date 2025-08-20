def convert_be_to_ad(be_year: int) -> int:
    ad_year = be_year - 543
    return(ad_year)

be_year = 2567
print(convert_be_to_ad(be_year))