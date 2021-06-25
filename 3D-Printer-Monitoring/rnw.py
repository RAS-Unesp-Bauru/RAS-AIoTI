from pombo import Pigeon as p

def main():

    while True:
        x = p.sedex()
        if x:
            print('Hello World!')
            x = p.off()
        else:
            continue 

main()
