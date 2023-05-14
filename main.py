

class Puzzle(object):
    def main(self):
        print("Welcome to puzzle solver by Ritesh Singh.\n")

        initialChoice = input('You can have either default initial state or enter your own. Press "1" for default and press any other key for entering your own initial state.')
        puzzleMat = []

        puzzleSize = 3 #we can change this number to make 8 puzzle into another puzzles

        
        if initialChoice == "1":
            puzzleMat.append(['1', '0', '2'])
            puzzleMat.append(['4', '3', '5'])
            puzzleMat.append(['7', '8', '6'])

        else:
            print('Enter the intital state of the puzzle:')

            for i in range(puzzleSize):
                r = input('Enter row ' + str(i+1) + '(give a space between each number, enter only three numbers per row(for 8 puzzle) then press enter):')
                puzzleMat.append(r.split(' '))

        print(puzzleMat)

if __name__ == '__main__':
  Puzzle().main()