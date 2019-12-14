from random import randint
import random




def main():
    total_num_fishes = int(input('What is the total number of fishes? '))
    fishes = [i for i in random.sample(range(1,1000), total_num_fishes)]
    fishes_directions = [randint(0,1) for _ in range(total_num_fishes)]
    j = 0
    hunter = int()
    while fishes_directio :
        if fishes[j] > fishes[j+1] and fishes_directions[j] != fishes_directions[j+1]:
            fishes.remove(fishes[j+1])
            fishes_directions.remove(fishes_directions[j+1])
        elif fishes[j] < fishes[j+1] and fishes_directions[j] != fishes_directions[j+1]:
            fishes.remove(fishes[j])
            fishes_directions.remove(fishes_directions[j])
        elif fishes[j] and  fishes[j+1] and fishes_directions[j] == fishes_directions[j+1]:






if __name__ == '__main__':
    main()