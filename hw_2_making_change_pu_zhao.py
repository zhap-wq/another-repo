def make_change(owed_change):
    n_q=owed_change//25
    r1=owed_change%25
    n_d=r1//10
    r2=r1%10
    n_n=r2//5
    n_p=r2%5
    print(f' Your change:{n_q} quarters {n_d} dimes {n_n} nickels {n_p} pennies')
def main():
    o=int(input(' Amount of change owned (up to 99 cents):'))
    make_change(o)

main()
