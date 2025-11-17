def address (**kwargs):
    for key,val in kwargs.items():
        print(f"{key:<7} : {val:>15}")

address(street="1115 Lucknow St",
        city="halifax",
        state="NS")