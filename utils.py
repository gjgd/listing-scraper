def filter_out_parking(df):
  df = df[(df['Row'] != "PARKI")]
  df = df[(df['Section'] !=  "PARKING")]
  return df
