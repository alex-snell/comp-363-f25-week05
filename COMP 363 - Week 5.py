class NeedlemanWunch():
    table: list[list[str]| int] = []

    def __init__(self):
        self.table = []
        
        
    def _needleman_wunch(self, A: str, B: str):
        #initilize points
        match = 1
        gap_penalty = -2
        mismatch_penalty = -1
        #itnitilize rows  & columns with +1 for setting up 
        rows = len(B) +1
        columns = len(A) + 1
        #intilize matrix for score and direction
        scoring_matrix = [[0 for _ in range(columns)] for _ in range(rows)]
        direction_matrix = [["" for _ in range(columns)] for _ in range(rows)]

        #initilize base case
        for i in range(rows-1):
            scoring_matrix[i][0] = i * gap_penalty
            direction_matrix[i][0] = "UP"
        for j in range(columns-1):
            scoring_matrix[0][j] = j * gap_penalty
            direction_matrix[0][j] = "LEFT"
        direction_matrix[0][0] = "DONE"


        for i in range(1,rows):
            #in range start at 1 and go to rows-1
            for j in range(1, columns):
                #if the letter is the same at the same spot
                if B[i-1] == A[j-1]:
                    #diagonal score for a match
                    diagonal_score = scoring_matrix[i-1][j-1] + match
                else:
                    #mismatch penalty not gap
                    diagonal_score = scoring_matrix[i-1][j-1] + mismatch_penalty
                #these are the gap penalties, if the penalty is not as bad as the gap
                up_score = scoring_matrix[i-1][j] + gap_penalty #A gap
                left_score = scoring_matrix[i][j-1] + gap_penalty #B gap
                #
                max_score = max(diagonal_score,up_score,left_score)
                scoring_matrix[i][j] = max_score

                if max_score == diagonal_score:
                    direction_matrix[i][j] = "DIAGONAL"
                elif max_score == up_score:
                    direction_matrix[i][j] = "UP"
                else:
                    direction_matrix[i][j] = "LEFT"
        #everything from here down works
        alignA = ""
        alignB = ""
        #set i and j
        i = rows -1
        j = columns -1
        #set up alignment by going until one reaches 0
        while i > 0 or j > 0:
            direction = direction_matrix[i][j]

            if direction == "DIAGONAL":
                #since i = rows -1, for indexing subtract one more (j as well)
                alignA = A[j-1] + alignA
                alignB = B[i-1] + alignB
                i -= 1
                j -= 1
            #if its up add a gap to A due to table structue, 
            #decrease i to continue down the row
            elif direction == "UP":
                alignA = '-' + alignA
                alignB = B[i-1] + alignB
                i -= 1
            #if its left add a gap to B due to table structure
             #decrease j to continue down the column
            elif direction == "LEFT":
                alignA = A[j-1] + alignA
                alignB = '-' + alignB
                j -= 1
            
        return alignA,alignB, scoring_matrix
    
    def getComparisons(self, tests):
        for i in range(len(tests)):
            A = tests[i][0]
            B = tests[i][1]
            a, b, matrix = self._needleman_wunch(A,B)
            print("A:",a)
            print("B:",b)
            #print(matrix)
            print("")
            

tests = [
    ["CRANE", "RAIN"],
    ["CYCLE", "BICYCLE"],
    ["ASTRONOMY", "GASTRONOMY"],
    ["INTENTION", "EXECUTION"],
    ["AGGTAB", "GXTXAYB"],
    ["GATTACA", "GCATGCU"],
    ["DELICIOUS", "RELIGIOUS"],
]

algorithm = NeedlemanWunch()
algorithm.getComparisons(tests)

tests1 = [
    ["GCATGCU", "GATTACA"],
    ["KITTEN", "SITTING"],
    ["SATURDAY", "SUNDAY"],
    ["ALGORITHM", "ALTRUISTIC"],
    ["POLYNOMIAL", "EXPONENTIAL"],
    ["ROSALIND", "ROSALINE"],
    ["ACGTACGT", "ACGTTGCA"],
    ["MOUSE", "HOUSE"],
    ["FLOWER", "FLOW"],
    ["PYTHON", "PYTON"],
    ["MANHATTAN", "MANHATTAN"],
    ["ABCDEF", "AZCED"],
    ["TGCATAT", "ATCCGAT"],
    ["BANANA", "BAHAMA"],
    ["COMPUTER", "COMMUTER"],
    ["DYNAMIC", "DIAPHRAGM"],
    ["ALIGNED", "ASSIGNMENT"],
    ["TEACHER", "PREACHER"],
    ["NEEDLE", "NOODLE"],
    ["SEQUENCE", "CONSEQUENCE"]
]
algorithm.getComparisons(tests1)