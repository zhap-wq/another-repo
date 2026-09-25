def refrain ():
    print("And they all go marching down,")
    print("To the ground, to get out, of the rain.")
    print("BOOM! BOOM! BOOM!")

def verse(number,action):
    print(f'The ants go marching {number} by {number} hurrah, hurrah.')
    print(f'The ants go marching {number} by {number} hurrah, hurrah.')
    print(f'The ants go marching {number} by {number},')
    print(f'The little one stops to  {action}.')
    refrain()
    print( )

def main ():
    verse('one','suck his thumb')
    verse('two','tie her shoe')
    verse('three','climb a tree')
    verse('four','shut the door')
    verse('five','take a dive')
    verse('six','pick up sticks')
    verse('seven','pray to heaven')
    verse('eight','check the gate')
    verse('nine','check the time')
    verse('ten','say “The End!”')
main()
    
